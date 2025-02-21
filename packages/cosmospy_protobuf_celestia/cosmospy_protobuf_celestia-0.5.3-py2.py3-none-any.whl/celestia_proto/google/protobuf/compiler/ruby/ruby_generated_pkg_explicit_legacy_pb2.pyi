from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Four(_message.Message):
    __slots__ = ("another_string",)
    ANOTHER_STRING_FIELD_NUMBER: _ClassVar[int]
    another_string: str
    def __init__(self, another_string: _Optional[str] = ...) -> None: ...
