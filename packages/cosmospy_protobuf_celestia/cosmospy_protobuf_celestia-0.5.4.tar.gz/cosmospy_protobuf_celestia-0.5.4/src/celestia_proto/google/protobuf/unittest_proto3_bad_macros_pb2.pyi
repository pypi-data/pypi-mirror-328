from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class GID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GID_UNUSED: _ClassVar[GID]

class UID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UID_UNUSED: _ClassVar[UID]

class BadNames(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKAGE: _ClassVar[BadNames]
    PACKED: _ClassVar[BadNames]
    linux: _ClassVar[BadNames]
    DOMAIN: _ClassVar[BadNames]
    TRUE: _ClassVar[BadNames]
    FALSE: _ClassVar[BadNames]
    CREATE_NEW: _ClassVar[BadNames]
    DELETE: _ClassVar[BadNames]
    DOUBLE_CLICK: _ClassVar[BadNames]
    ERROR: _ClassVar[BadNames]
    ERROR_BUSY: _ClassVar[BadNames]
    ERROR_INSTALL_FAILED: _ClassVar[BadNames]
    ERROR_NOT_FOUND: _ClassVar[BadNames]
    GetClassName: _ClassVar[BadNames]
    GetCurrentTime: _ClassVar[BadNames]
    GetMessage: _ClassVar[BadNames]
    GetObject: _ClassVar[BadNames]
    IGNORE: _ClassVar[BadNames]
    IN: _ClassVar[BadNames]
    INPUT_KEYBOARD: _ClassVar[BadNames]
    NO_ERROR: _ClassVar[BadNames]
    OUT: _ClassVar[BadNames]
    OPTIONAL: _ClassVar[BadNames]
    NEAR: _ClassVar[BadNames]
    NO_DATA: _ClassVar[BadNames]
    REASON_UNKNOWN: _ClassVar[BadNames]
    SERVICE_DISABLED: _ClassVar[BadNames]
    SEVERITY_ERROR: _ClassVar[BadNames]
    STATUS_PENDING: _ClassVar[BadNames]
    STRICT: _ClassVar[BadNames]
    TYPE_BOOL: _ClassVar[BadNames]
    DEBUG: _ClassVar[BadNames]
GID_UNUSED: GID
UID_UNUSED: UID
PACKAGE: BadNames
PACKED: BadNames
linux: BadNames
DOMAIN: BadNames
TRUE: BadNames
FALSE: BadNames
CREATE_NEW: BadNames
DELETE: BadNames
DOUBLE_CLICK: BadNames
ERROR: BadNames
ERROR_BUSY: BadNames
ERROR_INSTALL_FAILED: BadNames
ERROR_NOT_FOUND: BadNames
GetClassName: BadNames
GetCurrentTime: BadNames
GetMessage: BadNames
GetObject: BadNames
IGNORE: BadNames
IN: BadNames
INPUT_KEYBOARD: BadNames
NO_ERROR: BadNames
OUT: BadNames
OPTIONAL: BadNames
NEAR: BadNames
NO_DATA: BadNames
REASON_UNKNOWN: BadNames
SERVICE_DISABLED: BadNames
SEVERITY_ERROR: BadNames
STATUS_PENDING: BadNames
STRICT: BadNames
TYPE_BOOL: BadNames
DEBUG: BadNames
