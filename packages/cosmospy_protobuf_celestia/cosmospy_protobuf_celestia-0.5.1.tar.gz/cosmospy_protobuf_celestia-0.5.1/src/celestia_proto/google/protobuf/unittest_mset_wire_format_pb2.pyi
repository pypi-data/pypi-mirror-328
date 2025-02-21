from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessageSet(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestMessageSetWireFormatContainer(_message.Message):
    __slots__ = ("message_set",)
    MESSAGE_SET_FIELD_NUMBER: _ClassVar[int]
    message_set: TestMessageSet
    def __init__(self, message_set: _Optional[_Union[TestMessageSet, _Mapping]] = ...) -> None: ...
