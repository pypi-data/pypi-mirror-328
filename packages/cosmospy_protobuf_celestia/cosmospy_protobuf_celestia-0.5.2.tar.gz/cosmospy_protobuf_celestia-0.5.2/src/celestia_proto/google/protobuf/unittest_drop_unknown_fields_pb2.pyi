from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Foo(_message.Message):
    __slots__ = ("int32_value", "enum_value")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[Foo.NestedEnum]
        BAR: _ClassVar[Foo.NestedEnum]
        BAZ: _ClassVar[Foo.NestedEnum]
    FOO: Foo.NestedEnum
    BAR: Foo.NestedEnum
    BAZ: Foo.NestedEnum
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    int32_value: int
    enum_value: Foo.NestedEnum
    def __init__(self, int32_value: _Optional[int] = ..., enum_value: _Optional[_Union[Foo.NestedEnum, str]] = ...) -> None: ...

class FooWithExtraFields(_message.Message):
    __slots__ = ("int32_value", "enum_value", "extra_int32_value")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[FooWithExtraFields.NestedEnum]
        BAR: _ClassVar[FooWithExtraFields.NestedEnum]
        BAZ: _ClassVar[FooWithExtraFields.NestedEnum]
        MOO: _ClassVar[FooWithExtraFields.NestedEnum]
    FOO: FooWithExtraFields.NestedEnum
    BAR: FooWithExtraFields.NestedEnum
    BAZ: FooWithExtraFields.NestedEnum
    MOO: FooWithExtraFields.NestedEnum
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    int32_value: int
    enum_value: FooWithExtraFields.NestedEnum
    extra_int32_value: int
    def __init__(self, int32_value: _Optional[int] = ..., enum_value: _Optional[_Union[FooWithExtraFields.NestedEnum, str]] = ..., extra_int32_value: _Optional[int] = ...) -> None: ...
