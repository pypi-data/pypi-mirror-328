from google.protobuf.json_format import Parse

from neurionpy.common.rest_client import RestClient
from neurionpy.protos.neurion.crucible.query_pb2 import (
    QueryParamsRequest, QueryParamsResponse,
    QueryGetCreatorsRequest, QueryGetCreatorsResponse,
    QueryGetCreatorApplicationsRequest, QueryGetCreatorApplicationsResponse,
    QueryGetTaskRequest, QueryGetTaskResponse,
    QueryListAllTasksRequest, QueryListAllTasksResponse,
    QueryListTasksByStatusRequest, QueryListTasksByStatusResponse,
    QueryGetSubmissionRequest, QueryGetSubmissionResponse,
    QueryGetSubmissionByTaskCreatorRequest, QueryGetSubmissionByTaskCreatorResponse,
    QueryGetSubmissionByTaskRequest, QueryGetSubmissionByTaskResponse,
    QueryGetEncryptedProofOfOwnershipRequest, QueryGetEncryptedProofOfOwnershipResponse,
    QueryGetPlagiarismReportRequest, QueryGetPlagiarismReportResponse,
    QueryGetTaskRewardRequest, QueryGetTaskRewardResponse,
    QueryGetPendingCreatorApplicationsRequest, QueryGetPendingCreatorApplicationsResponse,
    QueryGetTaskStakeRequest, QueryGetTaskStakeResponse,
    QueryGetUnscoredSubmissionsByTaskRequest, QueryGetUnscoredSubmissionsByTaskResponse,
)
from neurionpy.crucible.interface import CrucibleQuery


class CrucibleRestClient(CrucibleQuery):
    """Crucible REST client implementing all query endpoints."""
    API_URL = "/neurion/crucible"

    def __init__(self, rest_api: RestClient):
        """
        Initialize the Crucible REST client.

        :param rest_api: RestClient instance for making HTTP requests.
        """
        self._rest_api = rest_api

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Query module parameters.
        GET /neurion/crucible/params
        """
        response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(response, QueryParamsResponse())

    def GetCreators(self, request: QueryGetCreatorsRequest) -> QueryGetCreatorsResponse:
        """
        Query a list of creators.
        GET /neurion/crucible/get_creators
        """
        response = self._rest_api.get(f"{self.API_URL}/get_creators")
        return Parse(response, QueryGetCreatorsResponse())

    def GetCreatorApplications(
            self, request: QueryGetCreatorApplicationsRequest
    ) -> QueryGetCreatorApplicationsResponse:
        """
        Query creator applications for a given creator.
        GET /neurion/crucible/get_creator_applications/{creator}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_creator_applications/{request.creator}"
        )
        return Parse(response, QueryGetCreatorApplicationsResponse())

    def GetTask(self, request: QueryGetTaskRequest) -> QueryGetTaskResponse:
        """
        Query a task by its ID.
        GET /neurion/crucible/get_task/{id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_task/{request.id}")
        return Parse(response, QueryGetTaskResponse())

    def ListAllTasks(self, request: QueryListAllTasksRequest) -> QueryListAllTasksResponse:
        """
        List all tasks with pagination.
        GET /neurion/crucible/list_all_tasks/{offset}/{limit}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/list_all_tasks/{request.offset}/{request.limit}"
        )
        return Parse(response, QueryListAllTasksResponse())

    def ListTasksByStatus(self, request: QueryListTasksByStatusRequest) -> QueryListTasksByStatusResponse:
        """
        List tasks by status with pagination.
        GET /neurion/crucible/list_tasks_by_status/{status}/{offset}/{limit}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/list_tasks_by_status/{request.status}/{request.offset}/{request.limit}"
        )
        return Parse(response, QueryListTasksByStatusResponse())

    def GetSubmission(self, request: QueryGetSubmissionRequest) -> QueryGetSubmissionResponse:
        """
        Query a submission by its ID.
        GET /neurion/crucible/get_submission/{id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_submission/{request.id}")
        return Parse(response, QueryGetSubmissionResponse())

    def GetSubmissionByTaskCreator(
            self, request: QueryGetSubmissionByTaskCreatorRequest
    ) -> QueryGetSubmissionByTaskCreatorResponse:
        """
        Query submissions for a given task and creator.
        GET /neurion/crucible/get_submission_by_task_creator/{task_id}/{creator}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_submission_by_task_creator/{request.task_id}/{request.creator}"
        )
        return Parse(response, QueryGetSubmissionByTaskCreatorResponse())

    def GetSubmissionByTask(
            self, request: QueryGetSubmissionByTaskRequest
    ) -> QueryGetSubmissionByTaskResponse:
        """
        Query submissions for a given task.
        GET /neurion/crucible/get_submission_by_task/{task_id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_submission_by_task/{request.task_id}")
        return Parse(response, QueryGetSubmissionByTaskResponse())

    def GetEncryptedProofOfOwnership(
            self, request: QueryGetEncryptedProofOfOwnershipRequest
    ) -> QueryGetEncryptedProofOfOwnershipResponse:
        """
        Get encrypted proof of ownership.
        GET /neurion/crucible/get_encrypted_proof_of_ownership/{key}/{plaintext}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_encrypted_proof_of_ownership/{request.key}/{request.plaintext}"
        )
        return Parse(response, QueryGetEncryptedProofOfOwnershipResponse())

    def GetPlagiarismReport(
            self, request: QueryGetPlagiarismReportRequest
    ) -> QueryGetPlagiarismReportResponse:
        """
        Query a plagiarism report by report ID.
        GET /neurion/crucible/get_plagiarism_report/{report_id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_plagiarism_report/{request.report_id}")
        return Parse(response, QueryGetPlagiarismReportResponse())

    def GetTaskReward(self, request: QueryGetTaskRewardRequest) -> QueryGetTaskRewardResponse:
        """
        Query task reward for a given task and user.
        GET /neurion/crucible/get_task_reward/{task_id}/{user}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_task_reward/{request.task_id}/{request.user}"
        )
        return Parse(response, QueryGetTaskRewardResponse())

    def GetPendingCreatorApplications(
            self, request: QueryGetPendingCreatorApplicationsRequest
    ) -> QueryGetPendingCreatorApplicationsResponse:
        """
        Query pending creator applications.
        GET /neurion/crucible/get_pending_creator_applications
        """
        response = self._rest_api.get(f"{self.API_URL}/get_pending_creator_applications")
        return Parse(response, QueryGetPendingCreatorApplicationsResponse())

    def GetTaskStake(self, request: QueryGetTaskStakeRequest) -> QueryGetTaskStakeResponse:
        """
        Query task stake for a given task and user.
        GET /neurion/crucible/get_task_stake/{task_id}/{user}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_task_stake/{request.task_id}/{request.user}"
        )
        return Parse(response, QueryGetTaskStakeResponse())

    def GetUnscoredSubmissionsByTask(
            self, request: QueryGetUnscoredSubmissionsByTaskRequest
    ) -> QueryGetUnscoredSubmissionsByTaskResponse:
        """
        Query unscored submissions by task.
        GET /neurion/crucible/get_unscored_submissions_by_task/{task_id}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/get_unscored_submissions_by_task/{request.task_id}"
        )
        return Parse(response, QueryGetUnscoredSubmissionsByTaskResponse())