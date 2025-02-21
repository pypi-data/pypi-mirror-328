from google.protobuf import unittest_optimize_for_pb2 as _unittest_optimize_for_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEmbedOptimizedForSize(_message.Message):
    __slots__ = ("optional_message", "repeated_message")
    OPTIONAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    optional_message: _unittest_optimize_for_pb2.TestOptimizedForSize
    repeated_message: _containers.RepeatedCompositeFieldContainer[_unittest_optimize_for_pb2.TestOptimizedForSize]
    def __init__(self, optional_message: _Optional[_Union[_unittest_optimize_for_pb2.TestOptimizedForSize, _Mapping]] = ..., repeated_message: _Optional[_Iterable[_Union[_unittest_optimize_for_pb2.TestOptimizedForSize, _Mapping]]] = ...) -> None: ...
