from google.protobuf.json_format import Parse

from neurionpy.common.rest_client import RestClient
from neurionpy.protos.neurion.sanctum.query_pb2 import (
    QueryParamsRequest, QueryParamsResponse,
    QueryGetAvailableDatasetsRequest, QueryGetAvailableDatasetsResponse,
    QueryGetApprovedUsageRequestsRequest, QueryGetApprovedUsageRequestsResponse,
    QueryGetRewardRequest, QueryGetRewardResponse,
    QueryGetStakeRequest, QueryGetStakeResponse,
    QueryGetPendingDatasetsRequest, QueryGetPendingDatasetsResponse,
    QueryGetPendingUsageRequestsRequest, QueryGetPendingUsageRequestsResponse,
    QueryGetDatasetRequest, QueryGetDatasetResponse,
    QueryGetUsageRequestRequest, QueryGetUsageRequestResponse,
)
from neurionpy.sanctum.interface import SanctumQuery


class SanctumRestClient(SanctumQuery):
    """Sanctum REST client implementing all query endpoints."""
    API_URL = "/neurion/sanctum"

    def __init__(self, rest_api: RestClient):
        """
        Create Sanctum REST client.

        :param rest_api: RestClient instance for making HTTP requests.
        """
        self._rest_api = rest_api

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Query the parameters of the Sanctum module.
        GET /neurion/sanctum/params
        """
        response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(response, QueryParamsResponse())

    def GetAvailableDatasets(self, request: QueryGetAvailableDatasetsRequest) -> QueryGetAvailableDatasetsResponse:
        """
        Query a list of available datasets.
        GET /neurion/sanctum/get_available_datasets?offset={offset}&limit={limit}
        """
        params = {"offset": request.offset, "limit": request.limit}
        response = self._rest_api.get(f"{self.API_URL}/get_available_datasets/{request.offset}/{request.limit}")
        return Parse(response, QueryGetAvailableDatasetsResponse())

    def GetApprovedUsageRequests(self,
                                 request: QueryGetApprovedUsageRequestsRequest) -> QueryGetApprovedUsageRequestsResponse:
        """
        Query a list of approved usage requests.
        GET /neurion/sanctum/get_approved_usage_requests
        """
        response = self._rest_api.get(f"{self.API_URL}/get_approved_usage_requests")
        return Parse(response, QueryGetApprovedUsageRequestsResponse())

    def GetReward(self, request: QueryGetRewardRequest) -> QueryGetRewardResponse:
        """
        Query reward for a given user.
        GET /neurion/sanctum/get_reward/{user}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_reward/{request.user}")
        return Parse(response, QueryGetRewardResponse())

    def GetStake(self, request: QueryGetStakeRequest) -> QueryGetStakeResponse:
        """
        Query stake for a given user.
        GET /neurion/sanctum/get_stake/{user}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_stake/{request.user}")
        return Parse(response, QueryGetStakeResponse())

    def GetPendingDatasets(self, request: QueryGetPendingDatasetsRequest) -> QueryGetPendingDatasetsResponse:
        """
        Query a list of pending datasets.
        GET /neurion/sanctum/get_pending_datasets
        """
        response = self._rest_api.get(f"{self.API_URL}/get_pending_datasets")
        return Parse(response, QueryGetPendingDatasetsResponse())

    def GetPendingUsageRequests(self,
                                request: QueryGetPendingUsageRequestsRequest) -> QueryGetPendingUsageRequestsResponse:
        """
        Query a list of pending usage requests for a given user.
        GET /neurion/sanctum/get_pending_usage_requests/{user}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_pending_usage_requests/{request.user}")
        return Parse(response, QueryGetPendingUsageRequestsResponse())

    def GetDataset(self, request: QueryGetDatasetRequest) -> QueryGetDatasetResponse:
        """
        Query a dataset by its ID.
        GET /neurion/sanctum/get_dataset/{id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_dataset/{request.id}")
        return Parse(response, QueryGetDatasetResponse())

    def GetUsageRequest(self, request: QueryGetUsageRequestRequest) -> QueryGetUsageRequestResponse:
        """
        Query a usage request by its ID.
        GET /neurion/sanctum/get_usage_request/{id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_usage_request/{request.id}")
        return Parse(response, QueryGetUsageRequestResponse())