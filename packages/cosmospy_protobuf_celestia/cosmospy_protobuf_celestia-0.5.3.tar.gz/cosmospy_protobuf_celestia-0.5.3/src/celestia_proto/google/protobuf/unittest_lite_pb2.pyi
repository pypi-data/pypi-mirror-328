from google.protobuf import unittest_import_lite_pb2 as _unittest_import_lite_pb2
from google.protobuf import unittest_import_public_lite_pb2 as _unittest_import_public_lite_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForeignEnumLite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOREIGN_LITE_FOO: _ClassVar[ForeignEnumLite]
    FOREIGN_LITE_BAZ: _ClassVar[ForeignEnumLite]
    FOREIGN_LITE_BAR: _ClassVar[ForeignEnumLite]

class V1EnumLite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    V1_FIRST: _ClassVar[V1EnumLite]

class V2EnumLite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    V2_FIRST: _ClassVar[V2EnumLite]
    V2_SECOND: _ClassVar[V2EnumLite]
FOREIGN_LITE_FOO: ForeignEnumLite
FOREIGN_LITE_BAZ: ForeignEnumLite
FOREIGN_LITE_BAR: ForeignEnumLite
V1_FIRST: V1EnumLite
V2_FIRST: V2EnumLite
V2_SECOND: V2EnumLite
OPTIONAL_INT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_int32_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_INT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_int64_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_UINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_uint32_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_UINT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_uint64_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_SINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_sint32_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_SINT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_sint64_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_FIXED32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_fixed32_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_FIXED64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_fixed64_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_SFIXED32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_sfixed32_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_SFIXED64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_sfixed64_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_FLOAT_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_float_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_DOUBLE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_double_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_BOOL_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_bool_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_STRING_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_string_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_BYTES_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_bytes_extension_lite: _descriptor.FieldDescriptor
OPTIONALGROUP_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optionalgroup_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_NESTED_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_nested_message_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_FOREIGN_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_foreign_message_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_IMPORT_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_import_message_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_NESTED_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_nested_enum_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_FOREIGN_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_foreign_enum_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_IMPORT_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_import_enum_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_STRING_PIECE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_string_piece_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_CORD_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_cord_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_BYTES_CORD_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_bytes_cord_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_PUBLIC_IMPORT_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_public_import_message_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_LAZY_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_lazy_message_extension_lite: _descriptor.FieldDescriptor
OPTIONAL_UNVERIFIED_LAZY_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
optional_unverified_lazy_message_extension_lite: _descriptor.FieldDescriptor
REPEATED_INT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_int32_extension_lite: _descriptor.FieldDescriptor
REPEATED_INT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_int64_extension_lite: _descriptor.FieldDescriptor
REPEATED_UINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_uint32_extension_lite: _descriptor.FieldDescriptor
REPEATED_UINT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_uint64_extension_lite: _descriptor.FieldDescriptor
REPEATED_SINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_sint32_extension_lite: _descriptor.FieldDescriptor
REPEATED_SINT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_sint64_extension_lite: _descriptor.FieldDescriptor
REPEATED_FIXED32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_fixed32_extension_lite: _descriptor.FieldDescriptor
REPEATED_FIXED64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_fixed64_extension_lite: _descriptor.FieldDescriptor
REPEATED_SFIXED32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_sfixed32_extension_lite: _descriptor.FieldDescriptor
REPEATED_SFIXED64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_sfixed64_extension_lite: _descriptor.FieldDescriptor
REPEATED_FLOAT_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_float_extension_lite: _descriptor.FieldDescriptor
REPEATED_DOUBLE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_double_extension_lite: _descriptor.FieldDescriptor
REPEATED_BOOL_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_bool_extension_lite: _descriptor.FieldDescriptor
REPEATED_STRING_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_string_extension_lite: _descriptor.FieldDescriptor
REPEATED_BYTES_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_bytes_extension_lite: _descriptor.FieldDescriptor
REPEATEDGROUP_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeatedgroup_extension_lite: _descriptor.FieldDescriptor
REPEATED_NESTED_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_nested_message_extension_lite: _descriptor.FieldDescriptor
REPEATED_FOREIGN_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_foreign_message_extension_lite: _descriptor.FieldDescriptor
REPEATED_IMPORT_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_import_message_extension_lite: _descriptor.FieldDescriptor
REPEATED_NESTED_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_nested_enum_extension_lite: _descriptor.FieldDescriptor
REPEATED_FOREIGN_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_foreign_enum_extension_lite: _descriptor.FieldDescriptor
REPEATED_IMPORT_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_import_enum_extension_lite: _descriptor.FieldDescriptor
REPEATED_STRING_PIECE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_string_piece_extension_lite: _descriptor.FieldDescriptor
REPEATED_CORD_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_cord_extension_lite: _descriptor.FieldDescriptor
REPEATED_LAZY_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
repeated_lazy_message_extension_lite: _descriptor.FieldDescriptor
DEFAULT_INT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_int32_extension_lite: _descriptor.FieldDescriptor
DEFAULT_INT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_int64_extension_lite: _descriptor.FieldDescriptor
DEFAULT_UINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_uint32_extension_lite: _descriptor.FieldDescriptor
DEFAULT_UINT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_uint64_extension_lite: _descriptor.FieldDescriptor
DEFAULT_SINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_sint32_extension_lite: _descriptor.FieldDescriptor
DEFAULT_SINT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_sint64_extension_lite: _descriptor.FieldDescriptor
DEFAULT_FIXED32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_fixed32_extension_lite: _descriptor.FieldDescriptor
DEFAULT_FIXED64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_fixed64_extension_lite: _descriptor.FieldDescriptor
DEFAULT_SFIXED32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_sfixed32_extension_lite: _descriptor.FieldDescriptor
DEFAULT_SFIXED64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_sfixed64_extension_lite: _descriptor.FieldDescriptor
DEFAULT_FLOAT_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_float_extension_lite: _descriptor.FieldDescriptor
DEFAULT_DOUBLE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_double_extension_lite: _descriptor.FieldDescriptor
DEFAULT_BOOL_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_bool_extension_lite: _descriptor.FieldDescriptor
DEFAULT_STRING_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_string_extension_lite: _descriptor.FieldDescriptor
DEFAULT_BYTES_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_bytes_extension_lite: _descriptor.FieldDescriptor
DEFAULT_NESTED_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_nested_enum_extension_lite: _descriptor.FieldDescriptor
DEFAULT_FOREIGN_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_foreign_enum_extension_lite: _descriptor.FieldDescriptor
DEFAULT_IMPORT_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_import_enum_extension_lite: _descriptor.FieldDescriptor
DEFAULT_STRING_PIECE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_string_piece_extension_lite: _descriptor.FieldDescriptor
DEFAULT_CORD_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
default_cord_extension_lite: _descriptor.FieldDescriptor
ONEOF_UINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
oneof_uint32_extension_lite: _descriptor.FieldDescriptor
ONEOF_NESTED_MESSAGE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
oneof_nested_message_extension_lite: _descriptor.FieldDescriptor
ONEOF_STRING_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
oneof_string_extension_lite: _descriptor.FieldDescriptor
ONEOF_BYTES_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
oneof_bytes_extension_lite: _descriptor.FieldDescriptor
PACKED_INT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_int32_extension_lite: _descriptor.FieldDescriptor
PACKED_INT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_int64_extension_lite: _descriptor.FieldDescriptor
PACKED_UINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_uint32_extension_lite: _descriptor.FieldDescriptor
PACKED_UINT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_uint64_extension_lite: _descriptor.FieldDescriptor
PACKED_SINT32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_sint32_extension_lite: _descriptor.FieldDescriptor
PACKED_SINT64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_sint64_extension_lite: _descriptor.FieldDescriptor
PACKED_FIXED32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_fixed32_extension_lite: _descriptor.FieldDescriptor
PACKED_FIXED64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_fixed64_extension_lite: _descriptor.FieldDescriptor
PACKED_SFIXED32_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_sfixed32_extension_lite: _descriptor.FieldDescriptor
PACKED_SFIXED64_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_sfixed64_extension_lite: _descriptor.FieldDescriptor
PACKED_FLOAT_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_float_extension_lite: _descriptor.FieldDescriptor
PACKED_DOUBLE_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_double_extension_lite: _descriptor.FieldDescriptor
PACKED_BOOL_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_bool_extension_lite: _descriptor.FieldDescriptor
PACKED_ENUM_EXTENSION_LITE_FIELD_NUMBER: _ClassVar[int]
packed_enum_extension_lite: _descriptor.FieldDescriptor
TEST_ALL_TYPES_LITE_FIELD_NUMBER: _ClassVar[int]
test_all_types_lite: _descriptor.FieldDescriptor

class TestAllTypesLite(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optionalgroup", "optional_nested_message", "optional_foreign_message", "optional_import_message", "optional_nested_enum", "optional_foreign_enum", "optional_import_enum", "optional_string_piece", "optional_cord", "optional_bytes_cord", "optional_public_import_message", "optional_lazy_message", "optional_unverified_lazy_message", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeatedgroup", "repeated_nested_message", "repeated_foreign_message", "repeated_import_message", "repeated_nested_enum", "repeated_foreign_enum", "repeated_import_enum", "repeated_string_piece", "repeated_cord", "repeated_lazy_message", "default_int32", "default_int64", "default_uint32", "default_uint64", "default_sint32", "default_sint64", "default_fixed32", "default_fixed64", "default_sfixed32", "default_sfixed64", "default_float", "default_double", "default_bool", "default_string", "default_bytes", "default_nested_enum", "default_foreign_enum", "default_import_enum", "default_string_piece", "default_cord", "oneof_uint32", "oneof_nested_message", "oneof_string", "oneof_bytes", "oneof_lazy_nested_message", "oneof_nested_message2", "deceptively_named_list")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[TestAllTypesLite.NestedEnum]
        BAR: _ClassVar[TestAllTypesLite.NestedEnum]
        BAZ: _ClassVar[TestAllTypesLite.NestedEnum]
    FOO: TestAllTypesLite.NestedEnum
    BAR: TestAllTypesLite.NestedEnum
    BAZ: TestAllTypesLite.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("bb", "cc", "dd")
        BB_FIELD_NUMBER: _ClassVar[int]
        CC_FIELD_NUMBER: _ClassVar[int]
        DD_FIELD_NUMBER: _ClassVar[int]
        bb: int
        cc: int
        dd: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, bb: _Optional[int] = ..., cc: _Optional[int] = ..., dd: _Optional[_Iterable[int]] = ...) -> None: ...
    class NestedMessage2(_message.Message):
        __slots__ = ("dd",)
        DD_FIELD_NUMBER: _ClassVar[int]
        dd: int
        def __init__(self, dd: _Optional[int] = ...) -> None: ...
    class OptionalGroup(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    class RepeatedGroup(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
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
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_IMPORT_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_CORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PUBLIC_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UNVERIFIED_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
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
    REPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_IMPORT_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CORD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INT32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INT64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_UINT32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_UINT64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SINT32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SINT64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIXED32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIXED64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BOOL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STRING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BYTES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_IMPORT_ENUM_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CORD_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    ONEOF_LAZY_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NESTED_MESSAGE2_FIELD_NUMBER: _ClassVar[int]
    DECEPTIVELY_NAMED_LIST_FIELD_NUMBER: _ClassVar[int]
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
    optionalgroup: TestAllTypesLite.OptionalGroup
    optional_nested_message: TestAllTypesLite.NestedMessage
    optional_foreign_message: ForeignMessageLite
    optional_import_message: _unittest_import_lite_pb2.ImportMessageLite
    optional_nested_enum: TestAllTypesLite.NestedEnum
    optional_foreign_enum: ForeignEnumLite
    optional_import_enum: _unittest_import_lite_pb2.ImportEnumLite
    optional_string_piece: str
    optional_cord: str
    optional_bytes_cord: bytes
    optional_public_import_message: _unittest_import_public_lite_pb2.PublicImportMessageLite
    optional_lazy_message: TestAllTypesLite.NestedMessage
    optional_unverified_lazy_message: TestAllTypesLite.NestedMessage
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
    repeatedgroup: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite.RepeatedGroup]
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite.NestedMessage]
    repeated_foreign_message: _containers.RepeatedCompositeFieldContainer[ForeignMessageLite]
    repeated_import_message: _containers.RepeatedCompositeFieldContainer[_unittest_import_lite_pb2.ImportMessageLite]
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypesLite.NestedEnum]
    repeated_foreign_enum: _containers.RepeatedScalarFieldContainer[ForeignEnumLite]
    repeated_import_enum: _containers.RepeatedScalarFieldContainer[_unittest_import_lite_pb2.ImportEnumLite]
    repeated_string_piece: _containers.RepeatedScalarFieldContainer[str]
    repeated_cord: _containers.RepeatedScalarFieldContainer[str]
    repeated_lazy_message: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite.NestedMessage]
    default_int32: int
    default_int64: int
    default_uint32: int
    default_uint64: int
    default_sint32: int
    default_sint64: int
    default_fixed32: int
    default_fixed64: int
    default_sfixed32: int
    default_sfixed64: int
    default_float: float
    default_double: float
    default_bool: bool
    default_string: str
    default_bytes: bytes
    default_nested_enum: TestAllTypesLite.NestedEnum
    default_foreign_enum: ForeignEnumLite
    default_import_enum: _unittest_import_lite_pb2.ImportEnumLite
    default_string_piece: str
    default_cord: str
    oneof_uint32: int
    oneof_nested_message: TestAllTypesLite.NestedMessage
    oneof_string: str
    oneof_bytes: bytes
    oneof_lazy_nested_message: TestAllTypesLite.NestedMessage
    oneof_nested_message2: TestAllTypesLite.NestedMessage2
    deceptively_named_list: int
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optionalgroup: _Optional[_Union[TestAllTypesLite.OptionalGroup, _Mapping]] = ..., optional_nested_message: _Optional[_Union[TestAllTypesLite.NestedMessage, _Mapping]] = ..., optional_foreign_message: _Optional[_Union[ForeignMessageLite, _Mapping]] = ..., optional_import_message: _Optional[_Union[_unittest_import_lite_pb2.ImportMessageLite, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestAllTypesLite.NestedEnum, str]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnumLite, str]] = ..., optional_import_enum: _Optional[_Union[_unittest_import_lite_pb2.ImportEnumLite, str]] = ..., optional_string_piece: _Optional[str] = ..., optional_cord: _Optional[str] = ..., optional_bytes_cord: _Optional[bytes] = ..., optional_public_import_message: _Optional[_Union[_unittest_import_public_lite_pb2.PublicImportMessageLite, _Mapping]] = ..., optional_lazy_message: _Optional[_Union[TestAllTypesLite.NestedMessage, _Mapping]] = ..., optional_unverified_lazy_message: _Optional[_Union[TestAllTypesLite.NestedMessage, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeatedgroup: _Optional[_Iterable[_Union[TestAllTypesLite.RepeatedGroup, _Mapping]]] = ..., repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypesLite.NestedMessage, _Mapping]]] = ..., repeated_foreign_message: _Optional[_Iterable[_Union[ForeignMessageLite, _Mapping]]] = ..., repeated_import_message: _Optional[_Iterable[_Union[_unittest_import_lite_pb2.ImportMessageLite, _Mapping]]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypesLite.NestedEnum, str]]] = ..., repeated_foreign_enum: _Optional[_Iterable[_Union[ForeignEnumLite, str]]] = ..., repeated_import_enum: _Optional[_Iterable[_Union[_unittest_import_lite_pb2.ImportEnumLite, str]]] = ..., repeated_string_piece: _Optional[_Iterable[str]] = ..., repeated_cord: _Optional[_Iterable[str]] = ..., repeated_lazy_message: _Optional[_Iterable[_Union[TestAllTypesLite.NestedMessage, _Mapping]]] = ..., default_int32: _Optional[int] = ..., default_int64: _Optional[int] = ..., default_uint32: _Optional[int] = ..., default_uint64: _Optional[int] = ..., default_sint32: _Optional[int] = ..., default_sint64: _Optional[int] = ..., default_fixed32: _Optional[int] = ..., default_fixed64: _Optional[int] = ..., default_sfixed32: _Optional[int] = ..., default_sfixed64: _Optional[int] = ..., default_float: _Optional[float] = ..., default_double: _Optional[float] = ..., default_bool: bool = ..., default_string: _Optional[str] = ..., default_bytes: _Optional[bytes] = ..., default_nested_enum: _Optional[_Union[TestAllTypesLite.NestedEnum, str]] = ..., default_foreign_enum: _Optional[_Union[ForeignEnumLite, str]] = ..., default_import_enum: _Optional[_Union[_unittest_import_lite_pb2.ImportEnumLite, str]] = ..., default_string_piece: _Optional[str] = ..., default_cord: _Optional[str] = ..., oneof_uint32: _Optional[int] = ..., oneof_nested_message: _Optional[_Union[TestAllTypesLite.NestedMessage, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ..., oneof_lazy_nested_message: _Optional[_Union[TestAllTypesLite.NestedMessage, _Mapping]] = ..., oneof_nested_message2: _Optional[_Union[TestAllTypesLite.NestedMessage2, _Mapping]] = ..., deceptively_named_list: _Optional[int] = ...) -> None: ...

class ForeignMessageLite(_message.Message):
    __slots__ = ("c",)
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...

class TestPackedTypesLite(_message.Message):
    __slots__ = ("packed_int32", "packed_int64", "packed_uint32", "packed_uint64", "packed_sint32", "packed_sint64", "packed_fixed32", "packed_fixed64", "packed_sfixed32", "packed_sfixed64", "packed_float", "packed_double", "packed_bool", "packed_enum")
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
    PACKED_ENUM_FIELD_NUMBER: _ClassVar[int]
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
    packed_enum: _containers.RepeatedScalarFieldContainer[ForeignEnumLite]
    def __init__(self, packed_int32: _Optional[_Iterable[int]] = ..., packed_int64: _Optional[_Iterable[int]] = ..., packed_uint32: _Optional[_Iterable[int]] = ..., packed_uint64: _Optional[_Iterable[int]] = ..., packed_sint32: _Optional[_Iterable[int]] = ..., packed_sint64: _Optional[_Iterable[int]] = ..., packed_fixed32: _Optional[_Iterable[int]] = ..., packed_fixed64: _Optional[_Iterable[int]] = ..., packed_sfixed32: _Optional[_Iterable[int]] = ..., packed_sfixed64: _Optional[_Iterable[int]] = ..., packed_float: _Optional[_Iterable[float]] = ..., packed_double: _Optional[_Iterable[float]] = ..., packed_bool: _Optional[_Iterable[bool]] = ..., packed_enum: _Optional[_Iterable[_Union[ForeignEnumLite, str]]] = ...) -> None: ...

class TestAllExtensionsLite(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class OptionalGroup_extension_lite(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class RepeatedGroup_extension_lite(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class TestPackedExtensionsLite(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestNestedExtensionLite(_message.Message):
    __slots__ = ()
    NESTED_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    nested_extension: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class TestDeprecatedLite(_message.Message):
    __slots__ = ("deprecated_field", "deprecated_field2", "deprecated_field3", "deprecated_field4")
    DEPRECATED_FIELD_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD2_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD3_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD4_FIELD_NUMBER: _ClassVar[int]
    deprecated_field: int
    deprecated_field2: int
    deprecated_field3: str
    deprecated_field4: TestDeprecatedLite
    def __init__(self, deprecated_field: _Optional[int] = ..., deprecated_field2: _Optional[int] = ..., deprecated_field3: _Optional[str] = ..., deprecated_field4: _Optional[_Union[TestDeprecatedLite, _Mapping]] = ...) -> None: ...

class TestParsingMergeLite(_message.Message):
    __slots__ = ("required_all_types", "optional_all_types", "repeated_all_types", "optionalgroup", "repeatedgroup")
    Extensions: _python_message._ExtensionDict
    class RepeatedFieldsGenerator(_message.Message):
        __slots__ = ("field1", "field2", "field3", "group1", "group2", "ext1", "ext2")
        class Group1(_message.Message):
            __slots__ = ("field1",)
            FIELD1_FIELD_NUMBER: _ClassVar[int]
            field1: TestAllTypesLite
            def __init__(self, field1: _Optional[_Union[TestAllTypesLite, _Mapping]] = ...) -> None: ...
        class Group2(_message.Message):
            __slots__ = ("field1",)
            FIELD1_FIELD_NUMBER: _ClassVar[int]
            field1: TestAllTypesLite
            def __init__(self, field1: _Optional[_Union[TestAllTypesLite, _Mapping]] = ...) -> None: ...
        FIELD1_FIELD_NUMBER: _ClassVar[int]
        FIELD2_FIELD_NUMBER: _ClassVar[int]
        FIELD3_FIELD_NUMBER: _ClassVar[int]
        GROUP1_FIELD_NUMBER: _ClassVar[int]
        GROUP2_FIELD_NUMBER: _ClassVar[int]
        EXT1_FIELD_NUMBER: _ClassVar[int]
        EXT2_FIELD_NUMBER: _ClassVar[int]
        field1: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite]
        field2: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite]
        field3: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite]
        group1: _containers.RepeatedCompositeFieldContainer[TestParsingMergeLite.RepeatedFieldsGenerator.Group1]
        group2: _containers.RepeatedCompositeFieldContainer[TestParsingMergeLite.RepeatedFieldsGenerator.Group2]
        ext1: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite]
        ext2: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite]
        def __init__(self, field1: _Optional[_Iterable[_Union[TestAllTypesLite, _Mapping]]] = ..., field2: _Optional[_Iterable[_Union[TestAllTypesLite, _Mapping]]] = ..., field3: _Optional[_Iterable[_Union[TestAllTypesLite, _Mapping]]] = ..., group1: _Optional[_Iterable[_Union[TestParsingMergeLite.RepeatedFieldsGenerator.Group1, _Mapping]]] = ..., group2: _Optional[_Iterable[_Union[TestParsingMergeLite.RepeatedFieldsGenerator.Group2, _Mapping]]] = ..., ext1: _Optional[_Iterable[_Union[TestAllTypesLite, _Mapping]]] = ..., ext2: _Optional[_Iterable[_Union[TestAllTypesLite, _Mapping]]] = ...) -> None: ...
    class OptionalGroup(_message.Message):
        __slots__ = ("optional_group_all_types",)
        OPTIONAL_GROUP_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
        optional_group_all_types: TestAllTypesLite
        def __init__(self, optional_group_all_types: _Optional[_Union[TestAllTypesLite, _Mapping]] = ...) -> None: ...
    class RepeatedGroup(_message.Message):
        __slots__ = ("repeated_group_all_types",)
        REPEATED_GROUP_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
        repeated_group_all_types: TestAllTypesLite
        def __init__(self, repeated_group_all_types: _Optional[_Union[TestAllTypesLite, _Mapping]] = ...) -> None: ...
    OPTIONAL_EXT_FIELD_NUMBER: _ClassVar[int]
    optional_ext: _descriptor.FieldDescriptor
    REPEATED_EXT_FIELD_NUMBER: _ClassVar[int]
    repeated_ext: _descriptor.FieldDescriptor
    REQUIRED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    REPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
    required_all_types: TestAllTypesLite
    optional_all_types: TestAllTypesLite
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypesLite]
    optionalgroup: TestParsingMergeLite.OptionalGroup
    repeatedgroup: _containers.RepeatedCompositeFieldContainer[TestParsingMergeLite.RepeatedGroup]
    def __init__(self, required_all_types: _Optional[_Union[TestAllTypesLite, _Mapping]] = ..., optional_all_types: _Optional[_Union[TestAllTypesLite, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypesLite, _Mapping]]] = ..., optionalgroup: _Optional[_Union[TestParsingMergeLite.OptionalGroup, _Mapping]] = ..., repeatedgroup: _Optional[_Iterable[_Union[TestParsingMergeLite.RepeatedGroup, _Mapping]]] = ...) -> None: ...

class TestMergeExceptionLite(_message.Message):
    __slots__ = ("all_extensions",)
    ALL_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    all_extensions: TestAllExtensionsLite
    def __init__(self, all_extensions: _Optional[_Union[TestAllExtensionsLite, _Mapping]] = ...) -> None: ...

class TestEmptyMessageLite(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestEmptyMessageWithExtensionsLite(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class V1MessageLite(_message.Message):
    __slots__ = ("int_field", "enum_field")
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    int_field: int
    enum_field: V1EnumLite
    def __init__(self, int_field: _Optional[int] = ..., enum_field: _Optional[_Union[V1EnumLite, str]] = ...) -> None: ...

class V2MessageLite(_message.Message):
    __slots__ = ("int_field", "enum_field")
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    int_field: int
    enum_field: V2EnumLite
    def __init__(self, int_field: _Optional[int] = ..., enum_field: _Optional[_Union[V2EnumLite, str]] = ...) -> None: ...

class TestHugeFieldNumbersLite(_message.Message):
    __slots__ = ("optional_int32", "fixed_32", "repeated_int32", "packed_int32", "optional_enum", "optional_string", "optional_bytes", "optional_message", "optionalgroup", "string_string_map", "oneof_uint32", "oneof_test_all_types", "oneof_string", "oneof_bytes")
    Extensions: _python_message._ExtensionDict
    class OptionalGroup(_message.Message):
        __slots__ = ("group_a",)
        GROUP_A_FIELD_NUMBER: _ClassVar[int]
        group_a: int
        def __init__(self, group_a: _Optional[int] = ...) -> None: ...
    class StringStringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    FIXED_32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    STRING_STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_TEST_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    optional_int32: int
    fixed_32: int
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    packed_int32: _containers.RepeatedScalarFieldContainer[int]
    optional_enum: ForeignEnumLite
    optional_string: str
    optional_bytes: bytes
    optional_message: ForeignMessageLite
    optionalgroup: TestHugeFieldNumbersLite.OptionalGroup
    string_string_map: _containers.ScalarMap[str, str]
    oneof_uint32: int
    oneof_test_all_types: TestAllTypesLite
    oneof_string: str
    oneof_bytes: bytes
    def __init__(self, optional_int32: _Optional[int] = ..., fixed_32: _Optional[int] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., packed_int32: _Optional[_Iterable[int]] = ..., optional_enum: _Optional[_Union[ForeignEnumLite, str]] = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_message: _Optional[_Union[ForeignMessageLite, _Mapping]] = ..., optionalgroup: _Optional[_Union[TestHugeFieldNumbersLite.OptionalGroup, _Mapping]] = ..., string_string_map: _Optional[_Mapping[str, str]] = ..., oneof_uint32: _Optional[int] = ..., oneof_test_all_types: _Optional[_Union[TestAllTypesLite, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ...) -> None: ...

class TestOneofParsingLite(_message.Message):
    __slots__ = ("oneof_int32", "oneof_submessage", "oneof_string", "oneof_bytes", "oneof_string_cord", "oneof_bytes_cord", "oneof_string_string_piece", "oneof_bytes_string_piece", "oneof_enum")
    ONEOF_INT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_SUBMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_CORD_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_CORD_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_ENUM_FIELD_NUMBER: _ClassVar[int]
    oneof_int32: int
    oneof_submessage: TestAllTypesLite
    oneof_string: str
    oneof_bytes: bytes
    oneof_string_cord: str
    oneof_bytes_cord: bytes
    oneof_string_string_piece: str
    oneof_bytes_string_piece: bytes
    oneof_enum: V2EnumLite
    def __init__(self, oneof_int32: _Optional[int] = ..., oneof_submessage: _Optional[_Union[TestAllTypesLite, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ..., oneof_string_cord: _Optional[str] = ..., oneof_bytes_cord: _Optional[bytes] = ..., oneof_string_string_piece: _Optional[str] = ..., oneof_bytes_string_piece: _Optional[bytes] = ..., oneof_enum: _Optional[_Union[V2EnumLite, str]] = ...) -> None: ...

class TestMessageSetLite(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class PackedInt32(_message.Message):
    __slots__ = ("repeated_int32",)
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, repeated_int32: _Optional[_Iterable[int]] = ...) -> None: ...

class NonPackedInt32(_message.Message):
    __slots__ = ("repeated_int32",)
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, repeated_int32: _Optional[_Iterable[int]] = ...) -> None: ...

class PackedFixed32(_message.Message):
    __slots__ = ("repeated_fixed32",)
    REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    repeated_fixed32: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, repeated_fixed32: _Optional[_Iterable[int]] = ...) -> None: ...

class NonPackedFixed32(_message.Message):
    __slots__ = ("repeated_fixed32",)
    REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    repeated_fixed32: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, repeated_fixed32: _Optional[_Iterable[int]] = ...) -> None: ...

class DupEnum(_message.Message):
    __slots__ = ()
    class TestEnumWithDupValueLite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO1: _ClassVar[DupEnum.TestEnumWithDupValueLite]
        BAR1: _ClassVar[DupEnum.TestEnumWithDupValueLite]
        BAZ: _ClassVar[DupEnum.TestEnumWithDupValueLite]
        FOO2: _ClassVar[DupEnum.TestEnumWithDupValueLite]
        BAR2: _ClassVar[DupEnum.TestEnumWithDupValueLite]
    FOO1: DupEnum.TestEnumWithDupValueLite
    BAR1: DupEnum.TestEnumWithDupValueLite
    BAZ: DupEnum.TestEnumWithDupValueLite
    FOO2: DupEnum.TestEnumWithDupValueLite
    BAR2: DupEnum.TestEnumWithDupValueLite
    def __init__(self) -> None: ...

class RecursiveMessage(_message.Message):
    __slots__ = ("recurse", "payload")
    RECURSE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    recurse: RecursiveMessage
    payload: bytes
    def __init__(self, recurse: _Optional[_Union[RecursiveMessage, _Mapping]] = ..., payload: _Optional[bytes] = ...) -> None: ...

class RecursiveGroup(_message.Message):
    __slots__ = ("recurse",)
    RECURSE_FIELD_NUMBER: _ClassVar[int]
    recurse: RecursiveGroup
    def __init__(self, recurse: _Optional[_Union[RecursiveGroup, _Mapping]] = ...) -> None: ...
