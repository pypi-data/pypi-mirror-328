from google.protobuf import unittest_mset_wire_format_pb2 as _unittest_mset_wire_format_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessageSetContainer(_message.Message):
    __slots__ = ("message_set",)
    MESSAGE_SET_FIELD_NUMBER: _ClassVar[int]
    message_set: _unittest_mset_wire_format_pb2.TestMessageSet
    def __init__(self, message_set: _Optional[_Union[_unittest_mset_wire_format_pb2.TestMessageSet, _Mapping]] = ...) -> None: ...

class NestedTestMessageSetContainer(_message.Message):
    __slots__ = ("container", "child", "lazy_child")
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    LAZY_CHILD_FIELD_NUMBER: _ClassVar[int]
    container: TestMessageSetContainer
    child: NestedTestMessageSetContainer
    lazy_child: NestedTestMessageSetContainer
    def __init__(self, container: _Optional[_Union[TestMessageSetContainer, _Mapping]] = ..., child: _Optional[_Union[NestedTestMessageSetContainer, _Mapping]] = ..., lazy_child: _Optional[_Union[NestedTestMessageSetContainer, _Mapping]] = ...) -> None: ...

class NestedTestInt(_message.Message):
    __slots__ = ("a", "b", "child")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    child: NestedTestInt
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ..., child: _Optional[_Union[NestedTestInt, _Mapping]] = ...) -> None: ...

class TestMessageSetExtension1(_message.Message):
    __slots__ = ("i", "recursive", "test_aliasing")
    MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    message_set_extension: _descriptor.FieldDescriptor
    I_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    TEST_ALIASING_FIELD_NUMBER: _ClassVar[int]
    i: int
    recursive: _unittest_mset_wire_format_pb2.TestMessageSet
    test_aliasing: str
    def __init__(self, i: _Optional[int] = ..., recursive: _Optional[_Union[_unittest_mset_wire_format_pb2.TestMessageSet, _Mapping]] = ..., test_aliasing: _Optional[str] = ...) -> None: ...

class TestMessageSetExtension2(_message.Message):
    __slots__ = ("str",)
    MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    message_set_extension: _descriptor.FieldDescriptor
    STR_FIELD_NUMBER: _ClassVar[int]
    str: str
    def __init__(self, str: _Optional[str] = ...) -> None: ...

class TestMessageSetExtension3(_message.Message):
    __slots__ = ("msg", "required_int")
    MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    message_set_extension: _descriptor.FieldDescriptor
    MSG_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_INT_FIELD_NUMBER: _ClassVar[int]
    msg: NestedTestInt
    required_int: int
    def __init__(self, msg: _Optional[_Union[NestedTestInt, _Mapping]] = ..., required_int: _Optional[int] = ...) -> None: ...

class RawMessageSet(_message.Message):
    __slots__ = ("item",)
    class Item(_message.Message):
        __slots__ = ("type_id", "message")
        TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        type_id: int
        message: bytes
        def __init__(self, type_id: _Optional[int] = ..., message: _Optional[bytes] = ...) -> None: ...
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _containers.RepeatedCompositeFieldContainer[RawMessageSet.Item]
    def __init__(self, item: _Optional[_Iterable[_Union[RawMessageSet.Item, _Mapping]]] = ...) -> None: ...
