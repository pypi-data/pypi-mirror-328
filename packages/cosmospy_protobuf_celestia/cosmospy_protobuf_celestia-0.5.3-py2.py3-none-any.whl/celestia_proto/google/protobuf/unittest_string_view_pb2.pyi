from google.protobuf import cpp_features_pb2 as _cpp_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
SINGULAR_STRING_VIEW_EXTENSION_FIELD_NUMBER: _ClassVar[int]
singular_string_view_extension: _descriptor.FieldDescriptor
SINGULAR_BYTES_VIEW_EXTENSION_FIELD_NUMBER: _ClassVar[int]
singular_bytes_view_extension: _descriptor.FieldDescriptor
REPEATED_STRING_VIEW_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_string_view_extension: _descriptor.FieldDescriptor
REPEATED_BYTES_VIEW_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_bytes_view_extension: _descriptor.FieldDescriptor

class TestStringView(_message.Message):
    __slots__ = ("singular_string", "singular_bytes", "repeated_string", "repeated_bytes")
    SINGULAR_STRING_FIELD_NUMBER: _ClassVar[int]
    SINGULAR_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    singular_string: str
    singular_bytes: bytes
    repeated_string: _containers.RepeatedScalarFieldContainer[str]
    repeated_bytes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, singular_string: _Optional[str] = ..., singular_bytes: _Optional[bytes] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ...) -> None: ...

class TestStringViewExtension(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...
