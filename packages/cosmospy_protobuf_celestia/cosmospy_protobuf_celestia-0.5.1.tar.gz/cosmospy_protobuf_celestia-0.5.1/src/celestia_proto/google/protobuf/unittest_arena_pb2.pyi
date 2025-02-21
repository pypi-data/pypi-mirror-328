from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NestedMessage(_message.Message):
    __slots__ = ("d",)
    D_FIELD_NUMBER: _ClassVar[int]
    d: int
    def __init__(self, d: _Optional[int] = ...) -> None: ...

class ArenaMessage(_message.Message):
    __slots__ = ("repeated_nested_message",)
    REPEATED_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[NestedMessage]
    def __init__(self, repeated_nested_message: _Optional[_Iterable[_Union[NestedMessage, _Mapping]]] = ...) -> None: ...
