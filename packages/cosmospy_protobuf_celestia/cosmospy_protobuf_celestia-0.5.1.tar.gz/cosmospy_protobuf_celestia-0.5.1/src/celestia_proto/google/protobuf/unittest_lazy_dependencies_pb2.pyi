from google.protobuf import unittest_lazy_dependencies_custom_option_pb2 as _unittest_lazy_dependencies_custom_option_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportedMessage(_message.Message):
    __slots__ = ("lazy_message",)
    LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    lazy_message: _unittest_lazy_dependencies_custom_option_pb2.LazyMessage
    def __init__(self, lazy_message: _Optional[_Union[_unittest_lazy_dependencies_custom_option_pb2.LazyMessage, _Mapping]] = ...) -> None: ...

class MessageCustomOption(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MessageCustomOption2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
