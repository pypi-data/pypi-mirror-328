from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOO: _ClassVar[TestEnum]
FOO: TestEnum
TEST_EXTENSION_FIELD_NUMBER: _ClassVar[int]
test_extension: _descriptor.FieldDescriptor

class TestMessage(_message.Message):
    __slots__ = ("a",)
    Extensions: _python_message._ExtensionDict
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...
