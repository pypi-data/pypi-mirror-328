from google.protobuf import unittest_import_pb2 as _unittest_import_pb2
from google.protobuf import unittest_import_public_pb2 as _unittest_import_public_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Proto2MapEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROTO2_MAP_ENUM_FOO: _ClassVar[Proto2MapEnum]
    PROTO2_MAP_ENUM_BAR: _ClassVar[Proto2MapEnum]
    PROTO2_MAP_ENUM_BAZ: _ClassVar[Proto2MapEnum]

class Proto2MapEnumPlusExtra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    E_PROTO2_MAP_ENUM_FOO: _ClassVar[Proto2MapEnumPlusExtra]
    E_PROTO2_MAP_ENUM_BAR: _ClassVar[Proto2MapEnumPlusExtra]
    E_PROTO2_MAP_ENUM_BAZ: _ClassVar[Proto2MapEnumPlusExtra]
    E_PROTO2_MAP_ENUM_EXTRA: _ClassVar[Proto2MapEnumPlusExtra]
PROTO2_MAP_ENUM_FOO: Proto2MapEnum
PROTO2_MAP_ENUM_BAR: Proto2MapEnum
PROTO2_MAP_ENUM_BAZ: Proto2MapEnum
E_PROTO2_MAP_ENUM_FOO: Proto2MapEnumPlusExtra
E_PROTO2_MAP_ENUM_BAR: Proto2MapEnumPlusExtra
E_PROTO2_MAP_ENUM_BAZ: Proto2MapEnumPlusExtra
E_PROTO2_MAP_ENUM_EXTRA: Proto2MapEnumPlusExtra

class TestEnumMap(_message.Message):
    __slots__ = ("known_map_field", "unknown_map_field", "unknown_map_field_int64", "unknown_map_field_uint64", "unknown_map_field_int32", "unknown_map_field_uint32", "unknown_map_field_fixed32", "unknown_map_field_fixed64", "unknown_map_field_bool", "unknown_map_field_string", "unknown_map_field_sint32", "unknown_map_field_sint64", "unknown_map_field_sfixed32", "unknown_map_field_sfixed64")
    class KnownMapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldInt64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldUint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldInt32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldUint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldFixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldFixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldBoolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: Proto2MapEnum
        def __init__(self, key: bool = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Proto2MapEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldSint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldSint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldSfixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    class UnknownMapFieldSfixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnum, str]] = ...) -> None: ...
    KNOWN_MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_INT64_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_UINT64_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_INT32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_UINT32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_FIXED32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_FIXED64_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_BOOL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_STRING_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_SINT32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_SINT64_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    known_map_field: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_int64: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_uint64: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_int32: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_uint32: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_fixed32: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_fixed64: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_bool: _containers.ScalarMap[bool, Proto2MapEnum]
    unknown_map_field_string: _containers.ScalarMap[str, Proto2MapEnum]
    unknown_map_field_sint32: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_sint64: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_sfixed32: _containers.ScalarMap[int, Proto2MapEnum]
    unknown_map_field_sfixed64: _containers.ScalarMap[int, Proto2MapEnum]
    def __init__(self, known_map_field: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_int64: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_uint64: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_int32: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_uint32: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_fixed32: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_fixed64: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_bool: _Optional[_Mapping[bool, Proto2MapEnum]] = ..., unknown_map_field_string: _Optional[_Mapping[str, Proto2MapEnum]] = ..., unknown_map_field_sint32: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_sint64: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_sfixed32: _Optional[_Mapping[int, Proto2MapEnum]] = ..., unknown_map_field_sfixed64: _Optional[_Mapping[int, Proto2MapEnum]] = ...) -> None: ...

class TestEnumMapPlusExtra(_message.Message):
    __slots__ = ("known_map_field", "unknown_map_field", "unknown_map_field_int64", "unknown_map_field_uint64", "unknown_map_field_int32", "unknown_map_field_uint32", "unknown_map_field_fixed32", "unknown_map_field_fixed64", "unknown_map_field_bool", "unknown_map_field_string", "unknown_map_field_sint32", "unknown_map_field_sint64", "unknown_map_field_sfixed32", "unknown_map_field_sfixed64")
    class KnownMapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldInt64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldUint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldInt32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldUint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldFixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldFixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldBoolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: bool = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldSint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldSint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldSfixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    class UnknownMapFieldSfixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Proto2MapEnumPlusExtra
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Proto2MapEnumPlusExtra, str]] = ...) -> None: ...
    KNOWN_MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_INT64_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_UINT64_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_INT32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_UINT32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_FIXED32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_FIXED64_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_BOOL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_STRING_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_SINT32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_SINT64_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MAP_FIELD_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    known_map_field: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_int64: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_uint64: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_int32: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_uint32: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_fixed32: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_fixed64: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_bool: _containers.ScalarMap[bool, Proto2MapEnumPlusExtra]
    unknown_map_field_string: _containers.ScalarMap[str, Proto2MapEnumPlusExtra]
    unknown_map_field_sint32: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_sint64: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_sfixed32: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    unknown_map_field_sfixed64: _containers.ScalarMap[int, Proto2MapEnumPlusExtra]
    def __init__(self, known_map_field: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_int64: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_uint64: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_int32: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_uint32: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_fixed32: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_fixed64: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_bool: _Optional[_Mapping[bool, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_string: _Optional[_Mapping[str, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_sint32: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_sint64: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_sfixed32: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ..., unknown_map_field_sfixed64: _Optional[_Mapping[int, Proto2MapEnumPlusExtra]] = ...) -> None: ...

class TestImportEnumMap(_message.Message):
    __slots__ = ("import_enum_amp",)
    class ImportEnumAmpEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _unittest_import_pb2.ImportEnumForMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_unittest_import_pb2.ImportEnumForMap, str]] = ...) -> None: ...
    IMPORT_ENUM_AMP_FIELD_NUMBER: _ClassVar[int]
    import_enum_amp: _containers.ScalarMap[int, _unittest_import_pb2.ImportEnumForMap]
    def __init__(self, import_enum_amp: _Optional[_Mapping[int, _unittest_import_pb2.ImportEnumForMap]] = ...) -> None: ...

class TestIntIntMap(_message.Message):
    __slots__ = ("m",)
    class MEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    M_FIELD_NUMBER: _ClassVar[int]
    m: _containers.ScalarMap[int, int]
    def __init__(self, m: _Optional[_Mapping[int, int]] = ...) -> None: ...

class TestMaps(_message.Message):
    __slots__ = ("m_int32", "m_int64", "m_uint32", "m_uint64", "m_sint32", "m_sint64", "m_fixed32", "m_fixed64", "m_sfixed32", "m_sfixed64", "m_bool", "m_string")
    class MInt32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MInt64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MUint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MUint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MSint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MSint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MFixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MFixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MSfixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MSfixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestIntIntMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MBoolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: TestIntIntMap
        def __init__(self, key: bool = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    class MStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestIntIntMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestIntIntMap, _Mapping]] = ...) -> None: ...
    M_INT32_FIELD_NUMBER: _ClassVar[int]
    M_INT64_FIELD_NUMBER: _ClassVar[int]
    M_UINT32_FIELD_NUMBER: _ClassVar[int]
    M_UINT64_FIELD_NUMBER: _ClassVar[int]
    M_SINT32_FIELD_NUMBER: _ClassVar[int]
    M_SINT64_FIELD_NUMBER: _ClassVar[int]
    M_FIXED32_FIELD_NUMBER: _ClassVar[int]
    M_FIXED64_FIELD_NUMBER: _ClassVar[int]
    M_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    M_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    M_BOOL_FIELD_NUMBER: _ClassVar[int]
    M_STRING_FIELD_NUMBER: _ClassVar[int]
    m_int32: _containers.MessageMap[int, TestIntIntMap]
    m_int64: _containers.MessageMap[int, TestIntIntMap]
    m_uint32: _containers.MessageMap[int, TestIntIntMap]
    m_uint64: _containers.MessageMap[int, TestIntIntMap]
    m_sint32: _containers.MessageMap[int, TestIntIntMap]
    m_sint64: _containers.MessageMap[int, TestIntIntMap]
    m_fixed32: _containers.MessageMap[int, TestIntIntMap]
    m_fixed64: _containers.MessageMap[int, TestIntIntMap]
    m_sfixed32: _containers.MessageMap[int, TestIntIntMap]
    m_sfixed64: _containers.MessageMap[int, TestIntIntMap]
    m_bool: _containers.MessageMap[bool, TestIntIntMap]
    m_string: _containers.MessageMap[str, TestIntIntMap]
    def __init__(self, m_int32: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_int64: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_uint32: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_uint64: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_sint32: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_sint64: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_fixed32: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_fixed64: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_sfixed32: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_sfixed64: _Optional[_Mapping[int, TestIntIntMap]] = ..., m_bool: _Optional[_Mapping[bool, TestIntIntMap]] = ..., m_string: _Optional[_Mapping[str, TestIntIntMap]] = ...) -> None: ...

class TestSubmessageMaps(_message.Message):
    __slots__ = ("m",)
    M_FIELD_NUMBER: _ClassVar[int]
    m: TestMaps
    def __init__(self, m: _Optional[_Union[TestMaps, _Mapping]] = ...) -> None: ...

class TestProto2BytesMap(_message.Message):
    __slots__ = ("map_bytes", "map_string")
    class MapBytesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    class MapStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    MAP_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_FIELD_NUMBER: _ClassVar[int]
    map_bytes: _containers.ScalarMap[int, bytes]
    map_string: _containers.ScalarMap[int, str]
    def __init__(self, map_bytes: _Optional[_Mapping[int, bytes]] = ..., map_string: _Optional[_Mapping[int, str]] = ...) -> None: ...
