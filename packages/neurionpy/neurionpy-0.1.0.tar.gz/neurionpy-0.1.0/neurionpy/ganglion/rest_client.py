from google.protobuf.json_format import Parse

from neurionpy.common.rest_client import RestClient
from neurionpy.protos.neurion.ganglion.query_pb2 import (
    QueryParamsRequest, QueryParamsResponse,
    QueryIonByIonAddressRequest, QueryIonByIonAddressResponse,
    QueryIonByCreatorRequest, QueryIonByCreatorResponse,
    QueryGetValidatorsRequest, QueryGetValidatorsResponse,
    QueryIonsByInputSchemaHashRequest, QueryIonsByInputSchemaHashResponse,
    QueryGetPathwayRequest, QueryGetPathwayResponse,
    QueryListPathwaysRequest, QueryListPathwaysResponse,
    QueryListIonsByAddressesRequest, QueryListIonsByAddressesResponse,
    QueryUserPathwayStakeRequest, QueryUserPathwayStakeResponse,
    QueryGetUserRewardRequest, QueryGetUserRewardResponse,
    QueryGetProtocolFeeRequest, QueryGetProtocolFeeResponse,
    QueryPathwaysUsingIonRequest, QueryPathwaysUsingIonResponse,
    QueryIonsByReportsRequest, QueryIonsByReportsResponse,
    QueryListAllPathwaysRequest, QueryListAllPathwaysResponse,
    QueryGetRewardRequest, QueryGetRewardResponse,
    QueryGetStakeRequest, QueryGetStakeResponse,
    QueryGetIonRequest, QueryGetIonResponse,
    QueryGetPathwayUnstakeInitiatedUsersRequest, QueryGetPathwayUnstakeInitiatedUsersResponse,
    QueryGetStakerRewardRequest, QueryGetStakerRewardResponse,
)
from neurionpy.ganglion.interface import GanglionQuery


class GanglionRestClient(GanglionQuery):
    """Ganglion REST client implementing all query endpoints."""
    API_URL = "/neurion/ganglion"

    def __init__(self, rest_api: RestClient):
        """
        Initialize the Ganglion REST client.

        :param rest_api: RestClient instance for making HTTP GET requests.
        """
        self._rest_api = rest_api

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Query module parameters.
        GET /neurion/ganglion/params
        """
        response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(response, QueryParamsResponse())

    def IonByIonAddress(self, request: QueryIonByIonAddressRequest) -> QueryIonByIonAddressResponse:
        """
        Query an Ion by its ion_address.
        GET /neurion/ganglion/ion_by_ion_address/{ion_address}
        """
        response = self._rest_api.get(f"{self.API_URL}/ion_by_ion_address/{request.ion_address}")
        return Parse(response, QueryIonByIonAddressResponse())

    def IonByCreator(self, request: QueryIonByCreatorRequest) -> QueryIonByCreatorResponse:
        """
        Query an Ion by its creator.
        GET /neurion/ganglion/ion_by_creator/{creator}
        """
        response = self._rest_api.get(f"{self.API_URL}/ion_by_creator/{request.creator}")
        return Parse(response, QueryIonByCreatorResponse())

    def GetValidators(self, request: QueryGetValidatorsRequest) -> QueryGetValidatorsResponse:
        """
        Query the list of validators.
        GET /neurion/ganglion/get_validators
        """
        response = self._rest_api.get(f"{self.API_URL}/get_validators")
        return Parse(response, QueryGetValidatorsResponse())

    def IonsByInputSchemaHash(self, request: QueryIonsByInputSchemaHashRequest) -> QueryIonsByInputSchemaHashResponse:
        """
        Query Ions by input_schema_hash with pagination.
        GET /neurion/ganglion/ions_by_input_schema_hash/{input_schema_hash}/{offset}/{limit}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/ions_by_input_schema_hash/{request.input_schema_hash}/{request.offset}/{request.limit}"
        )
        return Parse(response, QueryIonsByInputSchemaHashResponse())

    def GetPathway(self, request: QueryGetPathwayRequest) -> QueryGetPathwayResponse:
        """
        Query a pathway by its id.
        GET /neurion/ganglion/get_pathway/{id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_pathway/{request.id}")
        return Parse(response, QueryGetPathwayResponse())

    def ListPathways(self, request: QueryListPathwaysRequest) -> QueryListPathwaysResponse:
        """
        List pathways for a creator with pagination.
        GET /neurion/ganglion/list_pathways/{creator}/{offset}/{limit}
        """
        response = self._rest_api.get(
            f"{self.API_URL}/list_pathways/{request.creator}/{request.offset}/{request.limit}"
        )
        return Parse(response, QueryListPathwaysResponse())

    def ListIonsByAddresses(self, request: QueryListIonsByAddressesRequest) -> QueryListIonsByAddressesResponse:
        """
        List Ions by a list of ion addresses.
        GET /neurion/ganglion/list_ions_by_addresses/{ion_addresses}
        """
        # Join multiple addresses with commas
        addresses = ",".join(request.ion_addresses)
        response = self._rest_api.get(f"{self.API_URL}/list_ions_by_addresses/{addresses}")
        return Parse(response, QueryListIonsByAddressesResponse())

    def UserPathwayStake(self, request: QueryUserPathwayStakeRequest) -> QueryUserPathwayStakeResponse:
        """
        Query pathway stake for a given pathway and user.
        GET /neurion/ganglion/user_pathway_stake/{id}/{user}
        """
        response = self._rest_api.get(f"{self.API_URL}/user_pathway_stake/{request.id}/{request.user}")
        return Parse(response, QueryUserPathwayStakeResponse())

    def GetUserReward(self, request: QueryGetUserRewardRequest) -> QueryGetUserRewardResponse:
        """
        Query user reward.
        GET /neurion/ganglion/get_user_reward/{user}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_user_reward/{request.user}")
        return Parse(response, QueryGetUserRewardResponse())

    def GetProtocolFee(self, request: QueryGetProtocolFeeRequest) -> QueryGetProtocolFeeResponse:
        """
        Query the protocol fee.
        GET /neurion/ganglion/get_protocol_fee
        """
        response = self._rest_api.get(f"{self.API_URL}/get_protocol_fee")
        return Parse(response, QueryGetProtocolFeeResponse())

    def PathwaysUsingIon(self, request: QueryPathwaysUsingIonRequest) -> QueryPathwaysUsingIonResponse:
        """
        Query pathways using a given ion.
        GET /neurion/ganglion/pathways_using_ion/{ion_address}
        """
        response = self._rest_api.get(f"{self.API_URL}/pathways_using_ion/{request.ion_address}")
        return Parse(response, QueryPathwaysUsingIonResponse())

    def IonsByReports(self, request: QueryIonsByReportsRequest) -> QueryIonsByReportsResponse:
        """
        Query ions by reports with pagination.
        GET /neurion/ganglion/ions_by_reports/{offset}/{limit}
        """
        response = self._rest_api.get(f"{self.API_URL}/ions_by_reports/{request.offset}/{request.limit}")
        return Parse(response, QueryIonsByReportsResponse())

    def ListAllPathways(self, request: QueryListAllPathwaysRequest) -> QueryListAllPathwaysResponse:
        """
        List all pathways with pagination.
        GET /neurion/ganglion/list_all_pathways/{offset}/{limit}
        """
        response = self._rest_api.get(f"{self.API_URL}/list_all_pathways/{request.offset}/{request.limit}")
        return Parse(response, QueryListAllPathwaysResponse())

    def GetReward(self, request: QueryGetRewardRequest) -> QueryGetRewardResponse:
        """
        Query reward for a given user.
        GET /neurion/ganglion/get_reward/{user}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_reward/{request.user}")
        return Parse(response, QueryGetRewardResponse())

    def GetStake(self, request: QueryGetStakeRequest) -> QueryGetStakeResponse:
        """
        Query stake for a given user.
        GET /neurion/ganglion/get_stake/{user}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_stake/{request.user}")
        return Parse(response, QueryGetStakeResponse())

    def GetIon(self, request: QueryGetIonRequest) -> QueryGetIonResponse:
        """
        Query an Ion by its id.
        GET /neurion/ganglion/get_ion/{id}
        """
        response = self._rest_api.get(f"{self.API_URL}/get_ion/{request.id}")
        return Parse(response, QueryGetIonResponse())

    def GetPathwayUnstakeInitiatedUsers(
        self, request: QueryGetPathwayUnstakeInitiatedUsersRequest
    ) -> QueryGetPathwayUnstakeInitiatedUsersResponse:
        """
        Query pathway unstake initiated users.
        GET /neurion/ganglion/get_pathway_unstake_initiated_users
        """
        response = self._rest_api.get(f"{self.API_URL}/get_pathway_unstake_initiated_users")
        return Parse(response, QueryGetPathwayUnstakeInitiatedUsersResponse())

    def GetStakerReward(self, request: QueryGetStakerRewardRequest) -> QueryGetStakerRewardResponse:
        """
        Query staker reward.
        GET /neurion/ganglion/get_staker_reward
        """
        response = self._rest_api.get(f"{self.API_URL}/get_staker_reward")
        return Parse(response, QueryGetStakerRewardResponse())