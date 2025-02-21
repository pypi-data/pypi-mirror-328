from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyzeChild(_message.Message):
    __slots__ = ("child_id", "child")
    CHILD_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    child_id: int
    child: AnalyzeChild
    def __init__(self, child_id: _Optional[int] = ..., child: _Optional[_Union[AnalyzeChild, _Mapping]] = ...) -> None: ...

class AnalyzeThis(_message.Message):
    __slots__ = ("id", "optional_string", "repeated_string", "optional_child", "repeated_child", "nested")
    class Nested(_message.Message):
        __slots__ = ("nexted_id", "optional_string")
        NEXTED_ID_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
        nexted_id: int
        optional_string: str
        def __init__(self, nexted_id: _Optional[int] = ..., optional_string: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CHILD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CHILD_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    id: int
    optional_string: str
    repeated_string: _containers.RepeatedScalarFieldContainer[str]
    optional_child: AnalyzeChild
    repeated_child: _containers.RepeatedCompositeFieldContainer[AnalyzeChild]
    nested: AnalyzeThis.Nested
    def __init__(self, id: _Optional[int] = ..., optional_string: _Optional[str] = ..., repeated_string: _Optional[_Iterable[str]] = ..., optional_child: _Optional[_Union[AnalyzeChild, _Mapping]] = ..., repeated_child: _Optional[_Iterable[_Union[AnalyzeChild, _Mapping]]] = ..., nested: _Optional[_Union[AnalyzeThis.Nested, _Mapping]] = ...) -> None: ...
