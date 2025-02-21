from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestAny(_message.Message):
    __slots__ = ("int32_value", "any_value", "repeated_any_value", "text")
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANY_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ANY_VALUE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    int32_value: int
    any_value: _any_pb2.Any
    repeated_any_value: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    text: str
    def __init__(self, int32_value: _Optional[int] = ..., any_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., repeated_any_value: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., text: _Optional[str] = ...) -> None: ...
