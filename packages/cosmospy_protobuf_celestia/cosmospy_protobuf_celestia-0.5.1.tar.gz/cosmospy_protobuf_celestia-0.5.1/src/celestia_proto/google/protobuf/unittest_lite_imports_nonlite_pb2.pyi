from google.protobuf import unittest_pb2 as _unittest_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestLiteImportsNonlite(_message.Message):
    __slots__ = ("message", "message_with_required")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_WITH_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    message: _unittest_pb2.TestAllTypes
    message_with_required: _unittest_pb2.TestRequired
    def __init__(self, message: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ..., message_with_required: _Optional[_Union[_unittest_pb2.TestRequired, _Mapping]] = ...) -> None: ...
