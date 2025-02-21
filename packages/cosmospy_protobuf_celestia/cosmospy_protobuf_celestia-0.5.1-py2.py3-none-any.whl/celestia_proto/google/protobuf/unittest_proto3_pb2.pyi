from google.protobuf import unittest_import_pb2 as _unittest_import_pb2
from google.protobuf import unittest_import_public_pb2 as _unittest_import_public_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForeignEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOREIGN_ZERO: _ClassVar[ForeignEnum]
    FOREIGN_FOO: _ClassVar[ForeignEnum]
    FOREIGN_BAR: _ClassVar[ForeignEnum]
    FOREIGN_BAZ: _ClassVar[ForeignEnum]
    FOREIGN_LARGE: _ClassVar[ForeignEnum]
FOREIGN_ZERO: ForeignEnum
FOREIGN_FOO: ForeignEnum
FOREIGN_BAR: ForeignEnum
FOREIGN_BAZ: ForeignEnum
FOREIGN_LARGE: ForeignEnum

class TestAllTypes(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optional_nested_message", "optional_foreign_message", "optional_import_message", "optional_nested_enum", "optional_foreign_enum", "optional_string_piece", "optional_cord", "optional_public_import_message", "optional_lazy_message", "optional_unverified_lazy_message", "optional_lazy_import_message", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeated_nested_message", "repeated_foreign_message", "repeated_import_message", "repeated_nested_enum", "repeated_foreign_enum", "repeated_string_piece", "repeated_cord", "repeated_lazy_message", "oneof_uint32", "oneof_nested_message", "oneof_string", "oneof_bytes")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZERO: _ClassVar[TestAllTypes.NestedEnum]
        FOO: _ClassVar[TestAllTypes.NestedEnum]
        BAR: _ClassVar[TestAllTypes.NestedEnum]
        BAZ: _ClassVar[TestAllTypes.NestedEnum]
        NEG: _ClassVar[TestAllTypes.NestedEnum]
    ZERO: TestAllTypes.NestedEnum
    FOO: TestAllTypes.NestedEnum
    BAR: TestAllTypes.NestedEnum
    BAZ: TestAllTypes.NestedEnum
    NEG: TestAllTypes.NestedEnum
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
    OPTIONAL_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PUBLIC_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UNVERIFIED_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LAZY_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
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
    REPEATED_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CORD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
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
    optional_import_message: _unittest_import_pb2.ImportMessage
    optional_nested_enum: TestAllTypes.NestedEnum
    optional_foreign_enum: ForeignEnum
    optional_string_piece: str
    optional_cord: str
    optional_public_import_message: _unittest_import_public_pb2.PublicImportMessage
    optional_lazy_message: TestAllTypes.NestedMessage
    optional_unverified_lazy_message: TestAllTypes.NestedMessage
    optional_lazy_import_message: _unittest_import_pb2.ImportMessage
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
    repeated_import_message: _containers.RepeatedCompositeFieldContainer[_unittest_import_pb2.ImportMessage]
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypes.NestedEnum]
    repeated_foreign_enum: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    repeated_string_piece: _containers.RepeatedScalarFieldContainer[str]
    repeated_cord: _containers.RepeatedScalarFieldContainer[str]
    repeated_lazy_message: _containers.RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]
    oneof_uint32: int
    oneof_nested_message: TestAllTypes.NestedMessage
    oneof_string: str
    oneof_bytes: bytes
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_foreign_message: _Optional[_Union[ForeignMessage, _Mapping]] = ..., optional_import_message: _Optional[_Union[_unittest_import_pb2.ImportMessage, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestAllTypes.NestedEnum, str]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnum, str]] = ..., optional_string_piece: _Optional[str] = ..., optional_cord: _Optional[str] = ..., optional_public_import_message: _Optional[_Union[_unittest_import_public_pb2.PublicImportMessage, _Mapping]] = ..., optional_lazy_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_unverified_lazy_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_lazy_import_message: _Optional[_Union[_unittest_import_pb2.ImportMessage, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., repeated_foreign_message: _Optional[_Iterable[_Union[ForeignMessage, _Mapping]]] = ..., repeated_import_message: _Optional[_Iterable[_Union[_unittest_import_pb2.ImportMessage, _Mapping]]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypes.NestedEnum, str]]] = ..., repeated_foreign_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ..., repeated_string_piece: _Optional[_Iterable[str]] = ..., repeated_cord: _Optional[_Iterable[str]] = ..., repeated_lazy_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., oneof_uint32: _Optional[int] = ..., oneof_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ...) -> None: ...

class TestPackedTypes(_message.Message):
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
    packed_enum: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    def __init__(self, packed_int32: _Optional[_Iterable[int]] = ..., packed_int64: _Optional[_Iterable[int]] = ..., packed_uint32: _Optional[_Iterable[int]] = ..., packed_uint64: _Optional[_Iterable[int]] = ..., packed_sint32: _Optional[_Iterable[int]] = ..., packed_sint64: _Optional[_Iterable[int]] = ..., packed_fixed32: _Optional[_Iterable[int]] = ..., packed_fixed64: _Optional[_Iterable[int]] = ..., packed_sfixed32: _Optional[_Iterable[int]] = ..., packed_sfixed64: _Optional[_Iterable[int]] = ..., packed_float: _Optional[_Iterable[float]] = ..., packed_double: _Optional[_Iterable[float]] = ..., packed_bool: _Optional[_Iterable[bool]] = ..., packed_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ...) -> None: ...

class TestUnpackedTypes(_message.Message):
    __slots__ = ("repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_nested_enum")
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
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
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
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypes.NestedEnum]
    def __init__(self, repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypes.NestedEnum, str]]] = ...) -> None: ...

class NestedTestAllTypes(_message.Message):
    __slots__ = ("child", "payload")
    CHILD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    child: NestedTestAllTypes
    payload: TestAllTypes
    def __init__(self, child: _Optional[_Union[NestedTestAllTypes, _Mapping]] = ..., payload: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...

class ForeignMessage(_message.Message):
    __slots__ = ("c",)
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...

class TestEmptyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestMessageWithDummy(_message.Message):
    __slots__ = ("dummy",)
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    dummy: bool
    def __init__(self, dummy: bool = ...) -> None: ...

class TestOneof2(_message.Message):
    __slots__ = ("foo_enum",)
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[TestOneof2.NestedEnum]
        FOO: _ClassVar[TestOneof2.NestedEnum]
        BAR: _ClassVar[TestOneof2.NestedEnum]
        BAZ: _ClassVar[TestOneof2.NestedEnum]
    UNKNOWN: TestOneof2.NestedEnum
    FOO: TestOneof2.NestedEnum
    BAR: TestOneof2.NestedEnum
    BAZ: TestOneof2.NestedEnum
    FOO_ENUM_FIELD_NUMBER: _ClassVar[int]
    foo_enum: TestOneof2.NestedEnum
    def __init__(self, foo_enum: _Optional[_Union[TestOneof2.NestedEnum, str]] = ...) -> None: ...

class TestHasbits(_message.Message):
    __slots__ = ("b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "b11", "b12", "b13", "b14", "b15", "b16", "b17", "b18", "b19", "b20", "b21", "b22", "b23", "b24", "b25", "b26", "b27", "b28", "b29", "b30", "b31", "b32", "b33", "b34", "b35", "b36", "b37", "b38", "b39", "b40", "b41", "b42", "b43", "b44", "b45", "b46", "b47", "b48", "b49", "b50", "b51", "b52", "b53", "b54", "b55", "b56", "b57", "b58", "b59", "b60", "b61", "b62", "b63", "b64", "b65", "b66", "b67", "b68", "b69", "child")
    B1_FIELD_NUMBER: _ClassVar[int]
    B2_FIELD_NUMBER: _ClassVar[int]
    B3_FIELD_NUMBER: _ClassVar[int]
    B4_FIELD_NUMBER: _ClassVar[int]
    B5_FIELD_NUMBER: _ClassVar[int]
    B6_FIELD_NUMBER: _ClassVar[int]
    B7_FIELD_NUMBER: _ClassVar[int]
    B8_FIELD_NUMBER: _ClassVar[int]
    B9_FIELD_NUMBER: _ClassVar[int]
    B10_FIELD_NUMBER: _ClassVar[int]
    B11_FIELD_NUMBER: _ClassVar[int]
    B12_FIELD_NUMBER: _ClassVar[int]
    B13_FIELD_NUMBER: _ClassVar[int]
    B14_FIELD_NUMBER: _ClassVar[int]
    B15_FIELD_NUMBER: _ClassVar[int]
    B16_FIELD_NUMBER: _ClassVar[int]
    B17_FIELD_NUMBER: _ClassVar[int]
    B18_FIELD_NUMBER: _ClassVar[int]
    B19_FIELD_NUMBER: _ClassVar[int]
    B20_FIELD_NUMBER: _ClassVar[int]
    B21_FIELD_NUMBER: _ClassVar[int]
    B22_FIELD_NUMBER: _ClassVar[int]
    B23_FIELD_NUMBER: _ClassVar[int]
    B24_FIELD_NUMBER: _ClassVar[int]
    B25_FIELD_NUMBER: _ClassVar[int]
    B26_FIELD_NUMBER: _ClassVar[int]
    B27_FIELD_NUMBER: _ClassVar[int]
    B28_FIELD_NUMBER: _ClassVar[int]
    B29_FIELD_NUMBER: _ClassVar[int]
    B30_FIELD_NUMBER: _ClassVar[int]
    B31_FIELD_NUMBER: _ClassVar[int]
    B32_FIELD_NUMBER: _ClassVar[int]
    B33_FIELD_NUMBER: _ClassVar[int]
    B34_FIELD_NUMBER: _ClassVar[int]
    B35_FIELD_NUMBER: _ClassVar[int]
    B36_FIELD_NUMBER: _ClassVar[int]
    B37_FIELD_NUMBER: _ClassVar[int]
    B38_FIELD_NUMBER: _ClassVar[int]
    B39_FIELD_NUMBER: _ClassVar[int]
    B40_FIELD_NUMBER: _ClassVar[int]
    B41_FIELD_NUMBER: _ClassVar[int]
    B42_FIELD_NUMBER: _ClassVar[int]
    B43_FIELD_NUMBER: _ClassVar[int]
    B44_FIELD_NUMBER: _ClassVar[int]
    B45_FIELD_NUMBER: _ClassVar[int]
    B46_FIELD_NUMBER: _ClassVar[int]
    B47_FIELD_NUMBER: _ClassVar[int]
    B48_FIELD_NUMBER: _ClassVar[int]
    B49_FIELD_NUMBER: _ClassVar[int]
    B50_FIELD_NUMBER: _ClassVar[int]
    B51_FIELD_NUMBER: _ClassVar[int]
    B52_FIELD_NUMBER: _ClassVar[int]
    B53_FIELD_NUMBER: _ClassVar[int]
    B54_FIELD_NUMBER: _ClassVar[int]
    B55_FIELD_NUMBER: _ClassVar[int]
    B56_FIELD_NUMBER: _ClassVar[int]
    B57_FIELD_NUMBER: _ClassVar[int]
    B58_FIELD_NUMBER: _ClassVar[int]
    B59_FIELD_NUMBER: _ClassVar[int]
    B60_FIELD_NUMBER: _ClassVar[int]
    B61_FIELD_NUMBER: _ClassVar[int]
    B62_FIELD_NUMBER: _ClassVar[int]
    B63_FIELD_NUMBER: _ClassVar[int]
    B64_FIELD_NUMBER: _ClassVar[int]
    B65_FIELD_NUMBER: _ClassVar[int]
    B66_FIELD_NUMBER: _ClassVar[int]
    B67_FIELD_NUMBER: _ClassVar[int]
    B68_FIELD_NUMBER: _ClassVar[int]
    B69_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    b1: bool
    b2: bool
    b3: bool
    b4: bool
    b5: bool
    b6: bool
    b7: bool
    b8: bool
    b9: bool
    b10: bool
    b11: bool
    b12: bool
    b13: bool
    b14: bool
    b15: bool
    b16: bool
    b17: bool
    b18: bool
    b19: bool
    b20: bool
    b21: bool
    b22: bool
    b23: bool
    b24: bool
    b25: bool
    b26: bool
    b27: bool
    b28: bool
    b29: bool
    b30: bool
    b31: bool
    b32: bool
    b33: bool
    b34: bool
    b35: bool
    b36: bool
    b37: bool
    b38: bool
    b39: bool
    b40: bool
    b41: bool
    b42: bool
    b43: bool
    b44: bool
    b45: bool
    b46: bool
    b47: bool
    b48: bool
    b49: bool
    b50: bool
    b51: bool
    b52: bool
    b53: bool
    b54: bool
    b55: bool
    b56: bool
    b57: bool
    b58: bool
    b59: bool
    b60: bool
    b61: bool
    b62: bool
    b63: bool
    b64: bool
    b65: bool
    b66: bool
    b67: bool
    b68: bool
    b69: bool
    child: TestAllTypes
    def __init__(self, b1: bool = ..., b2: bool = ..., b3: bool = ..., b4: bool = ..., b5: bool = ..., b6: bool = ..., b7: bool = ..., b8: bool = ..., b9: bool = ..., b10: bool = ..., b11: bool = ..., b12: bool = ..., b13: bool = ..., b14: bool = ..., b15: bool = ..., b16: bool = ..., b17: bool = ..., b18: bool = ..., b19: bool = ..., b20: bool = ..., b21: bool = ..., b22: bool = ..., b23: bool = ..., b24: bool = ..., b25: bool = ..., b26: bool = ..., b27: bool = ..., b28: bool = ..., b29: bool = ..., b30: bool = ..., b31: bool = ..., b32: bool = ..., b33: bool = ..., b34: bool = ..., b35: bool = ..., b36: bool = ..., b37: bool = ..., b38: bool = ..., b39: bool = ..., b40: bool = ..., b41: bool = ..., b42: bool = ..., b43: bool = ..., b44: bool = ..., b45: bool = ..., b46: bool = ..., b47: bool = ..., b48: bool = ..., b49: bool = ..., b50: bool = ..., b51: bool = ..., b52: bool = ..., b53: bool = ..., b54: bool = ..., b55: bool = ..., b56: bool = ..., b57: bool = ..., b58: bool = ..., b59: bool = ..., b60: bool = ..., b61: bool = ..., b62: bool = ..., b63: bool = ..., b64: bool = ..., b65: bool = ..., b66: bool = ..., b67: bool = ..., b68: bool = ..., b69: bool = ..., child: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...
