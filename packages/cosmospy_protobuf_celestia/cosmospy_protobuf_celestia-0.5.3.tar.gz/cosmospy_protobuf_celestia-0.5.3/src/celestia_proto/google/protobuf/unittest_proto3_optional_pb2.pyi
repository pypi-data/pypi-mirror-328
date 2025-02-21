from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestProto3Optional(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optional_cord", "optional_nested_message", "lazy_nested_message", "optional_nested_enum", "singular_int32", "singular_int64")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TestProto3Optional.NestedEnum]
        FOO: _ClassVar[TestProto3Optional.NestedEnum]
        BAR: _ClassVar[TestProto3Optional.NestedEnum]
        BAZ: _ClassVar[TestProto3Optional.NestedEnum]
        NEG: _ClassVar[TestProto3Optional.NestedEnum]
    UNSPECIFIED: TestProto3Optional.NestedEnum
    FOO: TestProto3Optional.NestedEnum
    BAR: TestProto3Optional.NestedEnum
    BAZ: TestProto3Optional.NestedEnum
    NEG: TestProto3Optional.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("bb",)
        BB_FIELD_NUMBER: _ClassVar[int]
        bb: int
        def __init__(self, bb: _Optional[int] = ...) -> None: ...
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SINT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIXED32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIXED64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BOOL_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAZY_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    SINGULAR_INT32_FIELD_NUMBER: _ClassVar[int]
    SINGULAR_INT64_FIELD_NUMBER: _ClassVar[int]
    optional_int32: int
    optional_int64: int
    optional_uint32: int
    optional_uint64: int
    optional_sint32: int
    optional_sint64: int
    optional_fixed32: int
    optional_fixed64: int
    optional_sfixed32: int
    optional_sfixed64: int
    optional_float: float
    optional_double: float
    optional_bool: bool
    optional_string: str
    optional_bytes: bytes
    optional_cord: str
    optional_nested_message: TestProto3Optional.NestedMessage
    lazy_nested_message: TestProto3Optional.NestedMessage
    optional_nested_enum: TestProto3Optional.NestedEnum
    singular_int32: int
    singular_int64: int
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_cord: _Optional[str] = ..., optional_nested_message: _Optional[_Union[TestProto3Optional.NestedMessage, _Mapping]] = ..., lazy_nested_message: _Optional[_Union[TestProto3Optional.NestedMessage, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestProto3Optional.NestedEnum, str]] = ..., singular_int32: _Optional[int] = ..., singular_int64: _Optional[int] = ...) -> None: ...

class TestProto3OptionalMessage(_message.Message):
    __slots__ = ("nested_message", "optional_nested_message")
    class NestedMessage(_message.Message):
        __slots__ = ("s",)
        S_FIELD_NUMBER: _ClassVar[int]
        s: str
        def __init__(self, s: _Optional[str] = ...) -> None: ...
    NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    nested_message: TestProto3OptionalMessage.NestedMessage
    optional_nested_message: TestProto3OptionalMessage.NestedMessage
    def __init__(self, nested_message: _Optional[_Union[TestProto3OptionalMessage.NestedMessage, _Mapping]] = ..., optional_nested_message: _Optional[_Union[TestProto3OptionalMessage.NestedMessage, _Mapping]] = ...) -> None: ...

class Proto3OptionalExtensions(_message.Message):
    __slots__ = ()
    EXT_NO_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    ext_no_optional: _descriptor.FieldDescriptor
    EXT_WITH_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    ext_with_optional: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...
