from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
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

class TestAllTypesProto3(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optional_nested_message", "optional_foreign_message", "optional_nested_enum", "optional_foreign_enum", "optional_aliased_enum", "optional_string_piece", "optional_cord", "recursive_message", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeated_nested_message", "repeated_foreign_message", "repeated_nested_enum", "repeated_foreign_enum", "repeated_string_piece", "repeated_cord", "packed_int32", "packed_int64", "packed_uint32", "packed_uint64", "packed_sint32", "packed_sint64", "packed_fixed32", "packed_fixed64", "packed_sfixed32", "packed_sfixed64", "packed_float", "packed_double", "packed_bool", "packed_nested_enum", "unpacked_int32", "unpacked_int64", "unpacked_uint32", "unpacked_uint64", "unpacked_sint32", "unpacked_sint64", "unpacked_fixed32", "unpacked_fixed64", "unpacked_sfixed32", "unpacked_sfixed64", "unpacked_float", "unpacked_double", "unpacked_bool", "unpacked_nested_enum", "map_int32_int32", "map_int64_int64", "map_uint32_uint32", "map_uint64_uint64", "map_sint32_sint32", "map_sint64_sint64", "map_fixed32_fixed32", "map_fixed64_fixed64", "map_sfixed32_sfixed32", "map_sfixed64_sfixed64", "map_int32_float", "map_int32_double", "map_bool_bool", "map_string_string", "map_string_bytes", "map_string_nested_message", "map_string_foreign_message", "map_string_nested_enum", "map_string_foreign_enum", "oneof_uint32", "oneof_nested_message", "oneof_string", "oneof_bytes", "oneof_bool", "oneof_uint64", "oneof_float", "oneof_double", "oneof_enum", "oneof_null_value", "optional_bool_wrapper", "optional_int32_wrapper", "optional_int64_wrapper", "optional_uint32_wrapper", "optional_uint64_wrapper", "optional_float_wrapper", "optional_double_wrapper", "optional_string_wrapper", "optional_bytes_wrapper", "repeated_bool_wrapper", "repeated_int32_wrapper", "repeated_int64_wrapper", "repeated_uint32_wrapper", "repeated_uint64_wrapper", "repeated_float_wrapper", "repeated_double_wrapper", "repeated_string_wrapper", "repeated_bytes_wrapper", "optional_duration", "optional_timestamp", "optional_field_mask", "optional_struct", "optional_any", "optional_value", "optional_null_value", "repeated_duration", "repeated_timestamp", "repeated_fieldmask", "repeated_struct", "repeated_any", "repeated_value", "repeated_list_value", "fieldname1", "field_name2", "_field_name3", "field__name4_", "field0name5", "field_0_name6", "fieldName7", "FieldName8", "field_Name9", "Field_Name10", "FIELD_NAME11", "FIELD_name12", "__field_name13", "__Field_name14", "field__name15", "field__Name16", "field_name17__", "Field_name18__")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[TestAllTypesProto3.NestedEnum]
        BAR: _ClassVar[TestAllTypesProto3.NestedEnum]
        BAZ: _ClassVar[TestAllTypesProto3.NestedEnum]
        NEG: _ClassVar[TestAllTypesProto3.NestedEnum]
    FOO: TestAllTypesProto3.NestedEnum
    BAR: TestAllTypesProto3.NestedEnum
    BAZ: TestAllTypesProto3.NestedEnum
    NEG: TestAllTypesProto3.NestedEnum
    class AliasedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALIAS_FOO: _ClassVar[TestAllTypesProto3.AliasedEnum]
        ALIAS_BAR: _ClassVar[TestAllTypesProto3.AliasedEnum]
        ALIAS_BAZ: _ClassVar[TestAllTypesProto3.AliasedEnum]
        MOO: _ClassVar[TestAllTypesProto3.AliasedEnum]
        moo: _ClassVar[TestAllTypesProto3.AliasedEnum]
        bAz: _ClassVar[TestAllTypesProto3.AliasedEnum]
    ALIAS_FOO: TestAllTypesProto3.AliasedEnum
    ALIAS_BAR: TestAllTypesProto3.AliasedEnum
    ALIAS_BAZ: TestAllTypesProto3.AliasedEnum
    MOO: TestAllTypesProto3.AliasedEnum
    moo: TestAllTypesProto3.AliasedEnum
    bAz: TestAllTypesProto3.AliasedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("a", "corecursive")
        A_FIELD_NUMBER: _ClassVar[int]
        CORECURSIVE_FIELD_NUMBER: _ClassVar[int]
        a: int
        corecursive: TestAllTypesProto3
        def __init__(self, a: _Optional[int] = ..., corecursive: _Optional[_Union[TestAllTypesProto3, _Mapping]] = ...) -> None: ...
    class MapInt32Int32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapInt64Int64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapUint32Uint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapUint64Uint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapSint32Sint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapSint64Sint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapFixed32Fixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapFixed64Fixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapSfixed32Sfixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapSfixed64Sfixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapInt32FloatEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class MapInt32DoubleEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class MapBoolBoolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: bool
        def __init__(self, key: bool = ..., value: bool = ...) -> None: ...
    class MapStringStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MapStringBytesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class MapStringNestedMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestAllTypesProto3.NestedMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestAllTypesProto3.NestedMessage, _Mapping]] = ...) -> None: ...
    class MapStringForeignMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ForeignMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ForeignMessage, _Mapping]] = ...) -> None: ...
    class MapStringNestedEnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestAllTypesProto3.NestedEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestAllTypesProto3.NestedEnum, str]] = ...) -> None: ...
    class MapStringForeignEnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ForeignEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ForeignEnum, str]] = ...) -> None: ...
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
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALIASED_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CORD_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
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
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CORD_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_UINT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_UINT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_SINT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_SINT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    PACKED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    PACKED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    PACKED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    PACKED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    PACKED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    PACKED_BOOL_FIELD_NUMBER: _ClassVar[int]
    PACKED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_INT32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_INT64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_UINT32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_UINT64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_SINT32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_SINT64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_BOOL_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_INT32_FIELD_NUMBER: _ClassVar[int]
    MAP_INT64_INT64_FIELD_NUMBER: _ClassVar[int]
    MAP_UINT32_UINT32_FIELD_NUMBER: _ClassVar[int]
    MAP_UINT64_UINT64_FIELD_NUMBER: _ClassVar[int]
    MAP_SINT32_SINT32_FIELD_NUMBER: _ClassVar[int]
    MAP_SINT64_SINT64_FIELD_NUMBER: _ClassVar[int]
    MAP_FIXED32_FIXED32_FIELD_NUMBER: _ClassVar[int]
    MAP_FIXED64_FIXED64_FIELD_NUMBER: _ClassVar[int]
    MAP_SFIXED32_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    MAP_SFIXED64_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_FLOAT_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    MAP_BOOL_BOOL_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BOOL_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ONEOF_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_ENUM_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BOOL_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT64_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FLOAT_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DOUBLE_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT32_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT64_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DURATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRUCT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ANY_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DURATION_FIELD_NUMBER: _ClassVar[int]
    REPEATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIELDMASK_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRUCT_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ANY_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME1_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME2_FIELD_NUMBER: _ClassVar[int]
    _FIELD_NAME3_FIELD_NUMBER: _ClassVar[int]
    FIELD__NAME4__FIELD_NUMBER: _ClassVar[int]
    FIELD0NAME5_FIELD_NUMBER: _ClassVar[int]
    FIELD_0_NAME6_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME7_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME8_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME9_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME10_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME11_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME12_FIELD_NUMBER: _ClassVar[int]
    __FIELD_NAME13_FIELD_NUMBER: _ClassVar[int]
    __FIELD_NAME14_FIELD_NUMBER: _ClassVar[int]
    FIELD__NAME15_FIELD_NUMBER: _ClassVar[int]
    FIELD__NAME16_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME17___FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME18___FIELD_NUMBER: _ClassVar[int]
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
    optional_nested_message: TestAllTypesProto3.NestedMessage
    optional_foreign_message: ForeignMessage
    optional_nested_enum: TestAllTypesProto3.NestedEnum
    optional_foreign_enum: ForeignEnum
    optional_aliased_enum: TestAllTypesProto3.AliasedEnum
    optional_string_piece: str
    optional_cord: str
    recursive_message: TestAllTypesProto3
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
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[TestAllTypesProto3.NestedMessage]
    repeated_foreign_message: _containers.RepeatedCompositeFieldContainer[ForeignMessage]
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypesProto3.NestedEnum]
    repeated_foreign_enum: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    repeated_string_piece: _containers.RepeatedScalarFieldContainer[str]
    repeated_cord: _containers.RepeatedScalarFieldContainer[str]
    packed_int32: _containers.RepeatedScalarFieldContainer[int]
    packed_int64: _containers.RepeatedScalarFieldContainer[int]
    packed_uint32: _containers.RepeatedScalarFieldContainer[int]
    packed_uint64: _containers.RepeatedScalarFieldContainer[int]
    packed_sint32: _containers.RepeatedScalarFieldContainer[int]
    packed_sint64: _containers.RepeatedScalarFieldContainer[int]
    packed_fixed32: _containers.RepeatedScalarFieldContainer[int]
    packed_fixed64: _containers.RepeatedScalarFieldContainer[int]
    packed_sfixed32: _containers.RepeatedScalarFieldContainer[int]
    packed_sfixed64: _containers.RepeatedScalarFieldContainer[int]
    packed_float: _containers.RepeatedScalarFieldContainer[float]
    packed_double: _containers.RepeatedScalarFieldContainer[float]
    packed_bool: _containers.RepeatedScalarFieldContainer[bool]
    packed_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypesProto3.NestedEnum]
    unpacked_int32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_int64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_uint32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_uint64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_sint32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_sint64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_fixed32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_fixed64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_sfixed32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_sfixed64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_float: _containers.RepeatedScalarFieldContainer[float]
    unpacked_double: _containers.RepeatedScalarFieldContainer[float]
    unpacked_bool: _containers.RepeatedScalarFieldContainer[bool]
    unpacked_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypesProto3.NestedEnum]
    map_int32_int32: _containers.ScalarMap[int, int]
    map_int64_int64: _containers.ScalarMap[int, int]
    map_uint32_uint32: _containers.ScalarMap[int, int]
    map_uint64_uint64: _containers.ScalarMap[int, int]
    map_sint32_sint32: _containers.ScalarMap[int, int]
    map_sint64_sint64: _containers.ScalarMap[int, int]
    map_fixed32_fixed32: _containers.ScalarMap[int, int]
    map_fixed64_fixed64: _containers.ScalarMap[int, int]
    map_sfixed32_sfixed32: _containers.ScalarMap[int, int]
    map_sfixed64_sfixed64: _containers.ScalarMap[int, int]
    map_int32_float: _containers.ScalarMap[int, float]
    map_int32_double: _containers.ScalarMap[int, float]
    map_bool_bool: _containers.ScalarMap[bool, bool]
    map_string_string: _containers.ScalarMap[str, str]
    map_string_bytes: _containers.ScalarMap[str, bytes]
    map_string_nested_message: _containers.MessageMap[str, TestAllTypesProto3.NestedMessage]
    map_string_foreign_message: _containers.MessageMap[str, ForeignMessage]
    map_string_nested_enum: _containers.ScalarMap[str, TestAllTypesProto3.NestedEnum]
    map_string_foreign_enum: _containers.ScalarMap[str, ForeignEnum]
    oneof_uint32: int
    oneof_nested_message: TestAllTypesProto3.NestedMessage
    oneof_string: str
    oneof_bytes: bytes
    oneof_bool: bool
    oneof_uint64: int
    oneof_float: float
    oneof_double: float
    oneof_enum: TestAllTypesProto3.NestedEnum
    oneof_null_value: _struct_pb2.NullValue
    optional_bool_wrapper: _wrappers_pb2.BoolValue
    optional_int32_wrapper: _wrappers_pb2.Int32Value
    optional_int64_wrapper: _wrappers_pb2.Int64Value
    optional_uint32_wrapper: _wrappers_pb2.UInt32Value
    optional_uint64_wrapper: _wrappers_pb2.UInt64Value
    optional_float_wrapper: _wrappers_pb2.FloatValue
    optional_double_wrapper: _wrappers_pb2.DoubleValue
    optional_string_wrapper: _wrappers_pb2.StringValue
    optional_bytes_wrapper: _wrappers_pb2.BytesValue
    repeated_bool_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BoolValue]
    repeated_int32_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int32Value]
    repeated_int64_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
    repeated_uint32_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt32Value]
    repeated_uint64_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt64Value]
    repeated_float_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.FloatValue]
    repeated_double_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.DoubleValue]
    repeated_string_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    repeated_bytes_wrapper: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BytesValue]
    optional_duration: _duration_pb2.Duration
    optional_timestamp: _timestamp_pb2.Timestamp
    optional_field_mask: _field_mask_pb2.FieldMask
    optional_struct: _struct_pb2.Struct
    optional_any: _any_pb2.Any
    optional_value: _struct_pb2.Value
    optional_null_value: _struct_pb2.NullValue
    repeated_duration: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    repeated_timestamp: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    repeated_fieldmask: _containers.RepeatedCompositeFieldContainer[_field_mask_pb2.FieldMask]
    repeated_struct: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    repeated_any: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    repeated_value: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    repeated_list_value: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
    fieldname1: int
    field_name2: int
    _field_name3: int
    field__name4_: int
    field0name5: int
    field_0_name6: int
    fieldName7: int
    FieldName8: int
    field_Name9: int
    Field_Name10: int
    FIELD_NAME11: int
    FIELD_name12: int
    __field_name13: int
    __Field_name14: int
    field__name15: int
    field__Name16: int
    field_name17__: int
    Field_name18__: int
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_nested_message: _Optional[_Union[TestAllTypesProto3.NestedMessage, _Mapping]] = ..., optional_foreign_message: _Optional[_Union[ForeignMessage, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestAllTypesProto3.NestedEnum, str]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnum, str]] = ..., optional_aliased_enum: _Optional[_Union[TestAllTypesProto3.AliasedEnum, str]] = ..., optional_string_piece: _Optional[str] = ..., optional_cord: _Optional[str] = ..., recursive_message: _Optional[_Union[TestAllTypesProto3, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypesProto3.NestedMessage, _Mapping]]] = ..., repeated_foreign_message: _Optional[_Iterable[_Union[ForeignMessage, _Mapping]]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypesProto3.NestedEnum, str]]] = ..., repeated_foreign_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ..., repeated_string_piece: _Optional[_Iterable[str]] = ..., repeated_cord: _Optional[_Iterable[str]] = ..., packed_int32: _Optional[_Iterable[int]] = ..., packed_int64: _Optional[_Iterable[int]] = ..., packed_uint32: _Optional[_Iterable[int]] = ..., packed_uint64: _Optional[_Iterable[int]] = ..., packed_sint32: _Optional[_Iterable[int]] = ..., packed_sint64: _Optional[_Iterable[int]] = ..., packed_fixed32: _Optional[_Iterable[int]] = ..., packed_fixed64: _Optional[_Iterable[int]] = ..., packed_sfixed32: _Optional[_Iterable[int]] = ..., packed_sfixed64: _Optional[_Iterable[int]] = ..., packed_float: _Optional[_Iterable[float]] = ..., packed_double: _Optional[_Iterable[float]] = ..., packed_bool: _Optional[_Iterable[bool]] = ..., packed_nested_enum: _Optional[_Iterable[_Union[TestAllTypesProto3.NestedEnum, str]]] = ..., unpacked_int32: _Optional[_Iterable[int]] = ..., unpacked_int64: _Optional[_Iterable[int]] = ..., unpacked_uint32: _Optional[_Iterable[int]] = ..., unpacked_uint64: _Optional[_Iterable[int]] = ..., unpacked_sint32: _Optional[_Iterable[int]] = ..., unpacked_sint64: _Optional[_Iterable[int]] = ..., unpacked_fixed32: _Optional[_Iterable[int]] = ..., unpacked_fixed64: _Optional[_Iterable[int]] = ..., unpacked_sfixed32: _Optional[_Iterable[int]] = ..., unpacked_sfixed64: _Optional[_Iterable[int]] = ..., unpacked_float: _Optional[_Iterable[float]] = ..., unpacked_double: _Optional[_Iterable[float]] = ..., unpacked_bool: _Optional[_Iterable[bool]] = ..., unpacked_nested_enum: _Optional[_Iterable[_Union[TestAllTypesProto3.NestedEnum, str]]] = ..., map_int32_int32: _Optional[_Mapping[int, int]] = ..., map_int64_int64: _Optional[_Mapping[int, int]] = ..., map_uint32_uint32: _Optional[_Mapping[int, int]] = ..., map_uint64_uint64: _Optional[_Mapping[int, int]] = ..., map_sint32_sint32: _Optional[_Mapping[int, int]] = ..., map_sint64_sint64: _Optional[_Mapping[int, int]] = ..., map_fixed32_fixed32: _Optional[_Mapping[int, int]] = ..., map_fixed64_fixed64: _Optional[_Mapping[int, int]] = ..., map_sfixed32_sfixed32: _Optional[_Mapping[int, int]] = ..., map_sfixed64_sfixed64: _Optional[_Mapping[int, int]] = ..., map_int32_float: _Optional[_Mapping[int, float]] = ..., map_int32_double: _Optional[_Mapping[int, float]] = ..., map_bool_bool: _Optional[_Mapping[bool, bool]] = ..., map_string_string: _Optional[_Mapping[str, str]] = ..., map_string_bytes: _Optional[_Mapping[str, bytes]] = ..., map_string_nested_message: _Optional[_Mapping[str, TestAllTypesProto3.NestedMessage]] = ..., map_string_foreign_message: _Optional[_Mapping[str, ForeignMessage]] = ..., map_string_nested_enum: _Optional[_Mapping[str, TestAllTypesProto3.NestedEnum]] = ..., map_string_foreign_enum: _Optional[_Mapping[str, ForeignEnum]] = ..., oneof_uint32: _Optional[int] = ..., oneof_nested_message: _Optional[_Union[TestAllTypesProto3.NestedMessage, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ..., oneof_bool: bool = ..., oneof_uint64: _Optional[int] = ..., oneof_float: _Optional[float] = ..., oneof_double: _Optional[float] = ..., oneof_enum: _Optional[_Union[TestAllTypesProto3.NestedEnum, str]] = ..., oneof_null_value: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., optional_bool_wrapper: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., optional_int32_wrapper: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., optional_int64_wrapper: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., optional_uint32_wrapper: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., optional_uint64_wrapper: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., optional_float_wrapper: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., optional_double_wrapper: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., optional_string_wrapper: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., optional_bytes_wrapper: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., repeated_bool_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.BoolValue, _Mapping]]] = ..., repeated_int32_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.Int32Value, _Mapping]]] = ..., repeated_int64_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ..., repeated_uint32_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.UInt32Value, _Mapping]]] = ..., repeated_uint64_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.UInt64Value, _Mapping]]] = ..., repeated_float_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.FloatValue, _Mapping]]] = ..., repeated_double_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.DoubleValue, _Mapping]]] = ..., repeated_string_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., repeated_bytes_wrapper: _Optional[_Iterable[_Union[_wrappers_pb2.BytesValue, _Mapping]]] = ..., optional_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., optional_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., optional_field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., optional_struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., optional_any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., optional_value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., optional_null_value: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., repeated_duration: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]] = ..., repeated_timestamp: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ..., repeated_fieldmask: _Optional[_Iterable[_Union[_field_mask_pb2.FieldMask, _Mapping]]] = ..., repeated_struct: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., repeated_any: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., repeated_value: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ..., repeated_list_value: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]] = ..., fieldname1: _Optional[int] = ..., field_name2: _Optional[int] = ..., _field_name3: _Optional[int] = ..., field__name4_: _Optional[int] = ..., field0name5: _Optional[int] = ..., field_0_name6: _Optional[int] = ..., fieldName7: _Optional[int] = ..., FieldName8: _Optional[int] = ..., field_Name9: _Optional[int] = ..., Field_Name10: _Optional[int] = ..., FIELD_NAME11: _Optional[int] = ..., FIELD_name12: _Optional[int] = ..., __field_name13: _Optional[int] = ..., __Field_name14: _Optional[int] = ..., field__name15: _Optional[int] = ..., field__Name16: _Optional[int] = ..., field_name17__: _Optional[int] = ..., Field_name18__: _Optional[int] = ...) -> None: ...

class ForeignMessage(_message.Message):
    __slots__ = ("c",)
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...

class NullHypothesisProto3(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnumOnlyProto3(_message.Message):
    __slots__ = ()
    class Bool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFalse: _ClassVar[EnumOnlyProto3.Bool]
        kTrue: _ClassVar[EnumOnlyProto3.Bool]
    kFalse: EnumOnlyProto3.Bool
    kTrue: EnumOnlyProto3.Bool
    def __init__(self) -> None: ...
