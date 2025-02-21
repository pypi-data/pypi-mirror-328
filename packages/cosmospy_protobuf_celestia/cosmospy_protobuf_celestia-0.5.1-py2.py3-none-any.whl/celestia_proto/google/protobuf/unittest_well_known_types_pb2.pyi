from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import api_pb2 as _api_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import source_context_pb2 as _source_context_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import type_pb2 as _type_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestWellKnownTypes(_message.Message):
    __slots__ = ("any_field", "api_field", "duration_field", "empty_field", "field_mask_field", "source_context_field", "struct_field", "timestamp_field", "type_field", "double_field", "float_field", "int64_field", "uint64_field", "int32_field", "uint32_field", "bool_field", "string_field", "bytes_field", "value_field")
    ANY_FIELD_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_FIELD_NUMBER: _ClassVar[int]
    any_field: _any_pb2.Any
    api_field: _api_pb2.Api
    duration_field: _duration_pb2.Duration
    empty_field: _empty_pb2.Empty
    field_mask_field: _field_mask_pb2.FieldMask
    source_context_field: _source_context_pb2.SourceContext
    struct_field: _struct_pb2.Struct
    timestamp_field: _timestamp_pb2.Timestamp
    type_field: _type_pb2.Type
    double_field: _wrappers_pb2.DoubleValue
    float_field: _wrappers_pb2.FloatValue
    int64_field: _wrappers_pb2.Int64Value
    uint64_field: _wrappers_pb2.UInt64Value
    int32_field: _wrappers_pb2.Int32Value
    uint32_field: _wrappers_pb2.UInt32Value
    bool_field: _wrappers_pb2.BoolValue
    string_field: _wrappers_pb2.StringValue
    bytes_field: _wrappers_pb2.BytesValue
    value_field: _struct_pb2.Value
    def __init__(self, any_field: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., api_field: _Optional[_Union[_api_pb2.Api, _Mapping]] = ..., duration_field: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., empty_field: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., field_mask_field: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., source_context_field: _Optional[_Union[_source_context_pb2.SourceContext, _Mapping]] = ..., struct_field: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., timestamp_field: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type_field: _Optional[_Union[_type_pb2.Type, _Mapping]] = ..., double_field: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., float_field: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., int64_field: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., uint64_field: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., int32_field: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., uint32_field: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., bool_field: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., string_field: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., bytes_field: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., value_field: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class RepeatedWellKnownTypes(_message.Message):
    __slots__ = ("any_field", "api_field", "duration_field", "empty_field", "field_mask_field", "source_context_field", "struct_field", "timestamp_field", "type_field", "double_field", "float_field", "int64_field", "uint64_field", "int32_field", "uint32_field", "bool_field", "string_field", "bytes_field")
    ANY_FIELD_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    any_field: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    api_field: _containers.RepeatedCompositeFieldContainer[_api_pb2.Api]
    duration_field: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    empty_field: _containers.RepeatedCompositeFieldContainer[_empty_pb2.Empty]
    field_mask_field: _containers.RepeatedCompositeFieldContainer[_field_mask_pb2.FieldMask]
    source_context_field: _containers.RepeatedCompositeFieldContainer[_source_context_pb2.SourceContext]
    struct_field: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    timestamp_field: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    type_field: _containers.RepeatedCompositeFieldContainer[_type_pb2.Type]
    double_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.DoubleValue]
    float_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.FloatValue]
    int64_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
    uint64_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt64Value]
    int32_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int32Value]
    uint32_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt32Value]
    bool_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BoolValue]
    string_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    bytes_field: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BytesValue]
    def __init__(self, any_field: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., api_field: _Optional[_Iterable[_Union[_api_pb2.Api, _Mapping]]] = ..., duration_field: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]] = ..., empty_field: _Optional[_Iterable[_Union[_empty_pb2.Empty, _Mapping]]] = ..., field_mask_field: _Optional[_Iterable[_Union[_field_mask_pb2.FieldMask, _Mapping]]] = ..., source_context_field: _Optional[_Iterable[_Union[_source_context_pb2.SourceContext, _Mapping]]] = ..., struct_field: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., timestamp_field: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ..., type_field: _Optional[_Iterable[_Union[_type_pb2.Type, _Mapping]]] = ..., double_field: _Optional[_Iterable[_Union[_wrappers_pb2.DoubleValue, _Mapping]]] = ..., float_field: _Optional[_Iterable[_Union[_wrappers_pb2.FloatValue, _Mapping]]] = ..., int64_field: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ..., uint64_field: _Optional[_Iterable[_Union[_wrappers_pb2.UInt64Value, _Mapping]]] = ..., int32_field: _Optional[_Iterable[_Union[_wrappers_pb2.Int32Value, _Mapping]]] = ..., uint32_field: _Optional[_Iterable[_Union[_wrappers_pb2.UInt32Value, _Mapping]]] = ..., bool_field: _Optional[_Iterable[_Union[_wrappers_pb2.BoolValue, _Mapping]]] = ..., string_field: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., bytes_field: _Optional[_Iterable[_Union[_wrappers_pb2.BytesValue, _Mapping]]] = ...) -> None: ...

class OneofWellKnownTypes(_message.Message):
    __slots__ = ("any_field", "api_field", "duration_field", "empty_field", "field_mask_field", "source_context_field", "struct_field", "timestamp_field", "type_field", "double_field", "float_field", "int64_field", "uint64_field", "int32_field", "uint32_field", "bool_field", "string_field", "bytes_field")
    ANY_FIELD_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    any_field: _any_pb2.Any
    api_field: _api_pb2.Api
    duration_field: _duration_pb2.Duration
    empty_field: _empty_pb2.Empty
    field_mask_field: _field_mask_pb2.FieldMask
    source_context_field: _source_context_pb2.SourceContext
    struct_field: _struct_pb2.Struct
    timestamp_field: _timestamp_pb2.Timestamp
    type_field: _type_pb2.Type
    double_field: _wrappers_pb2.DoubleValue
    float_field: _wrappers_pb2.FloatValue
    int64_field: _wrappers_pb2.Int64Value
    uint64_field: _wrappers_pb2.UInt64Value
    int32_field: _wrappers_pb2.Int32Value
    uint32_field: _wrappers_pb2.UInt32Value
    bool_field: _wrappers_pb2.BoolValue
    string_field: _wrappers_pb2.StringValue
    bytes_field: _wrappers_pb2.BytesValue
    def __init__(self, any_field: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., api_field: _Optional[_Union[_api_pb2.Api, _Mapping]] = ..., duration_field: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., empty_field: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., field_mask_field: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., source_context_field: _Optional[_Union[_source_context_pb2.SourceContext, _Mapping]] = ..., struct_field: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., timestamp_field: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type_field: _Optional[_Union[_type_pb2.Type, _Mapping]] = ..., double_field: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., float_field: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., int64_field: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., uint64_field: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., int32_field: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., uint32_field: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., bool_field: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., string_field: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., bytes_field: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class MapWellKnownTypes(_message.Message):
    __slots__ = ("any_field", "api_field", "duration_field", "empty_field", "field_mask_field", "source_context_field", "struct_field", "timestamp_field", "type_field", "double_field", "float_field", "int64_field", "uint64_field", "int32_field", "uint32_field", "bool_field", "string_field", "bytes_field")
    class AnyFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _any_pb2.Any
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    class ApiFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _api_pb2.Api
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_api_pb2.Api, _Mapping]] = ...) -> None: ...
    class DurationFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _duration_pb2.Duration
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class EmptyFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _empty_pb2.Empty
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...
    class FieldMaskFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _field_mask_pb2.FieldMask
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    class SourceContextFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _source_context_pb2.SourceContext
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_source_context_pb2.SourceContext, _Mapping]] = ...) -> None: ...
    class StructFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _struct_pb2.Struct
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    class TimestampFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _timestamp_pb2.Timestamp
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class TypeFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _type_pb2.Type
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_type_pb2.Type, _Mapping]] = ...) -> None: ...
    class DoubleFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.DoubleValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
    class FloatFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.FloatValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...
    class Int64FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.Int64Value
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
    class Uint64FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.UInt64Value
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ...) -> None: ...
    class Int32FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.Int32Value
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
    class Uint32FieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.UInt32Value
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
    class BoolFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.BoolValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class StringFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.StringValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    class BytesFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _wrappers_pb2.BytesValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...
    ANY_FIELD_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    any_field: _containers.MessageMap[int, _any_pb2.Any]
    api_field: _containers.MessageMap[int, _api_pb2.Api]
    duration_field: _containers.MessageMap[int, _duration_pb2.Duration]
    empty_field: _containers.MessageMap[int, _empty_pb2.Empty]
    field_mask_field: _containers.MessageMap[int, _field_mask_pb2.FieldMask]
    source_context_field: _containers.MessageMap[int, _source_context_pb2.SourceContext]
    struct_field: _containers.MessageMap[int, _struct_pb2.Struct]
    timestamp_field: _containers.MessageMap[int, _timestamp_pb2.Timestamp]
    type_field: _containers.MessageMap[int, _type_pb2.Type]
    double_field: _containers.MessageMap[int, _wrappers_pb2.DoubleValue]
    float_field: _containers.MessageMap[int, _wrappers_pb2.FloatValue]
    int64_field: _containers.MessageMap[int, _wrappers_pb2.Int64Value]
    uint64_field: _containers.MessageMap[int, _wrappers_pb2.UInt64Value]
    int32_field: _containers.MessageMap[int, _wrappers_pb2.Int32Value]
    uint32_field: _containers.MessageMap[int, _wrappers_pb2.UInt32Value]
    bool_field: _containers.MessageMap[int, _wrappers_pb2.BoolValue]
    string_field: _containers.MessageMap[int, _wrappers_pb2.StringValue]
    bytes_field: _containers.MessageMap[int, _wrappers_pb2.BytesValue]
    def __init__(self, any_field: _Optional[_Mapping[int, _any_pb2.Any]] = ..., api_field: _Optional[_Mapping[int, _api_pb2.Api]] = ..., duration_field: _Optional[_Mapping[int, _duration_pb2.Duration]] = ..., empty_field: _Optional[_Mapping[int, _empty_pb2.Empty]] = ..., field_mask_field: _Optional[_Mapping[int, _field_mask_pb2.FieldMask]] = ..., source_context_field: _Optional[_Mapping[int, _source_context_pb2.SourceContext]] = ..., struct_field: _Optional[_Mapping[int, _struct_pb2.Struct]] = ..., timestamp_field: _Optional[_Mapping[int, _timestamp_pb2.Timestamp]] = ..., type_field: _Optional[_Mapping[int, _type_pb2.Type]] = ..., double_field: _Optional[_Mapping[int, _wrappers_pb2.DoubleValue]] = ..., float_field: _Optional[_Mapping[int, _wrappers_pb2.FloatValue]] = ..., int64_field: _Optional[_Mapping[int, _wrappers_pb2.Int64Value]] = ..., uint64_field: _Optional[_Mapping[int, _wrappers_pb2.UInt64Value]] = ..., int32_field: _Optional[_Mapping[int, _wrappers_pb2.Int32Value]] = ..., uint32_field: _Optional[_Mapping[int, _wrappers_pb2.UInt32Value]] = ..., bool_field: _Optional[_Mapping[int, _wrappers_pb2.BoolValue]] = ..., string_field: _Optional[_Mapping[int, _wrappers_pb2.StringValue]] = ..., bytes_field: _Optional[_Mapping[int, _wrappers_pb2.BytesValue]] = ...) -> None: ...
