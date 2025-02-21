from google.protobuf import unittest_pb2 as _unittest_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAP_ENUM_FOO: _ClassVar[MapEnum]
    MAP_ENUM_BAR: _ClassVar[MapEnum]
    MAP_ENUM_BAZ: _ClassVar[MapEnum]
MAP_ENUM_FOO: MapEnum
MAP_ENUM_BAR: MapEnum
MAP_ENUM_BAZ: MapEnum

class TestMap(_message.Message):
    __slots__ = ("map_int32_int32", "map_int64_int64", "map_uint32_uint32", "map_uint64_uint64", "map_sint32_sint32", "map_sint64_sint64", "map_fixed32_fixed32", "map_fixed64_fixed64", "map_sfixed32_sfixed32", "map_sfixed64_sfixed64", "map_int32_float", "map_int32_double", "map_bool_bool", "map_string_string", "map_int32_bytes", "map_int32_enum", "map_int32_foreign_message", "map_string_foreign_message", "map_int32_all_types")
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
    class MapInt32BytesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    class MapInt32EnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MapEnum, str]] = ...) -> None: ...
    class MapInt32ForeignMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.ForeignMessage
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.ForeignMessage, _Mapping]] = ...) -> None: ...
    class MapStringForeignMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _unittest_pb2.ForeignMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_unittest_pb2.ForeignMessage, _Mapping]] = ...) -> None: ...
    class MapInt32AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
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
    MAP_INT32_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
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
    map_int32_bytes: _containers.ScalarMap[int, bytes]
    map_int32_enum: _containers.ScalarMap[int, MapEnum]
    map_int32_foreign_message: _containers.MessageMap[int, _unittest_pb2.ForeignMessage]
    map_string_foreign_message: _containers.MessageMap[str, _unittest_pb2.ForeignMessage]
    map_int32_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    def __init__(self, map_int32_int32: _Optional[_Mapping[int, int]] = ..., map_int64_int64: _Optional[_Mapping[int, int]] = ..., map_uint32_uint32: _Optional[_Mapping[int, int]] = ..., map_uint64_uint64: _Optional[_Mapping[int, int]] = ..., map_sint32_sint32: _Optional[_Mapping[int, int]] = ..., map_sint64_sint64: _Optional[_Mapping[int, int]] = ..., map_fixed32_fixed32: _Optional[_Mapping[int, int]] = ..., map_fixed64_fixed64: _Optional[_Mapping[int, int]] = ..., map_sfixed32_sfixed32: _Optional[_Mapping[int, int]] = ..., map_sfixed64_sfixed64: _Optional[_Mapping[int, int]] = ..., map_int32_float: _Optional[_Mapping[int, float]] = ..., map_int32_double: _Optional[_Mapping[int, float]] = ..., map_bool_bool: _Optional[_Mapping[bool, bool]] = ..., map_string_string: _Optional[_Mapping[str, str]] = ..., map_int32_bytes: _Optional[_Mapping[int, bytes]] = ..., map_int32_enum: _Optional[_Mapping[int, MapEnum]] = ..., map_int32_foreign_message: _Optional[_Mapping[int, _unittest_pb2.ForeignMessage]] = ..., map_string_foreign_message: _Optional[_Mapping[str, _unittest_pb2.ForeignMessage]] = ..., map_int32_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ...) -> None: ...

class TestMapWithMessages(_message.Message):
    __slots__ = ("map_int32_all_types", "map_int64_all_types", "map_uint32_all_types", "map_uint64_all_types", "map_sint32_all_types", "map_sint64_all_types", "map_fixed32_all_types", "map_fixed64_all_types", "map_sfixed32_all_types", "map_sfixed64_all_types", "map_bool_all_types", "map_string_all_types")
    class MapInt32AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapInt64AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapUint32AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapUint64AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapSint32AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapSint64AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapFixed32AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapFixed64AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapSfixed32AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapSfixed64AllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapBoolAllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: bool = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    class MapStringAllTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    MAP_INT32_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_INT64_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_UINT32_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_UINT64_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_SINT32_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_SINT64_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_FIXED32_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_FIXED64_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_SFIXED32_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_SFIXED64_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_BOOL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    map_int32_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_int64_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_uint32_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_uint64_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_sint32_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_sint64_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_fixed32_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_fixed64_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_sfixed32_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_sfixed64_all_types: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    map_bool_all_types: _containers.MessageMap[bool, _unittest_pb2.TestAllTypes]
    map_string_all_types: _containers.MessageMap[str, _unittest_pb2.TestAllTypes]
    def __init__(self, map_int32_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_int64_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_uint32_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_uint64_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_sint32_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_sint64_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_fixed32_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_fixed64_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_sfixed32_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_sfixed64_all_types: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ..., map_bool_all_types: _Optional[_Mapping[bool, _unittest_pb2.TestAllTypes]] = ..., map_string_all_types: _Optional[_Mapping[str, _unittest_pb2.TestAllTypes]] = ...) -> None: ...

class TestMapSubmessage(_message.Message):
    __slots__ = ("test_map",)
    TEST_MAP_FIELD_NUMBER: _ClassVar[int]
    test_map: TestMap
    def __init__(self, test_map: _Optional[_Union[TestMap, _Mapping]] = ...) -> None: ...

class TestMessageMap(_message.Message):
    __slots__ = ("map_int32_message",)
    class MapInt32MessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestAllTypes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestAllTypes, _Mapping]] = ...) -> None: ...
    MAP_INT32_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    map_int32_message: _containers.MessageMap[int, _unittest_pb2.TestAllTypes]
    def __init__(self, map_int32_message: _Optional[_Mapping[int, _unittest_pb2.TestAllTypes]] = ...) -> None: ...

class TestSameTypeMap(_message.Message):
    __slots__ = ("map1", "map2")
    class Map1Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Map2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MAP1_FIELD_NUMBER: _ClassVar[int]
    MAP2_FIELD_NUMBER: _ClassVar[int]
    map1: _containers.ScalarMap[int, int]
    map2: _containers.ScalarMap[int, int]
    def __init__(self, map1: _Optional[_Mapping[int, int]] = ..., map2: _Optional[_Mapping[int, int]] = ...) -> None: ...

class TestRequiredMessageMap(_message.Message):
    __slots__ = ("map_field",)
    class MapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.TestRequired
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.TestRequired, _Mapping]] = ...) -> None: ...
    MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    map_field: _containers.MessageMap[int, _unittest_pb2.TestRequired]
    def __init__(self, map_field: _Optional[_Mapping[int, _unittest_pb2.TestRequired]] = ...) -> None: ...

class TestArenaMap(_message.Message):
    __slots__ = ("map_int32_int32", "map_int64_int64", "map_uint32_uint32", "map_uint64_uint64", "map_sint32_sint32", "map_sint64_sint64", "map_fixed32_fixed32", "map_fixed64_fixed64", "map_sfixed32_sfixed32", "map_sfixed64_sfixed64", "map_int32_float", "map_int32_double", "map_bool_bool", "map_string_string", "map_int32_bytes", "map_int32_enum", "map_int32_foreign_message")
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
    class MapInt32BytesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    class MapInt32EnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MapEnum, str]] = ...) -> None: ...
    class MapInt32ForeignMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_pb2.ForeignMessage
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_pb2.ForeignMessage, _Mapping]] = ...) -> None: ...
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
    MAP_INT32_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
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
    map_int32_bytes: _containers.ScalarMap[int, bytes]
    map_int32_enum: _containers.ScalarMap[int, MapEnum]
    map_int32_foreign_message: _containers.MessageMap[int, _unittest_pb2.ForeignMessage]
    def __init__(self, map_int32_int32: _Optional[_Mapping[int, int]] = ..., map_int64_int64: _Optional[_Mapping[int, int]] = ..., map_uint32_uint32: _Optional[_Mapping[int, int]] = ..., map_uint64_uint64: _Optional[_Mapping[int, int]] = ..., map_sint32_sint32: _Optional[_Mapping[int, int]] = ..., map_sint64_sint64: _Optional[_Mapping[int, int]] = ..., map_fixed32_fixed32: _Optional[_Mapping[int, int]] = ..., map_fixed64_fixed64: _Optional[_Mapping[int, int]] = ..., map_sfixed32_sfixed32: _Optional[_Mapping[int, int]] = ..., map_sfixed64_sfixed64: _Optional[_Mapping[int, int]] = ..., map_int32_float: _Optional[_Mapping[int, float]] = ..., map_int32_double: _Optional[_Mapping[int, float]] = ..., map_bool_bool: _Optional[_Mapping[bool, bool]] = ..., map_string_string: _Optional[_Mapping[str, str]] = ..., map_int32_bytes: _Optional[_Mapping[int, bytes]] = ..., map_int32_enum: _Optional[_Mapping[int, MapEnum]] = ..., map_int32_foreign_message: _Optional[_Mapping[int, _unittest_pb2.ForeignMessage]] = ...) -> None: ...

class MessageContainingEnumCalledType(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_FOO: _ClassVar[MessageContainingEnumCalledType.Type]
    TYPE_FOO: MessageContainingEnumCalledType.Type
    class TypeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MessageContainingEnumCalledType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MessageContainingEnumCalledType, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _containers.MessageMap[str, MessageContainingEnumCalledType]
    def __init__(self, type: _Optional[_Mapping[str, MessageContainingEnumCalledType]] = ...) -> None: ...

class MessageContainingMapCalledEntry(_message.Message):
    __slots__ = ("entry",)
    class EntryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.ScalarMap[int, int]
    def __init__(self, entry: _Optional[_Mapping[int, int]] = ...) -> None: ...

class TestRecursiveMapMessage(_message.Message):
    __slots__ = ("a",)
    class AEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestRecursiveMapMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestRecursiveMapMessage, _Mapping]] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    a: _containers.MessageMap[str, TestRecursiveMapMessage]
    def __init__(self, a: _Optional[_Mapping[str, TestRecursiveMapMessage]] = ...) -> None: ...

class TestI32StrMap(_message.Message):
    __slots__ = ("m_32_str",)
    class M32StrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    M_32_STR_FIELD_NUMBER: _ClassVar[int]
    m_32_str: _containers.ScalarMap[int, str]
    def __init__(self, m_32_str: _Optional[_Mapping[int, str]] = ...) -> None: ...
