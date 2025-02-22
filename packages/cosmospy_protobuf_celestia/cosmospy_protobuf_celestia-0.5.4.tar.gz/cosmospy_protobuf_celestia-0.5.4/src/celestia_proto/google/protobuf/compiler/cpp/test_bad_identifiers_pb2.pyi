from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class bool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    default: _ClassVar[bool]
    NOT_EQ: _ClassVar[bool]
    volatile: _ClassVar[bool]
    return: _ClassVar[bool]
default: bool
NOT_EQ: bool
volatile: bool
return: bool
UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
unknown_fields: _descriptor.FieldDescriptor
MUTABLE_UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
mutable_unknown_fields: _descriptor.FieldDescriptor
DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
descriptor: _descriptor.FieldDescriptor
DEFAULT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
default_instance: _descriptor.FieldDescriptor
SWAP_FIELD_NUMBER: _ClassVar[int]
swap: _descriptor.FieldDescriptor
VOID_FIELD_NUMBER: _ClassVar[int]
void: _descriptor.FieldDescriptor

class TestConflictingSymbolNames(_message.Message):
    __slots__ = ("input", "output", "length", "i", "new_element", "total_size", "tag", "source", "value", "file", "handle_uninterpreted", "index", "controller", "already_here", "uint8", "uint8_t", "uint16", "uint16_t", "uint32", "uint32_t", "uint64", "uint64_t", "int8", "int8_t", "int16", "int16_t", "int32", "int32_t", "int64", "int64_t", "size_t", "ssize_t", "intptr_t", "uintptr_t", "string", "memset", "cached_size", "extensions", "bit", "bits", "offsets", "reflection", "some_cord", "some_string_piece", "int", "friend", "typedecl", "auto", "do", "field_type", "is_packed", "release_length", "release_do", "target")
    Extensions: _python_message._ExtensionDict
    class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[TestConflictingSymbolNames.TestEnum]
    FOO: TestConflictingSymbolNames.TestEnum
    class BuildDescriptors(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TypeTraits(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Data1(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, data: _Optional[_Iterable[int]] = ...) -> None: ...
    class Data2(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: _containers.RepeatedScalarFieldContainer[TestConflictingSymbolNames.TestEnum]
        def __init__(self, data: _Optional[_Iterable[_Union[TestConflictingSymbolNames.TestEnum, str]]] = ...) -> None: ...
    class Data3(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, data: _Optional[_Iterable[str]] = ...) -> None: ...
    class Data4(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: _containers.RepeatedCompositeFieldContainer[TestConflictingSymbolNames.Data4]
        def __init__(self, data: _Optional[_Iterable[_Union[TestConflictingSymbolNames.Data4, _Mapping]]] = ...) -> None: ...
    class Data5(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, data: _Optional[_Iterable[str]] = ...) -> None: ...
    class Data6(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, data: _Optional[_Iterable[str]] = ...) -> None: ...
    class Cord(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class StringPiece(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class BadKnownNamesFields(_message.Message):
        __slots__ = ("unknown_fields", "mutable_unknown_fields", "descriptor", "default_instance", "swap")
        UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
        MUTABLE_UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        SWAP_FIELD_NUMBER: _ClassVar[int]
        unknown_fields: int
        mutable_unknown_fields: int
        descriptor: int
        default_instance: int
        swap: int
        def __init__(self, unknown_fields: _Optional[int] = ..., mutable_unknown_fields: _Optional[int] = ..., descriptor: _Optional[int] = ..., default_instance: _Optional[int] = ..., swap: _Optional[int] = ...) -> None: ...
    class BadKnownNamesFieldsNoStandardDescriptor(_message.Message):
        __slots__ = ("descriptor",)
        DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        descriptor: int
        def __init__(self, descriptor: _Optional[int] = ...) -> None: ...
    class BadKnownNamesTypes(_message.Message):
        __slots__ = ()
        class GetDescriptor(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetReflection(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Swap(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class UnsafeArenaSwap(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class New(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class CopyFrom(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class MergeFrom(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetMetadata(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Clear(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class IsInitialized(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        def __init__(self) -> None: ...
    class BadKnownNamesValues(_message.Message):
        __slots__ = ()
        Extensions: _python_message._ExtensionDict
        UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
        unknown_fields: _descriptor.FieldDescriptor
        MUTABLE_UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
        mutable_unknown_fields: _descriptor.FieldDescriptor
        DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        descriptor: _descriptor.FieldDescriptor
        DEFAULT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        default_instance: _descriptor.FieldDescriptor
        SWAP_FIELD_NUMBER: _ClassVar[int]
        swap: _descriptor.FieldDescriptor
        def __init__(self) -> None: ...
    class DO(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    I_FIELD_NUMBER: _ClassVar[int]
    NEW_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    HANDLE_UNINTERPRETED_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    ALREADY_HERE_FIELD_NUMBER: _ClassVar[int]
    UINT8_FIELD_NUMBER: _ClassVar[int]
    UINT8_T_FIELD_NUMBER: _ClassVar[int]
    UINT16_FIELD_NUMBER: _ClassVar[int]
    UINT16_T_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_NUMBER: _ClassVar[int]
    UINT32_T_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_NUMBER: _ClassVar[int]
    UINT64_T_FIELD_NUMBER: _ClassVar[int]
    INT8_FIELD_NUMBER: _ClassVar[int]
    INT8_T_FIELD_NUMBER: _ClassVar[int]
    INT16_FIELD_NUMBER: _ClassVar[int]
    INT16_T_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_NUMBER: _ClassVar[int]
    INT32_T_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_NUMBER: _ClassVar[int]
    INT64_T_FIELD_NUMBER: _ClassVar[int]
    SIZE_T_FIELD_NUMBER: _ClassVar[int]
    SSIZE_T_FIELD_NUMBER: _ClassVar[int]
    INTPTR_T_FIELD_NUMBER: _ClassVar[int]
    UINTPTR_T_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    MEMSET_FIELD_NUMBER: _ClassVar[int]
    CACHED_SIZE_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    BIT_FIELD_NUMBER: _ClassVar[int]
    BITS_FIELD_NUMBER: _ClassVar[int]
    OFFSETS_FIELD_NUMBER: _ClassVar[int]
    REFLECTION_FIELD_NUMBER: _ClassVar[int]
    SOME_CORD_FIELD_NUMBER: _ClassVar[int]
    SOME_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    TYPEDECL_FIELD_NUMBER: _ClassVar[int]
    AUTO_FIELD_NUMBER: _ClassVar[int]
    DO_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PACKED_FIELD_NUMBER: _ClassVar[int]
    RELEASE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DO_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    input: int
    output: int
    length: str
    i: _containers.RepeatedScalarFieldContainer[int]
    new_element: _containers.RepeatedScalarFieldContainer[str]
    total_size: int
    tag: int
    source: int
    value: int
    file: int
    handle_uninterpreted: int
    index: _containers.RepeatedScalarFieldContainer[int]
    controller: int
    already_here: int
    uint8: int
    uint8_t: int
    uint16: int
    uint16_t: int
    uint32: int
    uint32_t: int
    uint64: int
    uint64_t: int
    int8: int
    int8_t: int
    int16: int
    int16_t: int
    int32: int
    int32_t: int
    int64: int
    int64_t: int
    size_t: int
    ssize_t: int
    intptr_t: int
    uintptr_t: int
    string: str
    memset: int
    cached_size: int
    extensions: int
    bit: int
    bits: int
    offsets: int
    reflection: int
    some_cord: str
    some_string_piece: str
    int: int
    friend: int
    typedecl: int
    auto: int
    do: TestConflictingSymbolNames.DO
    field_type: int
    is_packed: bool
    release_length: str
    release_do: TestConflictingSymbolNames.DO
    target: str
    def __init__(self, input: _Optional[int] = ..., output: _Optional[int] = ..., length: _Optional[str] = ..., i: _Optional[_Iterable[int]] = ..., new_element: _Optional[_Iterable[str]] = ..., total_size: _Optional[int] = ..., tag: _Optional[int] = ..., source: _Optional[int] = ..., value: _Optional[int] = ..., file: _Optional[int] = ..., handle_uninterpreted: _Optional[int] = ..., index: _Optional[_Iterable[int]] = ..., controller: _Optional[int] = ..., already_here: _Optional[int] = ..., uint8: _Optional[int] = ..., uint8_t: _Optional[int] = ..., uint16: _Optional[int] = ..., uint16_t: _Optional[int] = ..., uint32: _Optional[int] = ..., uint32_t: _Optional[int] = ..., uint64: _Optional[int] = ..., uint64_t: _Optional[int] = ..., int8: _Optional[int] = ..., int8_t: _Optional[int] = ..., int16: _Optional[int] = ..., int16_t: _Optional[int] = ..., int32: _Optional[int] = ..., int32_t: _Optional[int] = ..., int64: _Optional[int] = ..., int64_t: _Optional[int] = ..., size_t: _Optional[int] = ..., ssize_t: _Optional[int] = ..., intptr_t: _Optional[int] = ..., uintptr_t: _Optional[int] = ..., string: _Optional[str] = ..., memset: _Optional[int] = ..., cached_size: _Optional[int] = ..., extensions: _Optional[int] = ..., bit: _Optional[int] = ..., bits: _Optional[int] = ..., offsets: _Optional[int] = ..., reflection: _Optional[int] = ..., some_cord: _Optional[str] = ..., some_string_piece: _Optional[str] = ..., int: _Optional[int] = ..., friend: _Optional[int] = ..., typedecl: _Optional[int] = ..., auto: _Optional[int] = ..., do: _Optional[_Union[TestConflictingSymbolNames.DO, _Mapping]] = ..., field_type: _Optional[int] = ..., is_packed: bool = ..., release_length: _Optional[str] = ..., release_do: _Optional[_Union[TestConflictingSymbolNames.DO, _Mapping]] = ..., target: _Optional[str] = ..., **kwargs) -> None: ...

class GetDescriptor(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetReflection(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Swap(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnsafeArenaSwap(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class New(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CopyFrom(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MergeFrom(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Clear(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IsInitialized(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestConflictingSymbolNamesExtension(_message.Message):
    __slots__ = ()
    REPEATED_INT32_EXT_FIELD_NUMBER: _ClassVar[int]
    repeated_int32_ext: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class TestConflictingEnumNames(_message.Message):
    __slots__ = ("conflicting_enum",)
    class while(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        default: _ClassVar[getattr(TestConflictingEnumNames, 'while')]
        and: _ClassVar[getattr(TestConflictingEnumNames, 'while')]
        class: _ClassVar[getattr(TestConflictingEnumNames, 'while')]
        int: _ClassVar[getattr(TestConflictingEnumNames, 'while')]
        typedef: _ClassVar[getattr(TestConflictingEnumNames, 'while')]
        XOR: _ClassVar[getattr(TestConflictingEnumNames, 'while')]
    default: getattr(TestConflictingEnumNames, 'while')
    and: getattr(TestConflictingEnumNames, 'while')
    class: getattr(TestConflictingEnumNames, 'while')
    int: getattr(TestConflictingEnumNames, 'while')
    typedef: getattr(TestConflictingEnumNames, 'while')
    XOR: getattr(TestConflictingEnumNames, 'while')
    CONFLICTING_ENUM_FIELD_NUMBER: _ClassVar[int]
    conflicting_enum: getattr(TestConflictingEnumNames, 'while')
    def __init__(self, conflicting_enum: _Optional[_Union[getattr(TestConflictingEnumNames, 'while'), str]] = ...) -> None: ...

class DummyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NULL(_message.Message):
    __slots__ = ("int",)
    INT_FIELD_NUMBER: _ClassVar[int]
    int: int
    def __init__(self, int: _Optional[int] = ...) -> None: ...

class Shutdown(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TableStruct(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
