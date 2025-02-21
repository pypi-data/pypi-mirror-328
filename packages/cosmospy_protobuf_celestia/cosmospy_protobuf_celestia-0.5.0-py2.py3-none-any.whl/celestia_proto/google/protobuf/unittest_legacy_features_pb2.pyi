from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEditionsMessage(_message.Message):
    __slots__ = ("required_field", "delimited_field")
    REQUIRED_FIELD_FIELD_NUMBER: _ClassVar[int]
    DELIMITED_FIELD_FIELD_NUMBER: _ClassVar[int]
    required_field: int
    delimited_field: TestEditionsMessage
    def __init__(self, required_field: _Optional[int] = ..., delimited_field: _Optional[_Union[TestEditionsMessage, _Mapping]] = ...) -> None: ...
