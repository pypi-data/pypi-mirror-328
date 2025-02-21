from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Proto3FileExtensions(_message.Message):
    __slots__ = ()
    SINGULAR_INT_FIELD_NUMBER: _ClassVar[int]
    singular_int: _descriptor.FieldDescriptor
    REPEATED_INT_FIELD_NUMBER: _ClassVar[int]
    repeated_int: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...
