from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TopLevelEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOP_LEVEL_UNKNOWN: _ClassVar[TopLevelEnum]
TOP_LEVEL_UNKNOWN: TopLevelEnum
PLAIN_OPTION_FIELD_NUMBER: _ClassVar[int]
plain_option: _descriptor.FieldDescriptor
RUNTIME_RETENTION_OPTION_FIELD_NUMBER: _ClassVar[int]
runtime_retention_option: _descriptor.FieldDescriptor
SOURCE_RETENTION_OPTION_FIELD_NUMBER: _ClassVar[int]
source_retention_option: _descriptor.FieldDescriptor
FILE_OPTION_FIELD_NUMBER: _ClassVar[int]
file_option: _descriptor.FieldDescriptor
REPEATED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
repeated_options: _descriptor.FieldDescriptor
EXTENSION_RANGE_OPTION_FIELD_NUMBER: _ClassVar[int]
extension_range_option: _descriptor.FieldDescriptor
MESSAGE_OPTION_FIELD_NUMBER: _ClassVar[int]
message_option: _descriptor.FieldDescriptor
FIELD_OPTION_FIELD_NUMBER: _ClassVar[int]
field_option: _descriptor.FieldDescriptor
ONEOF_OPTION_FIELD_NUMBER: _ClassVar[int]
oneof_option: _descriptor.FieldDescriptor
ENUM_OPTION_FIELD_NUMBER: _ClassVar[int]
enum_option: _descriptor.FieldDescriptor
ENUM_ENTRY_OPTION_FIELD_NUMBER: _ClassVar[int]
enum_entry_option: _descriptor.FieldDescriptor
SERVICE_OPTION_FIELD_NUMBER: _ClassVar[int]
service_option: _descriptor.FieldDescriptor
METHOD_OPTION_FIELD_NUMBER: _ClassVar[int]
method_option: _descriptor.FieldDescriptor
I_FIELD_NUMBER: _ClassVar[int]
i: _descriptor.FieldDescriptor

class OptionsMessage(_message.Message):
    __slots__ = ("plain_field", "runtime_retention_field", "source_retention_field")
    PLAIN_FIELD_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_RETENTION_FIELD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RETENTION_FIELD_FIELD_NUMBER: _ClassVar[int]
    plain_field: int
    runtime_retention_field: int
    source_retention_field: int
    def __init__(self, plain_field: _Optional[int] = ..., runtime_retention_field: _Optional[int] = ..., source_retention_field: _Optional[int] = ...) -> None: ...

class Extendee(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TopLevelMessage(_message.Message):
    __slots__ = ("f", "i")
    Extensions: _python_message._ExtensionDict
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NESTED_UNKNOWN: _ClassVar[TopLevelMessage.NestedEnum]
    NESTED_UNKNOWN: TopLevelMessage.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    S_FIELD_NUMBER: _ClassVar[int]
    s: _descriptor.FieldDescriptor
    F_FIELD_NUMBER: _ClassVar[int]
    I_FIELD_NUMBER: _ClassVar[int]
    f: float
    i: int
    def __init__(self, f: _Optional[float] = ..., i: _Optional[int] = ...) -> None: ...
