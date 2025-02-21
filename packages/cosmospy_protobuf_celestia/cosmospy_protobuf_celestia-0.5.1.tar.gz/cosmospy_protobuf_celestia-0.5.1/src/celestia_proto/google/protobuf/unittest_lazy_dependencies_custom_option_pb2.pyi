from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import unittest_lazy_dependencies_enum_pb2 as _unittest_lazy_dependencies_enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
LAZY_ENUM_OPTION_FIELD_NUMBER: _ClassVar[int]
lazy_enum_option: _descriptor.FieldDescriptor

class LazyMessage(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...
