from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MyEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOO: _ClassVar[MyEnum]
    BAR: _ClassVar[MyEnum]
    BAZ: _ClassVar[MyEnum]
FOO: MyEnum
BAR: MyEnum
BAZ: MyEnum

class MyMessage(_message.Message):
    __slots__ = ("e", "repeated_e", "repeated_packed_e", "repeated_packed_unexpected_e", "oneof_e_1", "oneof_e_2")
    E_FIELD_NUMBER: _ClassVar[int]
    REPEATED_E_FIELD_NUMBER: _ClassVar[int]
    REPEATED_PACKED_E_FIELD_NUMBER: _ClassVar[int]
    REPEATED_PACKED_UNEXPECTED_E_FIELD_NUMBER: _ClassVar[int]
    ONEOF_E_1_FIELD_NUMBER: _ClassVar[int]
    ONEOF_E_2_FIELD_NUMBER: _ClassVar[int]
    e: MyEnum
    repeated_e: _containers.RepeatedScalarFieldContainer[MyEnum]
    repeated_packed_e: _containers.RepeatedScalarFieldContainer[MyEnum]
    repeated_packed_unexpected_e: _containers.RepeatedScalarFieldContainer[MyEnum]
    oneof_e_1: MyEnum
    oneof_e_2: MyEnum
    def __init__(self, e: _Optional[_Union[MyEnum, str]] = ..., repeated_e: _Optional[_Iterable[_Union[MyEnum, str]]] = ..., repeated_packed_e: _Optional[_Iterable[_Union[MyEnum, str]]] = ..., repeated_packed_unexpected_e: _Optional[_Iterable[_Union[MyEnum, str]]] = ..., oneof_e_1: _Optional[_Union[MyEnum, str]] = ..., oneof_e_2: _Optional[_Union[MyEnum, str]] = ...) -> None: ...
