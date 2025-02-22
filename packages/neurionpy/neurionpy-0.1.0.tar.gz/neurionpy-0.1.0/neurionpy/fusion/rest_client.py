from google.protobuf.json_format import Parse

from neurionpy.common.rest_client import RestClient
from neurionpy.protos.neurion.fusion.query_pb2 import (
    QueryParamsRequest, QueryParamsResponse,
    QueryGetTaskRequest, QueryGetTaskResponse,
    QueryGetTaskRewardRequest, QueryGetTaskRewardResponse,
    QueryGetCreatorApplicantsRequest, QueryGetCreatorApplicantsResponse,
    QueryGetPendingCreatorApplicationsRequest, QueryGetPendingCreatorApplicationsResponse,
    QueryGetModelsByRoundRequest, QueryGetModelsByRoundResponse,
    QueryGetTaskStakeRequest, QueryGetTaskStakeResponse,
    QueryGetValidationTaskRequest, QueryGetValidationTaskResponse,
)
from neurionpy.fusion.interface import FusionQuery


class FusionRestClient(FusionQuery):
    """Fusion REST client implementing all query endpoints."""
    API_URL = "/neurion/fusion"

    def __init__(self, rest_api: RestClient):
        """
        Initialize the Fusion REST client.

        :param rest_api: RestClient instance for making HTTP GET requests.
        """
        self._rest_api = rest_api

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Query module parameters.
        GET /neurion/fusion/params
        """
        response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(response, QueryParamsResponse())

    def GetTask(self, request: QueryGetTaskRequest) -> QueryGetTaskResponse:
        """
        Query a task by its ID.
        GET /neurion/fusion/get_task/{task_id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_task/{request.task_id}")
        return Parse(response, QueryGetTaskResponse())

    def GetTaskReward(self, request: QueryGetTaskRewardRequest) -> QueryGetTaskRewardResponse:
        """
        Query task reward for a given task and user.
        GET /neurion/fusion/get_task_reward/{task_id}/{user}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_task_reward/{request.task_id}/{request.user}"
        )
        return Parse(response, QueryGetTaskRewardResponse())

    def GetCreatorApplicants(
        self, request: QueryGetCreatorApplicantsRequest
    ) -> QueryGetCreatorApplicantsResponse:
        """
        Query creator applicants for a given creator.
        GET /neurion/fusion/get_creator_applicants/{creator}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_creator_applicants/{request.creator}"
        )
        return Parse(response, QueryGetCreatorApplicantsResponse())

    def GetPendingCreatorApplications(
        self, request: QueryGetPendingCreatorApplicationsRequest
    ) -> QueryGetPendingCreatorApplicationsResponse:
        """
        Query pending creator applications.
        GET /neurion/fusion/get_pending_creator_applications
        """
        response = self._rest_api.get(f"{self.API_URL}/get_pending_creator_applications")
        return Parse(response, QueryGetPendingCreatorApplicationsResponse())

    def GetModelsByRound(self, request: QueryGetModelsByRoundRequest) -> QueryGetModelsByRoundResponse:
        """
        Query proposed models for a given task and round.
        GET /neurion/fusion/get_models_by_round/{task_id}/{round}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_models_by_round/{request.task_id}/{request.round}"
        )
        return Parse(response, QueryGetModelsByRoundResponse())

    def GetTaskStake(self, request: QueryGetTaskStakeRequest) -> QueryGetTaskStakeResponse:
        """
        Query task stake for a given task and user.
        GET /neurion/fusion/get_task_stake/{task_id}/{user}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_task_stake/{request.task_id}/{request.user}"
        )
        return Parse(response, QueryGetTaskStakeResponse())

    def GetValidationTask(self, request: QueryGetValidationTaskRequest) -> QueryGetValidationTaskResponse:
        """
        Query a validation task by its ID.
        GET /neurion/fusion/get_validation_task/{id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_validation_task/{request.id}")
        return Parse(response, QueryGetValidationTaskResponse())