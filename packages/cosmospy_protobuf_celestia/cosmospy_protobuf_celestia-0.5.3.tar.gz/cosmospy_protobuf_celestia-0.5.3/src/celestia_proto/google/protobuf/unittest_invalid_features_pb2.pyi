from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
TEST_INVALID_FIELD_NUMBER: _ClassVar[int]
test_invalid: _descriptor.FieldDescriptor

class TestInvalidFeatures(_message.Message):
    __slots__ = ("repeated_feature",)
    REPEATED_FEATURE_FIELD_NUMBER: _ClassVar[int]
    repeated_feature: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, repeated_feature: _Optional[_Iterable[int]] = ...) -> None: ...
