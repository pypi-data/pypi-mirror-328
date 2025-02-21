from google.protobuf import unittest_pb2 as _unittest_pb2
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestOptimizedForSize(_message.Message):
    __slots__ = ("i", "msg", "integer_field", "string_field")
    Extensions: _python_message._ExtensionDict
    TEST_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    test_extension: _descriptor.FieldDescriptor
    TEST_EXTENSION2_FIELD_NUMBER: _ClassVar[int]
    test_extension2: _descriptor.FieldDescriptor
    I_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    i: int
    msg: _unittest_pb2.ForeignMessage
    integer_field: int
    string_field: str
    def __init__(self, i: _Optional[int] = ..., msg: _Optional[_Union[_unittest_pb2.ForeignMessage, _Mapping]] = ..., integer_field: _Optional[int] = ..., string_field: _Optional[str] = ...) -> None: ...

class TestRequiredOptimizedForSize(_message.Message):
    __slots__ = ("x",)
    X_FIELD_NUMBER: _ClassVar[int]
    x: int
    def __init__(self, x: _Optional[int] = ...) -> None: ...

class TestOptionalOptimizedForSize(_message.Message):
    __slots__ = ("o",)
    O_FIELD_NUMBER: _ClassVar[int]
    o: TestRequiredOptimizedForSize
    def __init__(self, o: _Optional[_Union[TestRequiredOptimizedForSize, _Mapping]] = ...) -> None: ...
