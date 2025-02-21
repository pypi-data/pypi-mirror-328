from google.protobuf import unittest_delimited_import_pb2 as _unittest_delimited_import_pb2
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
LENGTHPREFIXED_FIELD_NUMBER: _ClassVar[int]
lengthprefixed: _descriptor.FieldDescriptor
GROUPLIKEFILESCOPE_FIELD_NUMBER: _ClassVar[int]
grouplikefilescope: _descriptor.FieldDescriptor
NOT_GROUP_LIKE_SCOPE_FIELD_NUMBER: _ClassVar[int]
not_group_like_scope: _descriptor.FieldDescriptor
GROUPLIKE_FIELD_NUMBER: _ClassVar[int]
grouplike: _descriptor.FieldDescriptor
MESSAGEIMPORT_FIELD_NUMBER: _ClassVar[int]
messageimport: _descriptor.FieldDescriptor

class LengthPrefixed(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...

class NotGroupLikeScope(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...

class GroupLikeFileScope(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...

class TestDelimited(_message.Message):
    __slots__ = ("lengthprefixed", "nested", "grouplike", "notgrouplike", "notgrouplikescope", "messageimport")
    Extensions: _python_message._ExtensionDict
    class LengthPrefixed(_message.Message):
        __slots__ = ("a", "b")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: int
        def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...
    class GroupLike(_message.Message):
        __slots__ = ("a", "b")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: int
        def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...
    LENGTHPREFIXED_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    GROUPLIKE_FIELD_NUMBER: _ClassVar[int]
    NOTGROUPLIKE_FIELD_NUMBER: _ClassVar[int]
    NOTGROUPLIKESCOPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGEIMPORT_FIELD_NUMBER: _ClassVar[int]
    lengthprefixed: TestDelimited.LengthPrefixed
    nested: TestDelimited
    grouplike: TestDelimited.GroupLike
    notgrouplike: TestDelimited.GroupLike
    notgrouplikescope: NotGroupLikeScope
    messageimport: _unittest_delimited_import_pb2.MessageImport
    def __init__(self, lengthprefixed: _Optional[_Union[TestDelimited.LengthPrefixed, _Mapping]] = ..., nested: _Optional[_Union[TestDelimited, _Mapping]] = ..., grouplike: _Optional[_Union[TestDelimited.GroupLike, _Mapping]] = ..., notgrouplike: _Optional[_Union[TestDelimited.GroupLike, _Mapping]] = ..., notgrouplikescope: _Optional[_Union[NotGroupLikeScope, _Mapping]] = ..., messageimport: _Optional[_Union[_unittest_delimited_import_pb2.MessageImport, _Mapping]] = ...) -> None: ...
