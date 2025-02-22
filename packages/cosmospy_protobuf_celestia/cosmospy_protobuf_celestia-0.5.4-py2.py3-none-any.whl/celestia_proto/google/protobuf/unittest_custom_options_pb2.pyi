from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MethodOpt1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METHODOPT1_VAL1: _ClassVar[MethodOpt1]
    METHODOPT1_VAL2: _ClassVar[MethodOpt1]

class AggregateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE: _ClassVar[AggregateEnum]
METHODOPT1_VAL1: MethodOpt1
METHODOPT1_VAL2: MethodOpt1
VALUE: AggregateEnum
FILE_OPT1_FIELD_NUMBER: _ClassVar[int]
file_opt1: _descriptor.FieldDescriptor
MESSAGE_OPT1_FIELD_NUMBER: _ClassVar[int]
message_opt1: _descriptor.FieldDescriptor
FIELD_OPT1_FIELD_NUMBER: _ClassVar[int]
field_opt1: _descriptor.FieldDescriptor
FIELD_OPT2_FIELD_NUMBER: _ClassVar[int]
field_opt2: _descriptor.FieldDescriptor
ONEOF_OPT1_FIELD_NUMBER: _ClassVar[int]
oneof_opt1: _descriptor.FieldDescriptor
ENUM_OPT1_FIELD_NUMBER: _ClassVar[int]
enum_opt1: _descriptor.FieldDescriptor
ENUM_VALUE_OPT1_FIELD_NUMBER: _ClassVar[int]
enum_value_opt1: _descriptor.FieldDescriptor
SERVICE_OPT1_FIELD_NUMBER: _ClassVar[int]
service_opt1: _descriptor.FieldDescriptor
METHOD_OPT1_FIELD_NUMBER: _ClassVar[int]
method_opt1: _descriptor.FieldDescriptor
BOOL_OPT_FIELD_NUMBER: _ClassVar[int]
bool_opt: _descriptor.FieldDescriptor
INT32_OPT_FIELD_NUMBER: _ClassVar[int]
int32_opt: _descriptor.FieldDescriptor
INT64_OPT_FIELD_NUMBER: _ClassVar[int]
int64_opt: _descriptor.FieldDescriptor
UINT32_OPT_FIELD_NUMBER: _ClassVar[int]
uint32_opt: _descriptor.FieldDescriptor
UINT64_OPT_FIELD_NUMBER: _ClassVar[int]
uint64_opt: _descriptor.FieldDescriptor
SINT32_OPT_FIELD_NUMBER: _ClassVar[int]
sint32_opt: _descriptor.FieldDescriptor
SINT64_OPT_FIELD_NUMBER: _ClassVar[int]
sint64_opt: _descriptor.FieldDescriptor
FIXED32_OPT_FIELD_NUMBER: _ClassVar[int]
fixed32_opt: _descriptor.FieldDescriptor
FIXED64_OPT_FIELD_NUMBER: _ClassVar[int]
fixed64_opt: _descriptor.FieldDescriptor
SFIXED32_OPT_FIELD_NUMBER: _ClassVar[int]
sfixed32_opt: _descriptor.FieldDescriptor
SFIXED64_OPT_FIELD_NUMBER: _ClassVar[int]
sfixed64_opt: _descriptor.FieldDescriptor
FLOAT_OPT_FIELD_NUMBER: _ClassVar[int]
float_opt: _descriptor.FieldDescriptor
DOUBLE_OPT_FIELD_NUMBER: _ClassVar[int]
double_opt: _descriptor.FieldDescriptor
STRING_OPT_FIELD_NUMBER: _ClassVar[int]
string_opt: _descriptor.FieldDescriptor
BYTES_OPT_FIELD_NUMBER: _ClassVar[int]
bytes_opt: _descriptor.FieldDescriptor
ENUM_OPT_FIELD_NUMBER: _ClassVar[int]
enum_opt: _descriptor.FieldDescriptor
MESSAGE_TYPE_OPT_FIELD_NUMBER: _ClassVar[int]
message_type_opt: _descriptor.FieldDescriptor
MOOO_FIELD_NUMBER: _ClassVar[int]
mooo: _descriptor.FieldDescriptor
CORGE_FIELD_NUMBER: _ClassVar[int]
corge: _descriptor.FieldDescriptor
GRAULT_FIELD_NUMBER: _ClassVar[int]
grault: _descriptor.FieldDescriptor
GARPLY_FIELD_NUMBER: _ClassVar[int]
garply: _descriptor.FieldDescriptor
COMPLEX_OPT1_FIELD_NUMBER: _ClassVar[int]
complex_opt1: _descriptor.FieldDescriptor
COMPLEX_OPT2_FIELD_NUMBER: _ClassVar[int]
complex_opt2: _descriptor.FieldDescriptor
COMPLEX_OPT3_FIELD_NUMBER: _ClassVar[int]
complex_opt3: _descriptor.FieldDescriptor
COMPLEXOPT6_FIELD_NUMBER: _ClassVar[int]
complexopt6: _descriptor.FieldDescriptor
FILEOPT_FIELD_NUMBER: _ClassVar[int]
fileopt: _descriptor.FieldDescriptor
MSGOPT_FIELD_NUMBER: _ClassVar[int]
msgopt: _descriptor.FieldDescriptor
FIELDOPT_FIELD_NUMBER: _ClassVar[int]
fieldopt: _descriptor.FieldDescriptor
ENUMOPT_FIELD_NUMBER: _ClassVar[int]
enumopt: _descriptor.FieldDescriptor
ENUMVALOPT_FIELD_NUMBER: _ClassVar[int]
enumvalopt: _descriptor.FieldDescriptor
SERVICEOPT_FIELD_NUMBER: _ClassVar[int]
serviceopt: _descriptor.FieldDescriptor
METHODOPT_FIELD_NUMBER: _ClassVar[int]
methodopt: _descriptor.FieldDescriptor
REQUIRED_ENUM_OPT_FIELD_NUMBER: _ClassVar[int]
required_enum_opt: _descriptor.FieldDescriptor

class TestMessageWithCustomOptions(_message.Message):
    __slots__ = ("field1", "oneof_field", "map_field")
    class AnEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANENUM_VAL1: _ClassVar[TestMessageWithCustomOptions.AnEnum]
        ANENUM_VAL2: _ClassVar[TestMessageWithCustomOptions.AnEnum]
    ANENUM_VAL1: TestMessageWithCustomOptions.AnEnum
    ANENUM_VAL2: TestMessageWithCustomOptions.AnEnum
    class MapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FIELD_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    field1: str
    oneof_field: int
    map_field: _containers.ScalarMap[str, str]
    def __init__(self, field1: _Optional[str] = ..., oneof_field: _Optional[int] = ..., map_field: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CustomOptionFooRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionFooResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionFooClientMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionFooServerMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DummyMessageContainingEnum(_message.Message):
    __slots__ = ()
    class TestEnumType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEST_OPTION_ENUM_TYPE1: _ClassVar[DummyMessageContainingEnum.TestEnumType]
        TEST_OPTION_ENUM_TYPE2: _ClassVar[DummyMessageContainingEnum.TestEnumType]
    TEST_OPTION_ENUM_TYPE1: DummyMessageContainingEnum.TestEnumType
    TEST_OPTION_ENUM_TYPE2: DummyMessageContainingEnum.TestEnumType
    def __init__(self) -> None: ...

class DummyMessageInvalidAsOptionType(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionMinIntegerValues(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionMaxIntegerValues(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionOtherValues(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingRealsFromPositiveInts(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingRealsFromNegativeInts(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingRealsFromInf(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingRealsFromNegativeInf(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingRealsFromNan(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingRealsFromNegativeNan(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ComplexOptionType1(_message.Message):
    __slots__ = ("foo", "foo2", "foo3", "foo4")
    Extensions: _python_message._ExtensionDict
    FOO_FIELD_NUMBER: _ClassVar[int]
    FOO2_FIELD_NUMBER: _ClassVar[int]
    FOO3_FIELD_NUMBER: _ClassVar[int]
    FOO4_FIELD_NUMBER: _ClassVar[int]
    foo: int
    foo2: int
    foo3: int
    foo4: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, foo: _Optional[int] = ..., foo2: _Optional[int] = ..., foo3: _Optional[int] = ..., foo4: _Optional[_Iterable[int]] = ...) -> None: ...

class ComplexOptionType2(_message.Message):
    __slots__ = ("bar", "baz", "fred", "barney")
    Extensions: _python_message._ExtensionDict
    class ComplexOptionType4(_message.Message):
        __slots__ = ("waldo",)
        COMPLEX_OPT4_FIELD_NUMBER: _ClassVar[int]
        complex_opt4: _descriptor.FieldDescriptor
        WALDO_FIELD_NUMBER: _ClassVar[int]
        waldo: int
        def __init__(self, waldo: _Optional[int] = ...) -> None: ...
    BAR_FIELD_NUMBER: _ClassVar[int]
    BAZ_FIELD_NUMBER: _ClassVar[int]
    FRED_FIELD_NUMBER: _ClassVar[int]
    BARNEY_FIELD_NUMBER: _ClassVar[int]
    bar: ComplexOptionType1
    baz: int
    fred: ComplexOptionType2.ComplexOptionType4
    barney: _containers.RepeatedCompositeFieldContainer[ComplexOptionType2.ComplexOptionType4]
    def __init__(self, bar: _Optional[_Union[ComplexOptionType1, _Mapping]] = ..., baz: _Optional[int] = ..., fred: _Optional[_Union[ComplexOptionType2.ComplexOptionType4, _Mapping]] = ..., barney: _Optional[_Iterable[_Union[ComplexOptionType2.ComplexOptionType4, _Mapping]]] = ...) -> None: ...

class ComplexOptionType3(_message.Message):
    __slots__ = ("moo", "complexoptiontype5")
    class ComplexOptionType5(_message.Message):
        __slots__ = ("plugh",)
        PLUGH_FIELD_NUMBER: _ClassVar[int]
        plugh: int
        def __init__(self, plugh: _Optional[int] = ...) -> None: ...
    MOO_FIELD_NUMBER: _ClassVar[int]
    COMPLEXOPTIONTYPE5_FIELD_NUMBER: _ClassVar[int]
    moo: int
    complexoptiontype5: ComplexOptionType3.ComplexOptionType5
    def __init__(self, moo: _Optional[int] = ..., complexoptiontype5: _Optional[_Union[ComplexOptionType3.ComplexOptionType5, _Mapping]] = ...) -> None: ...

class ComplexOpt6(_message.Message):
    __slots__ = ("xyzzy",)
    XYZZY_FIELD_NUMBER: _ClassVar[int]
    xyzzy: int
    def __init__(self, xyzzy: _Optional[int] = ...) -> None: ...

class VariousComplexOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AggregateMessageSet(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class AggregateMessageSetElement(_message.Message):
    __slots__ = ("s",)
    MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    message_set_extension: _descriptor.FieldDescriptor
    S_FIELD_NUMBER: _ClassVar[int]
    s: str
    def __init__(self, s: _Optional[str] = ...) -> None: ...

class Aggregate(_message.Message):
    __slots__ = ("i", "s", "sub", "file", "mset", "any")
    NESTED_FIELD_NUMBER: _ClassVar[int]
    nested: _descriptor.FieldDescriptor
    I_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MSET_FIELD_NUMBER: _ClassVar[int]
    ANY_FIELD_NUMBER: _ClassVar[int]
    i: int
    s: str
    sub: Aggregate
    file: _descriptor_pb2.FileOptions
    mset: AggregateMessageSet
    any: _any_pb2.Any
    def __init__(self, i: _Optional[int] = ..., s: _Optional[str] = ..., sub: _Optional[_Union[Aggregate, _Mapping]] = ..., file: _Optional[_Union[_descriptor_pb2.FileOptions, _Mapping]] = ..., mset: _Optional[_Union[AggregateMessageSet, _Mapping]] = ..., any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class AggregateMessage(_message.Message):
    __slots__ = ("fieldname",)
    FIELDNAME_FIELD_NUMBER: _ClassVar[int]
    fieldname: int
    def __init__(self, fieldname: _Optional[int] = ...) -> None: ...

class NestedOptionType(_message.Message):
    __slots__ = ()
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NESTED_ENUM_VALUE: _ClassVar[NestedOptionType.NestedEnum]
    NESTED_ENUM_VALUE: NestedOptionType.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("nested_field",)
        NESTED_FIELD_FIELD_NUMBER: _ClassVar[int]
        nested_field: int
        def __init__(self, nested_field: _Optional[int] = ...) -> None: ...
    NESTED_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    nested_extension: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class OldOptionType(_message.Message):
    __slots__ = ("value",)
    class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OLD_VALUE: _ClassVar[OldOptionType.TestEnum]
    OLD_VALUE: OldOptionType.TestEnum
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: OldOptionType.TestEnum
    def __init__(self, value: _Optional[_Union[OldOptionType.TestEnum, str]] = ...) -> None: ...

class NewOptionType(_message.Message):
    __slots__ = ("value",)
    class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OLD_VALUE: _ClassVar[NewOptionType.TestEnum]
        NEW_VALUE: _ClassVar[NewOptionType.TestEnum]
    OLD_VALUE: NewOptionType.TestEnum
    NEW_VALUE: NewOptionType.TestEnum
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: NewOptionType.TestEnum
    def __init__(self, value: _Optional[_Union[NewOptionType.TestEnum, str]] = ...) -> None: ...

class TestMessageWithRequiredEnumOption(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestServiceWithCustomOptions(_service.service): ...

class TestServiceWithCustomOptions_Stub(TestServiceWithCustomOptions): ...

class AggregateService(_service.service): ...

class AggregateService_Stub(AggregateService): ...
