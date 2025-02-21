from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROTOCOL: _ClassVar[EnumValue]
    BUFFER: _ClassVar[EnumValue]
    DEFAULT: _ClassVar[EnumValue]
PROTOCOL: EnumValue
BUFFER: EnumValue
DEFAULT: EnumValue

class TestFlagsAndStrings(_message.Message):
    __slots__ = ("A", "repeatedgroup")
    class RepeatedGroup(_message.Message):
        __slots__ = ("f",)
        F_FIELD_NUMBER: _ClassVar[int]
        f: str
        def __init__(self, f: _Optional[str] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    REPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
    A: int
    repeatedgroup: _containers.RepeatedCompositeFieldContainer[TestFlagsAndStrings.RepeatedGroup]
    def __init__(self, A: _Optional[int] = ..., repeatedgroup: _Optional[_Iterable[_Union[TestFlagsAndStrings.RepeatedGroup, _Mapping]]] = ...) -> None: ...

class TestBase64ByteArrays(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: bytes
    def __init__(self, a: _Optional[bytes] = ...) -> None: ...

class TestJavaScriptJSON(_message.Message):
    __slots__ = ("a", "final", "Var")
    A_FIELD_NUMBER: _ClassVar[int]
    FINAL_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    a: int
    final: float
    Var: str
    def __init__(self, a: _Optional[int] = ..., final: _Optional[float] = ..., Var: _Optional[str] = ..., **kwargs) -> None: ...

class TestJavaScriptOrderJSON1(_message.Message):
    __slots__ = ("d", "c", "x", "b", "a")
    D_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    d: int
    c: int
    x: bool
    b: int
    a: int
    def __init__(self, d: _Optional[int] = ..., c: _Optional[int] = ..., x: bool = ..., b: _Optional[int] = ..., a: _Optional[int] = ...) -> None: ...

class TestJavaScriptOrderJSON2(_message.Message):
    __slots__ = ("d", "c", "x", "b", "a", "z")
    D_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    d: int
    c: int
    x: bool
    b: int
    a: int
    z: _containers.RepeatedCompositeFieldContainer[TestJavaScriptOrderJSON1]
    def __init__(self, d: _Optional[int] = ..., c: _Optional[int] = ..., x: bool = ..., b: _Optional[int] = ..., a: _Optional[int] = ..., z: _Optional[_Iterable[_Union[TestJavaScriptOrderJSON1, _Mapping]]] = ...) -> None: ...

class TestLargeInt(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...

class TestNumbers(_message.Message):
    __slots__ = ("a", "b", "c", "d", "e", "f")
    class MyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OK: _ClassVar[TestNumbers.MyType]
        WARNING: _ClassVar[TestNumbers.MyType]
        ERROR: _ClassVar[TestNumbers.MyType]
    OK: TestNumbers.MyType
    WARNING: TestNumbers.MyType
    ERROR: TestNumbers.MyType
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    F_FIELD_NUMBER: _ClassVar[int]
    a: TestNumbers.MyType
    b: int
    c: float
    d: bool
    e: float
    f: int
    def __init__(self, a: _Optional[_Union[TestNumbers.MyType, str]] = ..., b: _Optional[int] = ..., c: _Optional[float] = ..., d: bool = ..., e: _Optional[float] = ..., f: _Optional[int] = ...) -> None: ...

class TestCamelCase(_message.Message):
    __slots__ = ("normal_field", "CAPITAL_FIELD", "CamelCaseField")
    NORMAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    CAPITAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    CAMELCASEFIELD_FIELD_NUMBER: _ClassVar[int]
    normal_field: str
    CAPITAL_FIELD: int
    CamelCaseField: int
    def __init__(self, normal_field: _Optional[str] = ..., CAPITAL_FIELD: _Optional[int] = ..., CamelCaseField: _Optional[int] = ...) -> None: ...

class TestBoolMap(_message.Message):
    __slots__ = ("bool_map",)
    class BoolMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: int
        def __init__(self, key: bool = ..., value: _Optional[int] = ...) -> None: ...
    BOOL_MAP_FIELD_NUMBER: _ClassVar[int]
    bool_map: _containers.ScalarMap[bool, int]
    def __init__(self, bool_map: _Optional[_Mapping[bool, int]] = ...) -> None: ...

class TestRecursion(_message.Message):
    __slots__ = ("value", "child")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    value: int
    child: TestRecursion
    def __init__(self, value: _Optional[int] = ..., child: _Optional[_Union[TestRecursion, _Mapping]] = ...) -> None: ...

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

class TestStringSerializer(_message.Message):
    __slots__ = ("scalar_string", "repeated_string", "string_map")
    class StringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCALAR_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    scalar_string: str
    repeated_string: _containers.RepeatedScalarFieldContainer[str]
    string_map: _containers.ScalarMap[str, str]
    def __init__(self, scalar_string: _Optional[str] = ..., repeated_string: _Optional[_Iterable[str]] = ..., string_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TestMessageWithExtension(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestExtension(_message.Message):
    __slots__ = ("value",)
    EXT_FIELD_NUMBER: _ClassVar[int]
    ext: _descriptor.FieldDescriptor
    ENUM_EXT_FIELD_NUMBER: _ClassVar[int]
    enum_ext: _descriptor.FieldDescriptor
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class TestDefaultEnumValue(_message.Message):
    __slots__ = ("enum_value",)
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    enum_value: EnumValue
    def __init__(self, enum_value: _Optional[_Union[EnumValue, str]] = ...) -> None: ...

class TestMapOfEnums(_message.Message):
    __slots__ = ("enum_map",)
    class EnumMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EnumValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EnumValue, str]] = ...) -> None: ...
    ENUM_MAP_FIELD_NUMBER: _ClassVar[int]
    enum_map: _containers.ScalarMap[str, EnumValue]
    def __init__(self, enum_map: _Optional[_Mapping[str, EnumValue]] = ...) -> None: ...

class TestRepeatedEnum(_message.Message):
    __slots__ = ("repeated_enum",)
    REPEATED_ENUM_FIELD_NUMBER: _ClassVar[int]
    repeated_enum: _containers.RepeatedScalarFieldContainer[EnumValue]
    def __init__(self, repeated_enum: _Optional[_Iterable[_Union[EnumValue, str]]] = ...) -> None: ...
