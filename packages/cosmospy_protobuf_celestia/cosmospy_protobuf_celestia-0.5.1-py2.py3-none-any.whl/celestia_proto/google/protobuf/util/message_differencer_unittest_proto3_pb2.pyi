from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestNoPresenceField(_message.Message):
    __slots__ = ("no_presence_bool", "no_presence_nested", "no_presence_repeated_nested", "no_presence_string", "no_presence_bool2", "no_presence_bool3")
    NO_PRESENCE_BOOL_FIELD_NUMBER: _ClassVar[int]
    NO_PRESENCE_NESTED_FIELD_NUMBER: _ClassVar[int]
    NO_PRESENCE_REPEATED_NESTED_FIELD_NUMBER: _ClassVar[int]
    NO_PRESENCE_STRING_FIELD_NUMBER: _ClassVar[int]
    NO_PRESENCE_BOOL2_FIELD_NUMBER: _ClassVar[int]
    NO_PRESENCE_BOOL3_FIELD_NUMBER: _ClassVar[int]
    no_presence_bool: bool
    no_presence_nested: TestNoPresenceField
    no_presence_repeated_nested: _containers.RepeatedCompositeFieldContainer[TestNoPresenceField]
    no_presence_string: str
    no_presence_bool2: bool
    no_presence_bool3: bool
    def __init__(self, no_presence_bool: bool = ..., no_presence_nested: _Optional[_Union[TestNoPresenceField, _Mapping]] = ..., no_presence_repeated_nested: _Optional[_Iterable[_Union[TestNoPresenceField, _Mapping]]] = ..., no_presence_string: _Optional[str] = ..., no_presence_bool2: bool = ..., no_presence_bool3: bool = ...) -> None: ...
