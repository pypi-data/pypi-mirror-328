from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_ENUM_FEATURE_UNKNOWN: _ClassVar[EnumFeature]
    VALUE1: _ClassVar[EnumFeature]
    VALUE2: _ClassVar[EnumFeature]
    VALUE3: _ClassVar[EnumFeature]
    VALUE4: _ClassVar[EnumFeature]
    VALUE5: _ClassVar[EnumFeature]
    VALUE6: _ClassVar[EnumFeature]
    VALUE7: _ClassVar[EnumFeature]
    VALUE8: _ClassVar[EnumFeature]
    VALUE9: _ClassVar[EnumFeature]
    VALUE10: _ClassVar[EnumFeature]
    VALUE11: _ClassVar[EnumFeature]
    VALUE12: _ClassVar[EnumFeature]
    VALUE13: _ClassVar[EnumFeature]
    VALUE14: _ClassVar[EnumFeature]
    VALUE15: _ClassVar[EnumFeature]

class ValueLifetimeFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_VALUE_LIFETIME_UNKNOWN: _ClassVar[ValueLifetimeFeature]
    VALUE_LIFETIME_INHERITED: _ClassVar[ValueLifetimeFeature]
    VALUE_LIFETIME_SUPPORT: _ClassVar[ValueLifetimeFeature]
    VALUE_LIFETIME_EMPTY_SUPPORT: _ClassVar[ValueLifetimeFeature]
    VALUE_LIFETIME_FUTURE: _ClassVar[ValueLifetimeFeature]
    VALUE_LIFETIME_DEPRECATED: _ClassVar[ValueLifetimeFeature]
    VALUE_LIFETIME_REMOVED: _ClassVar[ValueLifetimeFeature]
TEST_ENUM_FEATURE_UNKNOWN: EnumFeature
VALUE1: EnumFeature
VALUE2: EnumFeature
VALUE3: EnumFeature
VALUE4: EnumFeature
VALUE5: EnumFeature
VALUE6: EnumFeature
VALUE7: EnumFeature
VALUE8: EnumFeature
VALUE9: EnumFeature
VALUE10: EnumFeature
VALUE11: EnumFeature
VALUE12: EnumFeature
VALUE13: EnumFeature
VALUE14: EnumFeature
VALUE15: EnumFeature
TEST_VALUE_LIFETIME_UNKNOWN: ValueLifetimeFeature
VALUE_LIFETIME_INHERITED: ValueLifetimeFeature
VALUE_LIFETIME_SUPPORT: ValueLifetimeFeature
VALUE_LIFETIME_EMPTY_SUPPORT: ValueLifetimeFeature
VALUE_LIFETIME_FUTURE: ValueLifetimeFeature
VALUE_LIFETIME_DEPRECATED: ValueLifetimeFeature
VALUE_LIFETIME_REMOVED: ValueLifetimeFeature
TEST_FIELD_NUMBER: _ClassVar[int]
test: _descriptor.FieldDescriptor

class TestMessage(_message.Message):
    __slots__ = ()
    class Nested(_message.Message):
        __slots__ = ()
        TEST_NESTED_FIELD_NUMBER: _ClassVar[int]
        test_nested: _descriptor.FieldDescriptor
        def __init__(self) -> None: ...
    TEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    test_message: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class TestFeatures(_message.Message):
    __slots__ = ("file_feature", "extension_range_feature", "message_feature", "field_feature", "oneof_feature", "enum_feature", "enum_entry_feature", "service_feature", "method_feature", "multiple_feature", "bool_field_feature", "source_feature", "source_feature2", "removed_feature", "future_feature", "legacy_feature", "value_lifetime_feature")
    FILE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_RANGE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FEATURE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FEATURE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FEATURE_FIELD_NUMBER: _ClassVar[int]
    ENUM_ENTRY_FEATURE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FEATURE_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FEATURE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FEATURE2_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FEATURE_FIELD_NUMBER: _ClassVar[int]
    FUTURE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_FEATURE_FIELD_NUMBER: _ClassVar[int]
    VALUE_LIFETIME_FEATURE_FIELD_NUMBER: _ClassVar[int]
    file_feature: EnumFeature
    extension_range_feature: EnumFeature
    message_feature: EnumFeature
    field_feature: EnumFeature
    oneof_feature: EnumFeature
    enum_feature: EnumFeature
    enum_entry_feature: EnumFeature
    service_feature: EnumFeature
    method_feature: EnumFeature
    multiple_feature: EnumFeature
    bool_field_feature: bool
    source_feature: EnumFeature
    source_feature2: EnumFeature
    removed_feature: EnumFeature
    future_feature: EnumFeature
    legacy_feature: EnumFeature
    value_lifetime_feature: ValueLifetimeFeature
    def __init__(self, file_feature: _Optional[_Union[EnumFeature, str]] = ..., extension_range_feature: _Optional[_Union[EnumFeature, str]] = ..., message_feature: _Optional[_Union[EnumFeature, str]] = ..., field_feature: _Optional[_Union[EnumFeature, str]] = ..., oneof_feature: _Optional[_Union[EnumFeature, str]] = ..., enum_feature: _Optional[_Union[EnumFeature, str]] = ..., enum_entry_feature: _Optional[_Union[EnumFeature, str]] = ..., service_feature: _Optional[_Union[EnumFeature, str]] = ..., method_feature: _Optional[_Union[EnumFeature, str]] = ..., multiple_feature: _Optional[_Union[EnumFeature, str]] = ..., bool_field_feature: bool = ..., source_feature: _Optional[_Union[EnumFeature, str]] = ..., source_feature2: _Optional[_Union[EnumFeature, str]] = ..., removed_feature: _Optional[_Union[EnumFeature, str]] = ..., future_feature: _Optional[_Union[EnumFeature, str]] = ..., legacy_feature: _Optional[_Union[EnumFeature, str]] = ..., value_lifetime_feature: _Optional[_Union[ValueLifetimeFeature, str]] = ...) -> None: ...
