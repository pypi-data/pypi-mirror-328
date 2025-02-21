from google.protobuf import unittest_import_public_lite_pb2 as _unittest_import_public_lite_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
from google.protobuf.unittest_import_public_lite_pb2 import PublicImportMessageLite as PublicImportMessageLite

DESCRIPTOR: _descriptor.FileDescriptor

class ImportEnumLite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORT_LITE_FOO: _ClassVar[ImportEnumLite]
    IMPORT_LITE_BAR: _ClassVar[ImportEnumLite]
    IMPORT_LITE_BAZ: _ClassVar[ImportEnumLite]
IMPORT_LITE_FOO: ImportEnumLite
IMPORT_LITE_BAR: ImportEnumLite
IMPORT_LITE_BAZ: ImportEnumLite

class ImportMessageLite(_message.Message):
    __slots__ = ("d",)
    D_FIELD_NUMBER: _ClassVar[int]
    d: int
    def __init__(self, d: _Optional[int] = ...) -> None: ...
