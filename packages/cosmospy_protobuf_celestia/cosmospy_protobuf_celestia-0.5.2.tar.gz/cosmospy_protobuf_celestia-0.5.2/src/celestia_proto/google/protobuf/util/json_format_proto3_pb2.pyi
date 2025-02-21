from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import unittest_pb2 as _unittest_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOO: _ClassVar[EnumType]
    BAR: _ClassVar[EnumType]
    TLSv1_2: _ClassVar[EnumType]
FOO: EnumType
BAR: EnumType
TLSv1_2: EnumType

class MessageType(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class TestMessage(_message.Message):
    __slots__ = ("bool_value", "int32_value", "int64_value", "uint32_value", "uint64_value", "float_value", "double_value", "string_value", "bytes_value", "enum_value", "message_value", "repeated_bool_value", "repeated_int32_value", "repeated_int64_value", "repeated_uint32_value", "repeated_uint64_value", "repeated_float_value", "repeated_double_value", "repeated_string_value", "repeated_bytes_value", "repeated_enum_value", "repeated_message_value", "optional_bool_value", "optional_int32_value", "optional_int64_value", "optional_uint32_value", "optional_uint64_value", "optional_float_value", "optional_double_value", "optional_string_value", "optional_bytes_value", "optional_enum_value", "optional_message_value")
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MESSAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_MESSAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    int32_value: int
    int64_value: int
    uint32_value: int
    uint64_value: int
    float_value: float
    double_value: float
    string_value: str
    bytes_value: bytes
    enum_value: EnumType
    message_value: MessageType
    repeated_bool_value: _containers.RepeatedScalarFieldContainer[bool]
    repeated_int32_value: _containers.RepeatedScalarFieldContainer[int]
    repeated_int64_value: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint32_value: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint64_value: _containers.RepeatedScalarFieldContainer[int]
    repeated_float_value: _containers.RepeatedScalarFieldContainer[float]
    repeated_double_value: _containers.RepeatedScalarFieldContainer[float]
    repeated_string_value: _containers.RepeatedScalarFieldContainer[str]
    repeated_bytes_value: _containers.RepeatedScalarFieldContainer[bytes]
    repeated_enum_value: _containers.RepeatedScalarFieldContainer[EnumType]
    repeated_message_value: _containers.RepeatedCompositeFieldContainer[MessageType]
    optional_bool_value: bool
    optional_int32_value: int
    optional_int64_value: int
    optional_uint32_value: int
    optional_uint64_value: int
    optional_float_value: float
    optional_double_value: float
    optional_string_value: str
    optional_bytes_value: bytes
    optional_enum_value: EnumType
    optional_message_value: MessageType
    def __init__(self, bool_value: bool = ..., int32_value: _Optional[int] = ..., int64_value: _Optional[int] = ..., uint32_value: _Optional[int] = ..., uint64_value: _Optional[int] = ..., float_value: _Optional[float] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., bytes_value: _Optional[bytes] = ..., enum_value: _Optional[_Union[EnumType, str]] = ..., message_value: _Optional[_Union[MessageType, _Mapping]] = ..., repeated_bool_value: _Optional[_Iterable[bool]] = ..., repeated_int32_value: _Optional[_Iterable[int]] = ..., repeated_int64_value: _Optional[_Iterable[int]] = ..., repeated_uint32_value: _Optional[_Iterable[int]] = ..., repeated_uint64_value: _Optional[_Iterable[int]] = ..., repeated_float_value: _Optional[_Iterable[float]] = ..., repeated_double_value: _Optional[_Iterable[float]] = ..., repeated_string_value: _Optional[_Iterable[str]] = ..., repeated_bytes_value: _Optional[_Iterable[bytes]] = ..., repeated_enum_value: _Optional[_Iterable[_Union[EnumType, str]]] = ..., repeated_message_value: _Optional[_Iterable[_Union[MessageType, _Mapping]]] = ..., optional_bool_value: bool = ..., optional_int32_value: _Optional[int] = ..., optional_int64_value: _Optional[int] = ..., optional_uint32_value: _Optional[int] = ..., optional_uint64_value: _Optional[int] = ..., optional_float_value: _Optional[float] = ..., optional_double_value: _Optional[float] = ..., optional_string_value: _Optional[str] = ..., optional_bytes_value: _Optional[bytes] = ..., optional_enum_value: _Optional[_Union[EnumType, str]] = ..., optional_message_value: _Optional[_Union[MessageType, _Mapping]] = ...) -> None: ...

class TestOneof(_message.Message):
    __slots__ = ("oneof_int32_value", "oneof_string_value", "oneof_bytes_value", "oneof_enum_value", "oneof_message_value", "oneof_null_value")
    ONEOF_INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_MESSAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    oneof_int32_value: int
    oneof_string_value: str
    oneof_bytes_value: bytes
    oneof_enum_value: EnumType
    oneof_message_value: MessageType
    oneof_null_value: _struct_pb2.NullValue
    def __init__(self, oneof_int32_value: _Optional[int] = ..., oneof_string_value: _Optional[str] = ..., oneof_bytes_value: _Optional[bytes] = ..., oneof_enum_value: _Optional[_Union[EnumType, str]] = ..., oneof_message_value: _Optional[_Union[MessageType, _Mapping]] = ..., oneof_null_value: _Optional[_Union[_struct_pb2.NullValue, str]] = ...) -> None: ...

class TestMap(_message.Message):
    __slots__ = ("bool_map", "int32_map", "int64_map", "uint32_map", "uint64_map", "string_map")
    class BoolMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: int
        def __init__(self, key: bool = ..., value: _Optional[int] = ...) -> None: ...
    class Int32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Uint32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Uint64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class StringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BOOL_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    INT64_MAP_FIELD_NUMBER: _ClassVar[int]
    UINT32_MAP_FIELD_NUMBER: _ClassVar[int]
    UINT64_MAP_FIELD_NUMBER: _ClassVar[int]
    STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    bool_map: _containers.ScalarMap[bool, int]
    int32_map: _containers.ScalarMap[int, int]
    int64_map: _containers.ScalarMap[int, int]
    uint32_map: _containers.ScalarMap[int, int]
    uint64_map: _containers.ScalarMap[int, int]
    string_map: _containers.ScalarMap[str, int]
    def __init__(self, bool_map: _Optional[_Mapping[bool, int]] = ..., int32_map: _Optional[_Mapping[int, int]] = ..., int64_map: _Optional[_Mapping[int, int]] = ..., uint32_map: _Optional[_Mapping[int, int]] = ..., uint64_map: _Optional[_Mapping[int, int]] = ..., string_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class TestNestedMap(_message.Message):
    __slots__ = ("bool_map", "int32_map", "int64_map", "uint32_map", "uint64_map", "string_map", "map_map")
    class BoolMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: int
        def __init__(self, key: bool = ..., value: _Optional[int] = ...) -> None: ...
    class Int32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Uint32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Uint64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class StringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class MapMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestNestedMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestNestedMap, _Mapping]] = ...) -> None: ...
    BOOL_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    INT64_MAP_FIELD_NUMBER: _ClassVar[int]
    UINT32_MAP_FIELD_NUMBER: _ClassVar[int]
    UINT64_MAP_FIELD_NUMBER: _ClassVar[int]
    STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    MAP_MAP_FIELD_NUMBER: _ClassVar[int]
    bool_map: _containers.ScalarMap[bool, int]
    int32_map: _containers.ScalarMap[int, int]
    int64_map: _containers.ScalarMap[int, int]
    uint32_map: _containers.ScalarMap[int, int]
    uint64_map: _containers.ScalarMap[int, int]
    string_map: _containers.ScalarMap[str, int]
    map_map: _containers.MessageMap[str, TestNestedMap]
    def __init__(self, bool_map: _Optional[_Mapping[bool, int]] = ..., int32_map: _Optional[_Mapping[int, int]] = ..., int64_map: _Optional[_Mapping[int, int]] = ..., uint32_map: _Optional[_Mapping[int, int]] = ..., uint64_map: _Optional[_Mapping[int, int]] = ..., string_map: _Optional[_Mapping[str, int]] = ..., map_map: _Optional[_Mapping[str, TestNestedMap]] = ...) -> None: ...

class TestStringMap(_message.Message):
    __slots__ = ("string_map",)
    class StringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    string_map: _containers.ScalarMap[str, str]
    def __init__(self, string_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TestWrapper(_message.Message):
    __slots__ = ("bool_value", "int32_value", "int64_value", "uint32_value", "uint64_value", "float_value", "double_value", "string_value", "bytes_value", "repeated_bool_value", "repeated_int32_value", "repeated_int64_value", "repeated_uint32_value", "repeated_uint64_value", "repeated_float_value", "repeated_double_value", "repeated_string_value", "repeated_bytes_value")
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    bool_value: _wrappers_pb2.BoolValue
    int32_value: _wrappers_pb2.Int32Value
    int64_value: _wrappers_pb2.Int64Value
    uint32_value: _wrappers_pb2.UInt32Value
    uint64_value: _wrappers_pb2.UInt64Value
    float_value: _wrappers_pb2.FloatValue
    double_value: _wrappers_pb2.DoubleValue
    string_value: _wrappers_pb2.StringValue
    bytes_value: _wrappers_pb2.BytesValue
    repeated_bool_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BoolValue]
    repeated_int32_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int32Value]
    repeated_int64_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
    repeated_uint32_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt32Value]
    repeated_uint64_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt64Value]
    repeated_float_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.FloatValue]
    repeated_double_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.DoubleValue]
    repeated_string_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    repeated_bytes_value: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BytesValue]
    def __init__(self, bool_value: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., int32_value: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., int64_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., uint32_value: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., uint64_value: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., float_value: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., double_value: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., string_value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., bytes_value: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., repeated_bool_value: _Optional[_Iterable[_Union[_wrappers_pb2.BoolValue, _Mapping]]] = ..., repeated_int32_value: _Optional[_Iterable[_Union[_wrappers_pb2.Int32Value, _Mapping]]] = ..., repeated_int64_value: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ..., repeated_uint32_value: _Optional[_Iterable[_Union[_wrappers_pb2.UInt32Value, _Mapping]]] = ..., repeated_uint64_value: _Optional[_Iterable[_Union[_wrappers_pb2.UInt64Value, _Mapping]]] = ..., repeated_float_value: _Optional[_Iterable[_Union[_wrappers_pb2.FloatValue, _Mapping]]] = ..., repeated_double_value: _Optional[_Iterable[_Union[_wrappers_pb2.DoubleValue, _Mapping]]] = ..., repeated_string_value: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., repeated_bytes_value: _Optional[_Iterable[_Union[_wrappers_pb2.BytesValue, _Mapping]]] = ...) -> None: ...

class TestTimestamp(_message.Message):
    __slots__ = ("value", "repeated_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _timestamp_pb2.Timestamp
    repeated_value: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., repeated_value: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class TestDuration(_message.Message):
    __slots__ = ("value", "repeated_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _duration_pb2.Duration
    repeated_value: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    def __init__(self, value: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., repeated_value: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]] = ...) -> None: ...

class TestFieldMask(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _field_mask_pb2.FieldMask
    def __init__(self, value: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class TestStruct(_message.Message):
    __slots__ = ("value", "repeated_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _struct_pb2.Struct
    repeated_value: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(self, value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., repeated_value: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...) -> None: ...

class TestAny(_message.Message):
    __slots__ = ("value", "repeated_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _any_pb2.Any
    repeated_value: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., repeated_value: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class TestValue(_message.Message):
    __slots__ = ("value", "repeated_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _struct_pb2.Value
    repeated_value: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., repeated_value: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ...) -> None: ...

class TestListValue(_message.Message):
    __slots__ = ("value", "repeated_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _struct_pb2.ListValue
    repeated_value: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
    def __init__(self, value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., repeated_value: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]] = ...) -> None: ...

class TestBoolValue(_message.Message):
    __slots__ = ("bool_value", "bool_map")
    class BoolMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: int
        def __init__(self, key: bool = ..., value: _Optional[int] = ...) -> None: ...
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_MAP_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    bool_map: _containers.ScalarMap[bool, int]
    def __init__(self, bool_value: bool = ..., bool_map: _Optional[_Mapping[bool, int]] = ...) -> None: ...

class TestNullValue(_message.Message):
    __slots__ = ("null_value", "repeated_null_value")
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    null_value: _struct_pb2.NullValue
    repeated_null_value: _containers.RepeatedScalarFieldContainer[_struct_pb2.NullValue]
    def __init__(self, null_value: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., repeated_null_value: _Optional[_Iterable[_Union[_struct_pb2.NullValue, str]]] = ...) -> None: ...

class TestCustomJsonName(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class TestEvilJson(_message.Message):
    __slots__ = ("regular_value", "script", "quotes", "script_and_quotes", "empty_string", "backslash", "low_codepoint")
    REGULAR_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    QUOTES_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_AND_QUOTES_FIELD_NUMBER: _ClassVar[int]
    EMPTY_STRING_FIELD_NUMBER: _ClassVar[int]
    BACKSLASH_FIELD_NUMBER: _ClassVar[int]
    LOW_CODEPOINT_FIELD_NUMBER: _ClassVar[int]
    regular_value: int
    script: int
    quotes: int
    script_and_quotes: int
    empty_string: int
    backslash: int
    low_codepoint: int
    def __init__(self, regular_value: _Optional[int] = ..., script: _Optional[int] = ..., quotes: _Optional[int] = ..., script_and_quotes: _Optional[int] = ..., empty_string: _Optional[int] = ..., backslash: _Optional[int] = ..., low_codepoint: _Optional[int] = ...) -> None: ...

class TestExtensions(_message.Message):
    __slots__ = ("extensions",)
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    extensions: _unittest_pb2.TestAllExtensions
    def __init__(self, extensions: _Optional[_Union[_unittest_pb2.TestAllExtensions, _Mapping]] = ...) -> None: ...

class TestEnumValue(_message.Message):
    __slots__ = ("enum_value1", "enum_value2", "enum_value3")
    ENUM_VALUE1_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE2_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE3_FIELD_NUMBER: _ClassVar[int]
    enum_value1: EnumType
    enum_value2: EnumType
    enum_value3: EnumType
    def __init__(self, enum_value1: _Optional[_Union[EnumType, str]] = ..., enum_value2: _Optional[_Union[EnumType, str]] = ..., enum_value3: _Optional[_Union[EnumType, str]] = ...) -> None: ...

class MapsTestCases(_message.Message):
    __slots__ = ("empty_map", "string_to_int", "int_to_string", "mixed1", "mixed2", "map_of_objects", "empty_key_string_to_int1", "empty_key_string_to_int2", "empty_key_string_to_int3", "empty_key_bool_to_string", "empty_key_int_to_string", "empty_key_mixed", "empty_key_map_objects")
    EMPTY_MAP_FIELD_NUMBER: _ClassVar[int]
    STRING_TO_INT_FIELD_NUMBER: _ClassVar[int]
    INT_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    MIXED1_FIELD_NUMBER: _ClassVar[int]
    MIXED2_FIELD_NUMBER: _ClassVar[int]
    MAP_OF_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_STRING_TO_INT1_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_STRING_TO_INT2_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_STRING_TO_INT3_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_BOOL_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_INT_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_MIXED_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_MAP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    empty_map: EmptyMap
    string_to_int: StringtoInt
    int_to_string: IntToString
    mixed1: Mixed1
    mixed2: Mixed2
    map_of_objects: MapOfObjects
    empty_key_string_to_int1: StringtoInt
    empty_key_string_to_int2: StringtoInt
    empty_key_string_to_int3: StringtoInt
    empty_key_bool_to_string: BoolToString
    empty_key_int_to_string: IntToString
    empty_key_mixed: Mixed1
    empty_key_map_objects: MapOfObjects
    def __init__(self, empty_map: _Optional[_Union[EmptyMap, _Mapping]] = ..., string_to_int: _Optional[_Union[StringtoInt, _Mapping]] = ..., int_to_string: _Optional[_Union[IntToString, _Mapping]] = ..., mixed1: _Optional[_Union[Mixed1, _Mapping]] = ..., mixed2: _Optional[_Union[Mixed2, _Mapping]] = ..., map_of_objects: _Optional[_Union[MapOfObjects, _Mapping]] = ..., empty_key_string_to_int1: _Optional[_Union[StringtoInt, _Mapping]] = ..., empty_key_string_to_int2: _Optional[_Union[StringtoInt, _Mapping]] = ..., empty_key_string_to_int3: _Optional[_Union[StringtoInt, _Mapping]] = ..., empty_key_bool_to_string: _Optional[_Union[BoolToString, _Mapping]] = ..., empty_key_int_to_string: _Optional[_Union[IntToString, _Mapping]] = ..., empty_key_mixed: _Optional[_Union[Mixed1, _Mapping]] = ..., empty_key_map_objects: _Optional[_Union[MapOfObjects, _Mapping]] = ...) -> None: ...

class EmptyMap(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[int, int]
    def __init__(self, map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class StringtoInt(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[str, int]
    def __init__(self, map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class IntToString(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[int, str]
    def __init__(self, map: _Optional[_Mapping[int, str]] = ...) -> None: ...

class BoolToString(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: str
        def __init__(self, key: bool = ..., value: _Optional[str] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[bool, str]
    def __init__(self, map: _Optional[_Mapping[bool, str]] = ...) -> None: ...

class Mixed1(_message.Message):
    __slots__ = ("msg", "map")
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    MSG_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    msg: str
    map: _containers.ScalarMap[str, float]
    def __init__(self, msg: _Optional[str] = ..., map: _Optional[_Mapping[str, float]] = ...) -> None: ...

class Mixed2(_message.Message):
    __slots__ = ("map", "ee")
    class E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        E0: _ClassVar[Mixed2.E]
        E1: _ClassVar[Mixed2.E]
        E2: _ClassVar[Mixed2.E]
        E3: _ClassVar[Mixed2.E]
    E0: Mixed2.E
    E1: Mixed2.E
    E2: Mixed2.E
    E3: Mixed2.E
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    EE_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[int, bool]
    ee: Mixed2.E
    def __init__(self, map: _Optional[_Mapping[int, bool]] = ..., ee: _Optional[_Union[Mixed2.E, str]] = ...) -> None: ...

class MapOfObjects(_message.Message):
    __slots__ = ("map",)
    class M(_message.Message):
        __slots__ = ("inner_text",)
        INNER_TEXT_FIELD_NUMBER: _ClassVar[int]
        inner_text: str
        def __init__(self, inner_text: _Optional[str] = ...) -> None: ...
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapOfObjects.M
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapOfObjects.M, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, MapOfObjects.M]
    def __init__(self, map: _Optional[_Mapping[str, MapOfObjects.M]] = ...) -> None: ...

class MapOfEnums(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EnumType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EnumType, str]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[str, EnumType]
    def __init__(self, map: _Optional[_Mapping[str, EnumType]] = ...) -> None: ...

class MapIn(_message.Message):
    __slots__ = ("other", "things", "map_input", "map_any")
    class MapInputEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MapAnyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    OTHER_FIELD_NUMBER: _ClassVar[int]
    THINGS_FIELD_NUMBER: _ClassVar[int]
    MAP_INPUT_FIELD_NUMBER: _ClassVar[int]
    MAP_ANY_FIELD_NUMBER: _ClassVar[int]
    other: str
    things: _containers.RepeatedScalarFieldContainer[str]
    map_input: _containers.ScalarMap[str, str]
    map_any: _containers.MessageMap[str, _any_pb2.Any]
    def __init__(self, other: _Optional[str] = ..., things: _Optional[_Iterable[str]] = ..., map_input: _Optional[_Mapping[str, str]] = ..., map_any: _Optional[_Mapping[str, _any_pb2.Any]] = ...) -> None: ...

class MapOut(_message.Message):
    __slots__ = ("map1", "map2", "map3", "map4", "bar")
    class Map1Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapM
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapM, _Mapping]] = ...) -> None: ...
    class Map2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapOut
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapOut, _Mapping]] = ...) -> None: ...
    class Map3Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Map4Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: str
        def __init__(self, key: bool = ..., value: _Optional[str] = ...) -> None: ...
    MAP1_FIELD_NUMBER: _ClassVar[int]
    MAP2_FIELD_NUMBER: _ClassVar[int]
    MAP3_FIELD_NUMBER: _ClassVar[int]
    MAP4_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    map1: _containers.MessageMap[str, MapM]
    map2: _containers.MessageMap[str, MapOut]
    map3: _containers.ScalarMap[int, str]
    map4: _containers.ScalarMap[bool, str]
    bar: str
    def __init__(self, map1: _Optional[_Mapping[str, MapM]] = ..., map2: _Optional[_Mapping[str, MapOut]] = ..., map3: _Optional[_Mapping[int, str]] = ..., map4: _Optional[_Mapping[bool, str]] = ..., bar: _Optional[str] = ...) -> None: ...

class MapOutWireFormat(_message.Message):
    __slots__ = ("map1", "map2", "map3", "map4", "bar")
    class Map1Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapM
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapM, _Mapping]] = ...) -> None: ...
    class Map2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapOut
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapOut, _Mapping]] = ...) -> None: ...
    class Map3Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Map4Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: str
        def __init__(self, key: bool = ..., value: _Optional[str] = ...) -> None: ...
    MAP1_FIELD_NUMBER: _ClassVar[int]
    MAP2_FIELD_NUMBER: _ClassVar[int]
    MAP3_FIELD_NUMBER: _ClassVar[int]
    MAP4_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    map1: _containers.RepeatedCompositeFieldContainer[MapOutWireFormat.Map1Entry]
    map2: _containers.RepeatedCompositeFieldContainer[MapOutWireFormat.Map2Entry]
    map3: _containers.RepeatedCompositeFieldContainer[MapOutWireFormat.Map3Entry]
    map4: _containers.RepeatedCompositeFieldContainer[MapOutWireFormat.Map4Entry]
    bar: str
    def __init__(self, map1: _Optional[_Iterable[_Union[MapOutWireFormat.Map1Entry, _Mapping]]] = ..., map2: _Optional[_Iterable[_Union[MapOutWireFormat.Map2Entry, _Mapping]]] = ..., map3: _Optional[_Iterable[_Union[MapOutWireFormat.Map3Entry, _Mapping]]] = ..., map4: _Optional[_Iterable[_Union[MapOutWireFormat.Map4Entry, _Mapping]]] = ..., bar: _Optional[str] = ...) -> None: ...

class MapM(_message.Message):
    __slots__ = ("foo",)
    FOO_FIELD_NUMBER: _ClassVar[int]
    foo: str
    def __init__(self, foo: _Optional[str] = ...) -> None: ...
