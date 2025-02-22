import logging
import numpy as np


# commonroad
from commonroad.planning.planning_problem import PlanningProblem
from commonroad.scenario.lanelet import Lanelet, LaneletNetwork
from commonroad.scenario.scenario import Scenario
from commonroad.scenario.state import InitialState


# Own code base
from commonroad_route_planner.planners.networkx import (
    NetworkxRoutePlanner,
)
from commonroad_route_planner.planners.no_goal_found_planner import (
    NoGoalFoundRoutePlanner,
)
from commonroad_route_planner.utility.route_util import (
    lanelet_orientation_at_position,
    relative_orientation,
)
from commonroad_route_planner.utility.overtake_init_state import OvertakeInitState
from commonroad_route_planner.lanelet_sequence import LaneletSequence


# typing
from typing import List, Union


class RoutePlanner:
    """
    This planner plans routes as sequences of lanelet ids in CommonRoad scenarios.
    """

    def __init__(
        self,
        lanelet_network: LaneletNetwork,
        planning_problem: PlanningProblem,
        scenario: Union[Scenario, None] = None,
        extended_search: bool = False,
        prohibited_lanelet_ids: List[int] = None,
        logging_level: int = logging.WARNING,
    ) -> None:
        """
        Initialization of a RoutePlanner object.

        :param lanelet_network: cr lanelet network
        :param planning_problem: cr planning problem
        :param extended_search: necessary, if not the shortest reference_path is searched, e.g.
            if a specific lanelet must be included
        :param prohibited_lanelet_ids: lanelets ids that must not be used
        :param logging_level: logging level, default to warning
        """

        self._logging_level = logging_level
        self._logger = logging.Logger(name=__name__, level=logging_level)

        self._scenario: Scenario = scenario

        self._lanelet_network: LaneletNetwork = lanelet_network
        self._planning_problem: PlanningProblem = planning_problem

        self._extended_search: bool = extended_search
        self._prohibited_lanelet_ids: List[int] = (
            prohibited_lanelet_ids if (prohibited_lanelet_ids is not None) else list()
        )

        self._id_lanelets_start: List[int] = list()
        self._overtake_states = list()
        self._ids_lanelets_goal: List[int] = list()
        self._init_lanelet_ids_for_start_and_overtake()
        self._init_goal_lanelet_ids()

        self._planner: Union[NetworkxRoutePlanner, NoGoalFoundRoutePlanner] = None
        self._init_planner()

    @property
    def lanelet_network(self) -> LaneletNetwork:
        """
        :return: lanelet network of scenario
        """
        return self._lanelet_network

    @property
    def planning_problem(self) -> PlanningProblem:
        """
        :return: planning problem of scenario
        """
        return self._planning_problem

    @property
    def prohibited_lanelet_ids(self) -> List[int]:
        """
        :return: list of prohibited lanelet ids
        """
        return self._prohibited_lanelet_ids

    def update_planning_problem_and_plan_routes(
        self,
        planning_problem: PlanningProblem,
        extended_search: bool = False,
        prohibited_lanelet_ids: List[int] = None,
    ) -> List[LaneletSequence]:
        """
        Updates planning problem and recomputes necessary parts.
        Returns a new reference_path selector.

        :param planning_problem: planning problem to update
        :param extended_search: whether extended search should be used
        :param prohibited_lanelet_ids: which lanelet ids must not be included in the reference_path

        :return: list of lanelet id sequence from start to goal.
        """
        # Reset lists
        self._id_lanelets_start = list()
        self._ids_lanelets_goal = list()
        self._overtake_states = list()

        # update planning problems
        self._planning_problem = planning_problem
        self._extended_search: bool = extended_search
        self._prohibited_lanelet_ids: List[int] = (
            prohibited_lanelet_ids if (prohibited_lanelet_ids is not None) else list()
        )

        self._init_lanelet_ids_for_start_and_overtake()
        self._init_goal_lanelet_ids()
        self._init_planner()

        return self.plan_routes()

    def plan_routes(self) -> List[LaneletSequence]:
        """
        Plans routes for every pair of start/goal lanelets. If no goal lanelet ID is given then return a survival reference_path.

        :return: list of lanelet id sequence from start to goal.
        """
        routes: List[LaneletSequence] = []

        for id_lanelet_start in self._id_lanelets_start:
            # if survival reference_path _planner
            if len(self._ids_lanelets_goal) == 0:
                routes.append(
                    LaneletSequence(
                        self._planner.find_routes(
                            id_lanelet_start, id_lanelet_goal=None
                        )
                    )
                )

            else:
                # if normal _planner iterate through goal lanelet ids
                for id_lanelet_goal in self._ids_lanelets_goal:
                    ids_lanelets = self._planner.find_routes(
                        id_lanelet_start=id_lanelet_start,
                        id_lanelet_goal=id_lanelet_goal,
                    )
                    routes.extend(
                        [LaneletSequence(lanelet_ids) for lanelet_ids in ids_lanelets]
                    )

        if len(routes) == 0:
            raise ValueError(
                f"Planner {self._planner} could not find a single reference_path"
            )

        return routes

    def _get_filtered_ids(self, ids_lanelets_to_filter: List[int]) -> List[int]:
        """Filters lanelets with the list of ids of forbidden lanelets.

        :param ids_lanelets_to_filter: The list of the lanelet ids which should be filtered
        :return: List of desirable lanelets
        """
        filtered_ids = list()
        for id_lanelet in ids_lanelets_to_filter:
            if id_lanelet not in self._prohibited_lanelet_ids:
                filtered_ids.append(id_lanelet)

        return filtered_ids

    def _init_planner(self) -> None:
        """
        Initialize planner
        """
        # if there are no lanelets of the goal, activate the NoGoalFound _planner
        if len(self._ids_lanelets_goal) == 0:
            self._logger.debug(
                "Starting NoGoalFound Planner, since no goal information was found"
            )
            self._planner = NoGoalFoundRoutePlanner(
                lanelet_network=self._lanelet_network,
                prohibited_lanelet_ids=self._prohibited_lanelet_ids,
                logger=self._logger,
            )

        # check different backend

        else:
            self._planner = NetworkxRoutePlanner(
                lanelet_network=self._lanelet_network,
                overtake_states=self._overtake_states,
                extended_search=self._extended_search,
                prohibited_lanelet_ids=self._prohibited_lanelet_ids,
                logger=self._logger,
            )

    def _init_lanelet_ids_for_start_and_overtake(self) -> None:
        """
        Retrieves the ids of the lanelets in which the initial position is situated.
        Also checks if the initial state is during a lanechange
        """

        initial_state: InitialState = self._planning_problem.initial_state

        # sanity check
        if not hasattr(initial_state, "position"):
            self._logger.error(
                "No initial position in the given planning problem found"
            )
            raise ValueError("No initial position in the given planning problem found")

        # Add start lanelets
        self._id_lanelets_start = self._get_filtered_ids(
            self._lanelet_network.find_lanelet_by_position([initial_state.position])[0]
        )

        # Check if any of the start positions are during an overtake:
        # if the car is not driving in the correct direction for the lanelet,
        # it will also consider routes taking an adjacent lanelet in the opposite direction
        if (
            hasattr(initial_state, "orientation")
            and not initial_state.is_uncertain_orientation
        ):
            orientation = initial_state.orientation

            for id_lanelet_start in self._id_lanelets_start:
                lanelet: Lanelet = self._lanelet_network.find_lanelet_by_id(
                    id_lanelet_start
                )
                lanelet_angle = lanelet_orientation_at_position(
                    lanelet, initial_state.position
                )

                # Check if the angle difference is larger than 90 degrees
                if abs(relative_orientation(orientation, lanelet_angle)) > 0.5 * np.pi:
                    if (
                        lanelet.adj_left is not None
                        and not lanelet.adj_left_same_direction
                    ):
                        overtake_state = OvertakeInitState(
                            id_lanelet_start, lanelet.adj_left, self._lanelet_network
                        )
                        self._overtake_states.append(overtake_state)

                    elif (
                        lanelet.adj_right is not None
                        and not lanelet.adj_right_same_direction
                    ):
                        overtake_state = OvertakeInitState(
                            id_lanelet_start, lanelet.adj_right, self._lanelet_network
                        )
                        self._overtake_states.append(overtake_state)

        if len(self._id_lanelets_start) > 1:
            self._logger.debug(
                "Multiple start lanelet IDs: some may fail to reach goal lanelet"
            )

        if len(self._id_lanelets_start) == 0:
            self._logger.error("No initial lanelet ids found")
            raise ValueError("No initial lanelet ids found")

    def _init_goal_lanelet_ids(self) -> None:
        """
        Sets the goal lanelet ids in the attribute.
        Takes first goal polygon for uncertain goal position
        """

        # If the goal region is directly defined by lanelets, use it
        if hasattr(self._planning_problem.goal, "lanelets_of_goal_position"):
            if self._planning_problem.goal.lanelets_of_goal_position is None:
                self._logger.debug("Lanelets_of_goal_position not given")

            else:
                for (
                    goal_lanelet_ids
                ) in self._planning_problem.goal.lanelets_of_goal_position.values():
                    self._ids_lanelets_goal.extend(
                        self._get_filtered_ids(goal_lanelet_ids)
                    )

        # if the goal region has a state list, also use it
        if hasattr(self._planning_problem.goal, "state_list"):
            for idx, state in enumerate(self._planning_problem.goal.state_list):

                if not hasattr(state, "position"):
                    self._logger.info(
                        "Goal state of state list has no position entry, will pass"
                    )
                    continue

                # set goal position, which can either be defined by center for regions or by position
                if hasattr(state.position, "center"):
                    goal_position: np.ndarray = state.position.center
                else:
                    # For uncertain position reference_path planner takes first polygon
                    self._logger.info(
                        "For goals with geometric shape as definition,"
                        " CR reference_path planner uses the center of the first shape"
                    )
                    goal_position: np.ndarray = state.position.shapes[0].center

                for lanelet_id_list in self.lanelet_network.find_lanelet_by_position(
                    [goal_position]
                ):
                    self._ids_lanelets_goal.extend(lanelet_id_list)

            # remove duplicated and filter for permitted lanelets
            self.ids_lanelets_goal = self._get_filtered_ids(
                list(set(self._ids_lanelets_goal))
            )

        if len(self.ids_lanelets_goal) == 0:
            self._logger.debug("Could not find a single goal position or lane")
