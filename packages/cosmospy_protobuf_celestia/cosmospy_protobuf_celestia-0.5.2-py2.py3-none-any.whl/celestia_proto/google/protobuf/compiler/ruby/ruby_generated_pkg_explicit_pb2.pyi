from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Four(_message.Message):
    __slots__ = ("a_string",)
    A_STRING_FIELD_NUMBER: _ClassVar[int]
    a_string: str
    def __init__(self, a_string: _Optional[str] = ...) -> None: ...
