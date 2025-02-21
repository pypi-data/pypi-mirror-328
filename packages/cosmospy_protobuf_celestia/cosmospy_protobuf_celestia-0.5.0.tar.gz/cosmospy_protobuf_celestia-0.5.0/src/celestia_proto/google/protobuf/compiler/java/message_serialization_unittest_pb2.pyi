from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessageWithManyExtensionRanges(_message.Message):
    __slots__ = ("foo", "bar", "baz")
    Extensions: _python_message._ExtensionDict
    FOO_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    BAZ_FIELD_NUMBER: _ClassVar[int]
    foo: int
    bar: int
    baz: int
    def __init__(self, foo: _Optional[int] = ..., bar: _Optional[int] = ..., baz: _Optional[int] = ...) -> None: ...
