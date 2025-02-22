from amino import amino_pb2 as _amino_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from neurion.fusion import params_pb2 as _params_pb2
from neurion.fusion import task_pb2 as _task_pb2
from neurion.fusion import creator_application_pb2 as _creator_application_pb2
from neurion.fusion import proposed_model_pb2 as _proposed_model_pb2
from neurion.fusion import validation_task_pb2 as _validation_task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ("params",)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params
    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryGetTaskRequest(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class QueryGetTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: _task_pb2.Task
    def __init__(self, task: _Optional[_Union[_task_pb2.Task, _Mapping]] = ...) -> None: ...

class QueryGetTaskRewardRequest(_message.Message):
    __slots__ = ("task_id", "user")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    user: str
    def __init__(self, task_id: _Optional[int] = ..., user: _Optional[str] = ...) -> None: ...

class QueryGetTaskRewardResponse(_message.Message):
    __slots__ = ("reward",)
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: int
    def __init__(self, reward: _Optional[int] = ...) -> None: ...

class QueryGetCreatorApplicantsRequest(_message.Message):
    __slots__ = ("creator",)
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    creator: str
    def __init__(self, creator: _Optional[str] = ...) -> None: ...

class QueryGetCreatorApplicantsResponse(_message.Message):
    __slots__ = ("applicants",)
    APPLICANTS_FIELD_NUMBER: _ClassVar[int]
    applicants: _containers.RepeatedCompositeFieldContainer[_creator_application_pb2.CreatorApplication]
    def __init__(self, applicants: _Optional[_Iterable[_Union[_creator_application_pb2.CreatorApplication, _Mapping]]] = ...) -> None: ...

class QueryGetPendingCreatorApplicationsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryGetPendingCreatorApplicationsResponse(_message.Message):
    __slots__ = ("applicants",)
    APPLICANTS_FIELD_NUMBER: _ClassVar[int]
    applicants: _containers.RepeatedCompositeFieldContainer[_creator_application_pb2.CreatorApplication]
    def __init__(self, applicants: _Optional[_Iterable[_Union[_creator_application_pb2.CreatorApplication, _Mapping]]] = ...) -> None: ...

class QueryGetModelsByRoundRequest(_message.Message):
    __slots__ = ("task_id", "round")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    round: int
    def __init__(self, task_id: _Optional[int] = ..., round: _Optional[int] = ...) -> None: ...

class QueryGetModelsByRoundResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[_proposed_model_pb2.ProposedModel]
    def __init__(self, models: _Optional[_Iterable[_Union[_proposed_model_pb2.ProposedModel, _Mapping]]] = ...) -> None: ...

class QueryGetTaskStakeRequest(_message.Message):
    __slots__ = ("task_id", "user")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    user: str
    def __init__(self, task_id: _Optional[int] = ..., user: _Optional[str] = ...) -> None: ...

class QueryGetTaskStakeResponse(_message.Message):
    __slots__ = ("stake",)
    STAKE_FIELD_NUMBER: _ClassVar[int]
    stake: int
    def __init__(self, stake: _Optional[int] = ...) -> None: ...

class QueryGetValidationTaskRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class QueryGetValidationTaskResponse(_message.Message):
    __slots__ = ("validation_task",)
    VALIDATION_TASK_FIELD_NUMBER: _ClassVar[int]
    validation_task: _validation_task_pb2.ValidationTask
    def __init__(self, validation_task: _Optional[_Union[_validation_task_pb2.ValidationTask, _Mapping]] = ...) -> None: ...
