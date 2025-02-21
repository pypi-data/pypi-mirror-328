from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetaAnnotatedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_NULL: _ClassVar[MetaAnnotatedEnum]
    TEST_REDACTABLE: _ClassVar[MetaAnnotatedEnum]
    TEST_NO_REDACT: _ClassVar[MetaAnnotatedEnum]
    TEST_NO_REDACT_AGAIN: _ClassVar[MetaAnnotatedEnum]
    TEST_REDACTABLE_FALSE: _ClassVar[MetaAnnotatedEnum]
TEST_NULL: MetaAnnotatedEnum
TEST_REDACTABLE: MetaAnnotatedEnum
TEST_NO_REDACT: MetaAnnotatedEnum
TEST_NO_REDACT_AGAIN: MetaAnnotatedEnum
TEST_REDACTABLE_FALSE: MetaAnnotatedEnum
META_ANNOTATED_ENUM_FIELD_NUMBER: _ClassVar[int]
meta_annotated_enum: _descriptor.FieldDescriptor
REPEATED_META_ANNOTATED_ENUM_FIELD_NUMBER: _ClassVar[int]
repeated_meta_annotated_enum: _descriptor.FieldDescriptor
TEST_NESTED_MESSAGE_ENUM_FIELD_NUMBER: _ClassVar[int]
test_nested_message_enum: _descriptor.FieldDescriptor

class TestRedactedNestMessage(_message.Message):
    __slots__ = ("foo",)
    FOO_FIELD_NUMBER: _ClassVar[int]
    foo: str
    def __init__(self, foo: _Optional[str] = ...) -> None: ...

class TestRepeatedRedactedNestMessage(_message.Message):
    __slots__ = ("bar",)
    BAR_FIELD_NUMBER: _ClassVar[int]
    bar: str
    def __init__(self, bar: _Optional[str] = ...) -> None: ...

class TestMessageEnum(_message.Message):
    __slots__ = ("redactable_enum",)
    REDACTABLE_ENUM_FIELD_NUMBER: _ClassVar[int]
    redactable_enum: _containers.RepeatedScalarFieldContainer[MetaAnnotatedEnum]
    def __init__(self, redactable_enum: _Optional[_Iterable[_Union[MetaAnnotatedEnum, str]]] = ...) -> None: ...

class TestNestedMessageEnum(_message.Message):
    __slots__ = ("direct_enum", "nested_enum", "redacted_string")
    DIRECT_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REDACTED_STRING_FIELD_NUMBER: _ClassVar[int]
    direct_enum: _containers.RepeatedScalarFieldContainer[MetaAnnotatedEnum]
    nested_enum: TestMessageEnum
    redacted_string: str
    def __init__(self, direct_enum: _Optional[_Iterable[_Union[MetaAnnotatedEnum, str]]] = ..., nested_enum: _Optional[_Union[TestMessageEnum, _Mapping]] = ..., redacted_string: _Optional[str] = ...) -> None: ...

class TestRedactedMessage(_message.Message):
    __slots__ = ("text_field", "meta_annotated", "repeated_meta_annotated", "unredacted_repeated_annotations", "unreported_non_meta_debug_redact_field", "any_field", "redactable_false", "test_direct_message_enum", "test_nested_message_enum", "test_redacted_message_enum")
    TEXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    META_ANNOTATED_FIELD_NUMBER: _ClassVar[int]
    REPEATED_META_ANNOTATED_FIELD_NUMBER: _ClassVar[int]
    UNREDACTED_REPEATED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UNREPORTED_NON_META_DEBUG_REDACT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ANY_FIELD_FIELD_NUMBER: _ClassVar[int]
    REDACTABLE_FALSE_FIELD_NUMBER: _ClassVar[int]
    TEST_DIRECT_MESSAGE_ENUM_FIELD_NUMBER: _ClassVar[int]
    TEST_NESTED_MESSAGE_ENUM_FIELD_NUMBER: _ClassVar[int]
    TEST_REDACTED_MESSAGE_ENUM_FIELD_NUMBER: _ClassVar[int]
    text_field: str
    meta_annotated: str
    repeated_meta_annotated: str
    unredacted_repeated_annotations: str
    unreported_non_meta_debug_redact_field: str
    any_field: _any_pb2.Any
    redactable_false: str
    test_direct_message_enum: str
    test_nested_message_enum: str
    test_redacted_message_enum: str
    def __init__(self, text_field: _Optional[str] = ..., meta_annotated: _Optional[str] = ..., repeated_meta_annotated: _Optional[str] = ..., unredacted_repeated_annotations: _Optional[str] = ..., unreported_non_meta_debug_redact_field: _Optional[str] = ..., any_field: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., redactable_false: _Optional[str] = ..., test_direct_message_enum: _Optional[str] = ..., test_nested_message_enum: _Optional[str] = ..., test_redacted_message_enum: _Optional[str] = ...) -> None: ...
