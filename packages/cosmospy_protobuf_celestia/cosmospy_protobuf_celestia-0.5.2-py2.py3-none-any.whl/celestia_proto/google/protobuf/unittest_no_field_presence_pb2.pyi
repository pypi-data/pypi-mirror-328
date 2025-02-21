from google.protobuf import unittest_pb2 as _unittest_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForeignEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOREIGN_FOO: _ClassVar[ForeignEnum]
    FOREIGN_BAR: _ClassVar[ForeignEnum]
    FOREIGN_BAZ: _ClassVar[ForeignEnum]
FOREIGN_FOO: ForeignEnum
FOREIGN_BAR: ForeignEnum
FOREIGN_BAZ: ForeignEnum

class TestAllTypes(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optional_nested_message", "optional_foreign_message", "optional_proto2_message", "optional_nested_enum", "optional_foreign_enum", "optional_string_piece", "optional_cord", "optional_lazy_message", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeated_nested_message", "repeated_foreign_message", "repeated_proto2_message", "repeated_nested_enum", "repeated_foreign_enum", "repeated_string_piece", "repeated_cord", "repeated_lazy_message", "oneof_uint32", "oneof_nested_message", "oneof_string", "oneof_enum")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[TestAllTypes.NestedEnum]
        BAR: _ClassVar[TestAllTypes.NestedEnum]
        BAZ: _ClassVar[TestAllTypes.NestedEnum]
    FOO: TestAllTypes.NestedEnum
    BAR: TestAllTypes.NestedEnum
    BAZ: TestAllTypes.NestedEnum
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
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PROTO2_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SINT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SINT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_PROTO2_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CORD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_ENUM_FIELD_NUMBER: _ClassVar[int]
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
    optional_nested_message: TestAllTypes.NestedMessage
    optional_foreign_message: ForeignMessage
    optional_proto2_message: _unittest_pb2.TestAllTypes
    optional_nested_enum: TestAllTypes.NestedEnum
    optional_foreign_enum: ForeignEnum
    optional_string_piece: str
    optional_cord: str
    optional_lazy_message: TestAllTypes.NestedMessage
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    repeated_int64: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint32: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint64: _containers.RepeatedScalarFieldContainer[int]
    repeated_sint32: _containers.RepeatedScalarFieldContainer[int]
    repeated_sint64: _containers.RepeatedScalarFieldContainer[int]
    repeated_fixed32: _containers.RepeatedScalarFieldContainer[int]
    repeated_fixed64: _containers.RepeatedScalarFieldContainer[int]
    repeated_sfixed32: _containers.RepeatedScalarFieldContainer[int]
    repeated_sfixed64: _containers.RepeatedScalarFieldContainer[int]
    repeated_float: _containers.RepeatedScalarFieldContainer[float]
    repeated_double: _containers.RepeatedScalarFieldContainer[float]
    repeated_bool: _containers.RepeatedScalarFieldContainer[bool]
    repeated_string: _containers.RepeatedScalarFieldContainer[str]
    repeated_bytes: _containers.RepeatedScalarFieldContainer[bytes]
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]
    repeated_foreign_message: _containers.RepeatedCompositeFieldContainer[ForeignMessage]
    repeated_proto2_message: _containers.RepeatedCompositeFieldContainer[_unittest_pb2.TestAllTypes]
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypes.NestedEnum]
    repeated_foreign_enum: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    repeated_string_piece: _containers.RepeatedScalarFieldContainer[str]
    repeated_cord: _containers.RepeatedScalarFieldContainer[str]
    repeated_lazy_message: _containers.RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]
    oneof_uint32: int
    oneof_nested_message: TestAllTypes.NestedMessage
    oneof_string: str
    oneof_enum: TestAllTypes.NestedEnum
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_foreign_message: _Optional[_Union[ForeignMessage, _Mapping]] = ..., optional_proto2_message: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestAllTypes.NestedEnum, str]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnum, str]] = ..., optional_string_piece: _Optional[str] = ..., optional_cord: _Optional[str] = ..., optional_lazy_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., repeated_foreign_message: _Optional[_Iterable[_Union[ForeignMessage, _Mapping]]] = ..., repeated_proto2_message: _Optional[_Iterable[_Union[_unittest_pb2.TestAllTypes, _Mapping]]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypes.NestedEnum, str]]] = ..., repeated_foreign_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ..., repeated_string_piece: _Optional[_Iterable[str]] = ..., repeated_cord: _Optional[_Iterable[str]] = ..., repeated_lazy_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., oneof_uint32: _Optional[int] = ..., oneof_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_enum: _Optional[_Union[TestAllTypes.NestedEnum, str]] = ...) -> None: ...

class TestAllMapTypes(_message.Message):
    __slots__ = ("map_int32_bytes", "map_int32_foreign_enum", "map_int32_foreign_message", "map_int32_explicit_foreign_message")
    class MapInt32BytesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    class MapInt32ForeignEnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ForeignEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ForeignEnum, str]] = ...) -> None: ...
    class MapInt32ForeignMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ForeignMessage
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ForeignMessage, _Mapping]] = ...) -> None: ...
    class MapInt32ExplicitForeignMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ExplicitForeignMessage
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ExplicitForeignMessage, _Mapping]] = ...) -> None: ...
    MAP_INT32_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_EXPLICIT_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    map_int32_bytes: _containers.ScalarMap[int, bytes]
    map_int32_foreign_enum: _containers.ScalarMap[int, ForeignEnum]
    map_int32_foreign_message: _containers.MessageMap[int, ForeignMessage]
    map_int32_explicit_foreign_message: _containers.MessageMap[int, ExplicitForeignMessage]
    def __init__(self, map_int32_bytes: _Optional[_Mapping[int, bytes]] = ..., map_int32_foreign_enum: _Optional[_Mapping[int, ForeignEnum]] = ..., map_int32_foreign_message: _Optional[_Mapping[int, ForeignMessage]] = ..., map_int32_explicit_foreign_message: _Optional[_Mapping[int, ExplicitForeignMessage]] = ...) -> None: ...

class TestProto2Required(_message.Message):
    __slots__ = ("proto2",)
    PROTO2_FIELD_NUMBER: _ClassVar[int]
    proto2: _unittest_pb2.TestRequired
    def __init__(self, proto2: _Optional[_Union[_unittest_pb2.TestRequired, _Mapping]] = ...) -> None: ...

class ForeignMessage(_message.Message):
    __slots__ = ("c",)
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...

class ExplicitForeignMessage(_message.Message):
    __slots__ = ("c",)
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...
