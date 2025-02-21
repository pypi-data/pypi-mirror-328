from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestProto3BytesMap(_message.Message):
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
