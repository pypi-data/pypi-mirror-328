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
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optional_nested_message", "optional_foreign_message", "optional_import_message", "optional_nested_enum", "optional_foreign_enum", "optional_string_piece", "optional_cord", "optional_bytes_cord", "optional_public_import_message", "optional_lazy_message", "optional_unverified_lazy_message", "optional_lazy_import_message", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "proto3_optional_int32", "proto3_optional_int64", "proto3_optional_uint32", "proto3_optional_uint64", "proto3_optional_sint32", "proto3_optional_sint64", "proto3_optional_fixed32", "proto3_optional_fixed64", "proto3_optional_sfixed32", "proto3_optional_sfixed64", "proto3_optional_float", "proto3_optional_double", "proto3_optional_bool", "proto3_optional_string", "proto3_optional_bytes", "repeated_nested_message", "repeated_foreign_message", "repeated_import_message", "repeated_nested_enum", "repeated_foreign_enum", "repeated_string_piece", "repeated_cord", "repeated_lazy_message", "oneof_uint32", "oneof_nested_message", "oneof_string", "oneof_bytes")
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
    OPTIONAL_BYTES_CORD_FIELD_NUMBER: _ClassVar[int]
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
    PROTO3_OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_INT64_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_UINT32_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_UINT64_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_SINT32_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_SINT64_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_FIXED32_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_FIXED64_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_BOOL_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
    PROTO3_OPTIONAL_BYTES_FIELD_NUMBER: _ClassVar[int]
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
    optional_bytes_cord: bytes
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
    proto3_optional_int32: int
    proto3_optional_int64: int
    proto3_optional_uint32: int
    proto3_optional_uint64: int
    proto3_optional_sint32: int
    proto3_optional_sint64: int
    proto3_optional_fixed32: int
    proto3_optional_fixed64: int
    proto3_optional_sfixed32: int
    proto3_optional_sfixed64: int
    proto3_optional_float: float
    proto3_optional_double: float
    proto3_optional_bool: bool
    proto3_optional_string: str
    proto3_optional_bytes: bytes
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
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_foreign_message: _Optional[_Union[ForeignMessage, _Mapping]] = ..., optional_import_message: _Optional[_Union[_unittest_import_pb2.ImportMessage, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestAllTypes.NestedEnum, str]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnum, str]] = ..., optional_string_piece: _Optional[str] = ..., optional_cord: _Optional[str] = ..., optional_bytes_cord: _Optional[bytes] = ..., optional_public_import_message: _Optional[_Union[_unittest_import_public_pb2.PublicImportMessage, _Mapping]] = ..., optional_lazy_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_unverified_lazy_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_lazy_import_message: _Optional[_Union[_unittest_import_pb2.ImportMessage, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., proto3_optional_int32: _Optional[int] = ..., proto3_optional_int64: _Optional[int] = ..., proto3_optional_uint32: _Optional[int] = ..., proto3_optional_uint64: _Optional[int] = ..., proto3_optional_sint32: _Optional[int] = ..., proto3_optional_sint64: _Optional[int] = ..., proto3_optional_fixed32: _Optional[int] = ..., proto3_optional_fixed64: _Optional[int] = ..., proto3_optional_sfixed32: _Optional[int] = ..., proto3_optional_sfixed64: _Optional[int] = ..., proto3_optional_float: _Optional[float] = ..., proto3_optional_double: _Optional[float] = ..., proto3_optional_bool: bool = ..., proto3_optional_string: _Optional[str] = ..., proto3_optional_bytes: _Optional[bytes] = ..., repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., repeated_foreign_message: _Optional[_Iterable[_Union[ForeignMessage, _Mapping]]] = ..., repeated_import_message: _Optional[_Iterable[_Union[_unittest_import_pb2.ImportMessage, _Mapping]]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypes.NestedEnum, str]]] = ..., repeated_foreign_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ..., repeated_string_piece: _Optional[_Iterable[str]] = ..., repeated_cord: _Optional[_Iterable[str]] = ..., repeated_lazy_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., oneof_uint32: _Optional[int] = ..., oneof_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ...) -> None: ...

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
    __slots__ = ("child", "payload", "repeated_child", "lazy_payload")
    CHILD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CHILD_FIELD_NUMBER: _ClassVar[int]
    LAZY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    child: NestedTestAllTypes
    payload: TestAllTypes
    repeated_child: _containers.RepeatedCompositeFieldContainer[NestedTestAllTypes]
    lazy_payload: TestAllTypes
    def __init__(self, child: _Optional[_Union[NestedTestAllTypes, _Mapping]] = ..., payload: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_child: _Optional[_Iterable[_Union[NestedTestAllTypes, _Mapping]]] = ..., lazy_payload: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...

class ForeignMessage(_message.Message):
    __slots__ = ("c",)
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...

class TestEmptyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestPickleNestedMessage(_message.Message):
    __slots__ = ()
    class NestedMessage(_message.Message):
        __slots__ = ("bb",)
        class NestedNestedMessage(_message.Message):
            __slots__ = ("cc",)
            CC_FIELD_NUMBER: _ClassVar[int]
            cc: int
            def __init__(self, cc: _Optional[int] = ...) -> None: ...
        BB_FIELD_NUMBER: _ClassVar[int]
        bb: int
        def __init__(self, bb: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
