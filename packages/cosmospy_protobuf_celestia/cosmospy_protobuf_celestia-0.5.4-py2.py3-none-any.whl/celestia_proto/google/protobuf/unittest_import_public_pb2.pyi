from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PublicImportMessage(_message.Message):
    __slots__ = ("e",)
    E_FIELD_NUMBER: _ClassVar[int]
    e: int
    def __init__(self, e: _Optional[int] = ...) -> None: ...
