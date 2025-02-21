from google.protobuf import unittest_import_public_pb2 as _unittest_import_public_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
from google.protobuf.unittest_import_public_pb2 import PublicImportMessage as PublicImportMessage

DESCRIPTOR: _descriptor.FileDescriptor

class ImportEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORT_FOO: _ClassVar[ImportEnum]
    IMPORT_BAR: _ClassVar[ImportEnum]
    IMPORT_BAZ: _ClassVar[ImportEnum]

class ImportEnumForMap(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[ImportEnumForMap]
    FOO: _ClassVar[ImportEnumForMap]
    BAR: _ClassVar[ImportEnumForMap]
IMPORT_FOO: ImportEnum
IMPORT_BAR: ImportEnum
IMPORT_BAZ: ImportEnum
UNKNOWN: ImportEnumForMap
FOO: ImportEnumForMap
BAR: ImportEnumForMap

class ImportMessage(_message.Message):
    __slots__ = ("d",)
    D_FIELD_NUMBER: _ClassVar[int]
    d: int
    def __init__(self, d: _Optional[int] = ...) -> None: ...
