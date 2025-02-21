from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OnlyOneEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONLY_ONE_ENUM_DEFAULT: _ClassVar[OnlyOneEnum]
    ONLY_ONE_ENUM_VALID: _ClassVar[OnlyOneEnum]
ONLY_ONE_ENUM_DEFAULT: OnlyOneEnum
ONLY_ONE_ENUM_VALID: OnlyOneEnum
