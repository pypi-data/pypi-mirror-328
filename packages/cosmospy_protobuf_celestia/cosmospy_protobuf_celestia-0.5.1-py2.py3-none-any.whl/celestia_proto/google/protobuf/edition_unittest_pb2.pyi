from google.protobuf import cpp_features_pb2 as _cpp_features_pb2
from google.protobuf import unittest_import_pb2 as _unittest_import_pb2
from google.protobuf import unittest_import_public_pb2 as _unittest_import_public_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForeignEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOREIGN_FOO: _ClassVar[ForeignEnum]
    FOREIGN_BAR: _ClassVar[ForeignEnum]
    FOREIGN_BAZ: _ClassVar[ForeignEnum]
    FOREIGN_BAX: _ClassVar[ForeignEnum]

class TestReservedEnumFields(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[TestReservedEnumFields]

class TestEnumWithDupValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DUP_UNKNOWN1: _ClassVar[TestEnumWithDupValue]
    DUP_FOO1: _ClassVar[TestEnumWithDupValue]
    DUP_BAR1: _ClassVar[TestEnumWithDupValue]
    DUP_BAZ: _ClassVar[TestEnumWithDupValue]
    DUP_UNKNOWN2: _ClassVar[TestEnumWithDupValue]
    DUP_FOO2: _ClassVar[TestEnumWithDupValue]
    DUP_BAR2: _ClassVar[TestEnumWithDupValue]

class TestSparseEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPARSE_A: _ClassVar[TestSparseEnum]
    SPARSE_B: _ClassVar[TestSparseEnum]
    SPARSE_C: _ClassVar[TestSparseEnum]
    SPARSE_D: _ClassVar[TestSparseEnum]
    SPARSE_E: _ClassVar[TestSparseEnum]
    SPARSE_F: _ClassVar[TestSparseEnum]
    SPARSE_G: _ClassVar[TestSparseEnum]

class VeryLargeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENUM_LABEL_DEFAULT: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_1: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_2: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_3: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_4: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_5: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_6: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_7: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_8: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_9: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_10: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_11: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_12: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_13: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_14: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_15: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_16: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_17: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_18: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_19: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_20: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_21: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_22: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_23: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_24: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_25: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_26: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_27: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_28: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_29: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_30: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_31: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_32: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_33: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_34: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_35: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_36: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_37: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_38: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_39: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_40: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_41: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_42: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_43: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_44: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_45: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_46: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_47: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_48: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_49: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_50: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_51: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_52: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_53: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_54: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_55: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_56: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_57: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_58: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_59: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_60: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_61: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_62: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_63: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_64: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_65: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_66: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_67: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_68: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_69: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_70: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_71: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_72: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_73: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_74: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_75: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_76: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_77: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_78: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_79: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_80: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_81: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_82: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_83: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_84: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_85: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_86: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_87: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_88: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_89: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_90: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_91: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_92: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_93: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_94: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_95: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_96: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_97: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_98: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_99: _ClassVar[VeryLargeEnum]
    ENUM_LABEL_100: _ClassVar[VeryLargeEnum]
FOREIGN_FOO: ForeignEnum
FOREIGN_BAR: ForeignEnum
FOREIGN_BAZ: ForeignEnum
FOREIGN_BAX: ForeignEnum
UNKNOWN: TestReservedEnumFields
DUP_UNKNOWN1: TestEnumWithDupValue
DUP_FOO1: TestEnumWithDupValue
DUP_BAR1: TestEnumWithDupValue
DUP_BAZ: TestEnumWithDupValue
DUP_UNKNOWN2: TestEnumWithDupValue
DUP_FOO2: TestEnumWithDupValue
DUP_BAR2: TestEnumWithDupValue
SPARSE_A: TestSparseEnum
SPARSE_B: TestSparseEnum
SPARSE_C: TestSparseEnum
SPARSE_D: TestSparseEnum
SPARSE_E: TestSparseEnum
SPARSE_F: TestSparseEnum
SPARSE_G: TestSparseEnum
ENUM_LABEL_DEFAULT: VeryLargeEnum
ENUM_LABEL_1: VeryLargeEnum
ENUM_LABEL_2: VeryLargeEnum
ENUM_LABEL_3: VeryLargeEnum
ENUM_LABEL_4: VeryLargeEnum
ENUM_LABEL_5: VeryLargeEnum
ENUM_LABEL_6: VeryLargeEnum
ENUM_LABEL_7: VeryLargeEnum
ENUM_LABEL_8: VeryLargeEnum
ENUM_LABEL_9: VeryLargeEnum
ENUM_LABEL_10: VeryLargeEnum
ENUM_LABEL_11: VeryLargeEnum
ENUM_LABEL_12: VeryLargeEnum
ENUM_LABEL_13: VeryLargeEnum
ENUM_LABEL_14: VeryLargeEnum
ENUM_LABEL_15: VeryLargeEnum
ENUM_LABEL_16: VeryLargeEnum
ENUM_LABEL_17: VeryLargeEnum
ENUM_LABEL_18: VeryLargeEnum
ENUM_LABEL_19: VeryLargeEnum
ENUM_LABEL_20: VeryLargeEnum
ENUM_LABEL_21: VeryLargeEnum
ENUM_LABEL_22: VeryLargeEnum
ENUM_LABEL_23: VeryLargeEnum
ENUM_LABEL_24: VeryLargeEnum
ENUM_LABEL_25: VeryLargeEnum
ENUM_LABEL_26: VeryLargeEnum
ENUM_LABEL_27: VeryLargeEnum
ENUM_LABEL_28: VeryLargeEnum
ENUM_LABEL_29: VeryLargeEnum
ENUM_LABEL_30: VeryLargeEnum
ENUM_LABEL_31: VeryLargeEnum
ENUM_LABEL_32: VeryLargeEnum
ENUM_LABEL_33: VeryLargeEnum
ENUM_LABEL_34: VeryLargeEnum
ENUM_LABEL_35: VeryLargeEnum
ENUM_LABEL_36: VeryLargeEnum
ENUM_LABEL_37: VeryLargeEnum
ENUM_LABEL_38: VeryLargeEnum
ENUM_LABEL_39: VeryLargeEnum
ENUM_LABEL_40: VeryLargeEnum
ENUM_LABEL_41: VeryLargeEnum
ENUM_LABEL_42: VeryLargeEnum
ENUM_LABEL_43: VeryLargeEnum
ENUM_LABEL_44: VeryLargeEnum
ENUM_LABEL_45: VeryLargeEnum
ENUM_LABEL_46: VeryLargeEnum
ENUM_LABEL_47: VeryLargeEnum
ENUM_LABEL_48: VeryLargeEnum
ENUM_LABEL_49: VeryLargeEnum
ENUM_LABEL_50: VeryLargeEnum
ENUM_LABEL_51: VeryLargeEnum
ENUM_LABEL_52: VeryLargeEnum
ENUM_LABEL_53: VeryLargeEnum
ENUM_LABEL_54: VeryLargeEnum
ENUM_LABEL_55: VeryLargeEnum
ENUM_LABEL_56: VeryLargeEnum
ENUM_LABEL_57: VeryLargeEnum
ENUM_LABEL_58: VeryLargeEnum
ENUM_LABEL_59: VeryLargeEnum
ENUM_LABEL_60: VeryLargeEnum
ENUM_LABEL_61: VeryLargeEnum
ENUM_LABEL_62: VeryLargeEnum
ENUM_LABEL_63: VeryLargeEnum
ENUM_LABEL_64: VeryLargeEnum
ENUM_LABEL_65: VeryLargeEnum
ENUM_LABEL_66: VeryLargeEnum
ENUM_LABEL_67: VeryLargeEnum
ENUM_LABEL_68: VeryLargeEnum
ENUM_LABEL_69: VeryLargeEnum
ENUM_LABEL_70: VeryLargeEnum
ENUM_LABEL_71: VeryLargeEnum
ENUM_LABEL_72: VeryLargeEnum
ENUM_LABEL_73: VeryLargeEnum
ENUM_LABEL_74: VeryLargeEnum
ENUM_LABEL_75: VeryLargeEnum
ENUM_LABEL_76: VeryLargeEnum
ENUM_LABEL_77: VeryLargeEnum
ENUM_LABEL_78: VeryLargeEnum
ENUM_LABEL_79: VeryLargeEnum
ENUM_LABEL_80: VeryLargeEnum
ENUM_LABEL_81: VeryLargeEnum
ENUM_LABEL_82: VeryLargeEnum
ENUM_LABEL_83: VeryLargeEnum
ENUM_LABEL_84: VeryLargeEnum
ENUM_LABEL_85: VeryLargeEnum
ENUM_LABEL_86: VeryLargeEnum
ENUM_LABEL_87: VeryLargeEnum
ENUM_LABEL_88: VeryLargeEnum
ENUM_LABEL_89: VeryLargeEnum
ENUM_LABEL_90: VeryLargeEnum
ENUM_LABEL_91: VeryLargeEnum
ENUM_LABEL_92: VeryLargeEnum
ENUM_LABEL_93: VeryLargeEnum
ENUM_LABEL_94: VeryLargeEnum
ENUM_LABEL_95: VeryLargeEnum
ENUM_LABEL_96: VeryLargeEnum
ENUM_LABEL_97: VeryLargeEnum
ENUM_LABEL_98: VeryLargeEnum
ENUM_LABEL_99: VeryLargeEnum
ENUM_LABEL_100: VeryLargeEnum
OPTIONAL_INT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_int32_extension: _descriptor.FieldDescriptor
OPTIONAL_INT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_int64_extension: _descriptor.FieldDescriptor
OPTIONAL_UINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_uint32_extension: _descriptor.FieldDescriptor
OPTIONAL_UINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_uint64_extension: _descriptor.FieldDescriptor
OPTIONAL_SINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_sint32_extension: _descriptor.FieldDescriptor
OPTIONAL_SINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_sint64_extension: _descriptor.FieldDescriptor
OPTIONAL_FIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_fixed32_extension: _descriptor.FieldDescriptor
OPTIONAL_FIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_fixed64_extension: _descriptor.FieldDescriptor
OPTIONAL_SFIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_sfixed32_extension: _descriptor.FieldDescriptor
OPTIONAL_SFIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_sfixed64_extension: _descriptor.FieldDescriptor
OPTIONAL_FLOAT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_float_extension: _descriptor.FieldDescriptor
OPTIONAL_DOUBLE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_double_extension: _descriptor.FieldDescriptor
OPTIONAL_BOOL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_bool_extension: _descriptor.FieldDescriptor
OPTIONAL_STRING_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_string_extension: _descriptor.FieldDescriptor
OPTIONAL_BYTES_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_bytes_extension: _descriptor.FieldDescriptor
OPTIONALGROUP_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optionalgroup_extension: _descriptor.FieldDescriptor
OPTIONAL_NESTED_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_nested_message_extension: _descriptor.FieldDescriptor
OPTIONAL_FOREIGN_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_foreign_message_extension: _descriptor.FieldDescriptor
OPTIONAL_IMPORT_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_import_message_extension: _descriptor.FieldDescriptor
OPTIONAL_NESTED_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_nested_enum_extension: _descriptor.FieldDescriptor
OPTIONAL_FOREIGN_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_foreign_enum_extension: _descriptor.FieldDescriptor
OPTIONAL_IMPORT_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_import_enum_extension: _descriptor.FieldDescriptor
OPTIONAL_STRING_PIECE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_string_piece_extension: _descriptor.FieldDescriptor
OPTIONAL_CORD_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_cord_extension: _descriptor.FieldDescriptor
OPTIONAL_BYTES_CORD_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_bytes_cord_extension: _descriptor.FieldDescriptor
OPTIONAL_PUBLIC_IMPORT_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_public_import_message_extension: _descriptor.FieldDescriptor
OPTIONAL_LAZY_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_lazy_message_extension: _descriptor.FieldDescriptor
OPTIONAL_UNVERIFIED_LAZY_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_unverified_lazy_message_extension: _descriptor.FieldDescriptor
REPEATED_INT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_int32_extension: _descriptor.FieldDescriptor
REPEATED_INT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_int64_extension: _descriptor.FieldDescriptor
REPEATED_UINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_uint32_extension: _descriptor.FieldDescriptor
REPEATED_UINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_uint64_extension: _descriptor.FieldDescriptor
REPEATED_SINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_sint32_extension: _descriptor.FieldDescriptor
REPEATED_SINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_sint64_extension: _descriptor.FieldDescriptor
REPEATED_FIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_fixed32_extension: _descriptor.FieldDescriptor
REPEATED_FIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_fixed64_extension: _descriptor.FieldDescriptor
REPEATED_SFIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_sfixed32_extension: _descriptor.FieldDescriptor
REPEATED_SFIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_sfixed64_extension: _descriptor.FieldDescriptor
REPEATED_FLOAT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_float_extension: _descriptor.FieldDescriptor
REPEATED_DOUBLE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_double_extension: _descriptor.FieldDescriptor
REPEATED_BOOL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_bool_extension: _descriptor.FieldDescriptor
REPEATED_STRING_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_string_extension: _descriptor.FieldDescriptor
REPEATED_BYTES_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_bytes_extension: _descriptor.FieldDescriptor
REPEATEDGROUP_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeatedgroup_extension: _descriptor.FieldDescriptor
REPEATED_NESTED_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_nested_message_extension: _descriptor.FieldDescriptor
REPEATED_FOREIGN_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_foreign_message_extension: _descriptor.FieldDescriptor
REPEATED_IMPORT_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_import_message_extension: _descriptor.FieldDescriptor
REPEATED_NESTED_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_nested_enum_extension: _descriptor.FieldDescriptor
REPEATED_FOREIGN_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_foreign_enum_extension: _descriptor.FieldDescriptor
REPEATED_IMPORT_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_import_enum_extension: _descriptor.FieldDescriptor
REPEATED_STRING_PIECE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_string_piece_extension: _descriptor.FieldDescriptor
REPEATED_CORD_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_cord_extension: _descriptor.FieldDescriptor
REPEATED_LAZY_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_lazy_message_extension: _descriptor.FieldDescriptor
DEFAULT_INT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_int32_extension: _descriptor.FieldDescriptor
DEFAULT_INT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_int64_extension: _descriptor.FieldDescriptor
DEFAULT_UINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_uint32_extension: _descriptor.FieldDescriptor
DEFAULT_UINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_uint64_extension: _descriptor.FieldDescriptor
DEFAULT_SINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_sint32_extension: _descriptor.FieldDescriptor
DEFAULT_SINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_sint64_extension: _descriptor.FieldDescriptor
DEFAULT_FIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_fixed32_extension: _descriptor.FieldDescriptor
DEFAULT_FIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_fixed64_extension: _descriptor.FieldDescriptor
DEFAULT_SFIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_sfixed32_extension: _descriptor.FieldDescriptor
DEFAULT_SFIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_sfixed64_extension: _descriptor.FieldDescriptor
DEFAULT_FLOAT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_float_extension: _descriptor.FieldDescriptor
DEFAULT_DOUBLE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_double_extension: _descriptor.FieldDescriptor
DEFAULT_BOOL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_bool_extension: _descriptor.FieldDescriptor
DEFAULT_STRING_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_string_extension: _descriptor.FieldDescriptor
DEFAULT_BYTES_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_bytes_extension: _descriptor.FieldDescriptor
DEFAULT_NESTED_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_nested_enum_extension: _descriptor.FieldDescriptor
DEFAULT_FOREIGN_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_foreign_enum_extension: _descriptor.FieldDescriptor
DEFAULT_IMPORT_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_import_enum_extension: _descriptor.FieldDescriptor
DEFAULT_STRING_PIECE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_string_piece_extension: _descriptor.FieldDescriptor
DEFAULT_CORD_EXTENSION_FIELD_NUMBER: _ClassVar[int]
default_cord_extension: _descriptor.FieldDescriptor
ONEOF_UINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
oneof_uint32_extension: _descriptor.FieldDescriptor
ONEOF_NESTED_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
oneof_nested_message_extension: _descriptor.FieldDescriptor
ONEOF_STRING_EXTENSION_FIELD_NUMBER: _ClassVar[int]
oneof_string_extension: _descriptor.FieldDescriptor
ONEOF_BYTES_EXTENSION_FIELD_NUMBER: _ClassVar[int]
oneof_bytes_extension: _descriptor.FieldDescriptor
MY_EXTENSION_STRING_FIELD_NUMBER: _ClassVar[int]
my_extension_string: _descriptor.FieldDescriptor
MY_EXTENSION_INT_FIELD_NUMBER: _ClassVar[int]
my_extension_int: _descriptor.FieldDescriptor
PACKED_INT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_int32_extension: _descriptor.FieldDescriptor
PACKED_INT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_int64_extension: _descriptor.FieldDescriptor
PACKED_UINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_uint32_extension: _descriptor.FieldDescriptor
PACKED_UINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_uint64_extension: _descriptor.FieldDescriptor
PACKED_SINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_sint32_extension: _descriptor.FieldDescriptor
PACKED_SINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_sint64_extension: _descriptor.FieldDescriptor
PACKED_FIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_fixed32_extension: _descriptor.FieldDescriptor
PACKED_FIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_fixed64_extension: _descriptor.FieldDescriptor
PACKED_SFIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_sfixed32_extension: _descriptor.FieldDescriptor
PACKED_SFIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_sfixed64_extension: _descriptor.FieldDescriptor
PACKED_FLOAT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_float_extension: _descriptor.FieldDescriptor
PACKED_DOUBLE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_double_extension: _descriptor.FieldDescriptor
PACKED_BOOL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_bool_extension: _descriptor.FieldDescriptor
PACKED_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
packed_enum_extension: _descriptor.FieldDescriptor
UNPACKED_INT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_int32_extension: _descriptor.FieldDescriptor
UNPACKED_INT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_int64_extension: _descriptor.FieldDescriptor
UNPACKED_UINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_uint32_extension: _descriptor.FieldDescriptor
UNPACKED_UINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_uint64_extension: _descriptor.FieldDescriptor
UNPACKED_SINT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_sint32_extension: _descriptor.FieldDescriptor
UNPACKED_SINT64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_sint64_extension: _descriptor.FieldDescriptor
UNPACKED_FIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_fixed32_extension: _descriptor.FieldDescriptor
UNPACKED_FIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_fixed64_extension: _descriptor.FieldDescriptor
UNPACKED_SFIXED32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_sfixed32_extension: _descriptor.FieldDescriptor
UNPACKED_SFIXED64_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_sfixed64_extension: _descriptor.FieldDescriptor
UNPACKED_FLOAT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_float_extension: _descriptor.FieldDescriptor
UNPACKED_DOUBLE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_double_extension: _descriptor.FieldDescriptor
UNPACKED_BOOL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_bool_extension: _descriptor.FieldDescriptor
UNPACKED_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
unpacked_enum_extension: _descriptor.FieldDescriptor
TEST_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
test_all_types: _descriptor.FieldDescriptor
TEST_EXTENSION_INSIDE_TABLE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
test_extension_inside_table_extension: _descriptor.FieldDescriptor
INNER_FIELD_NUMBER: _ClassVar[int]
inner: _descriptor.FieldDescriptor

class TestAllTypes(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optionalgroup", "optional_nested_message", "optional_foreign_message", "optional_import_message", "optional_nested_enum", "optional_foreign_enum", "optional_import_enum", "optional_string_piece", "optional_cord", "optional_bytes_cord", "optional_public_import_message", "optional_lazy_message", "optional_unverified_lazy_message", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeatedgroup", "repeated_nested_message", "repeated_foreign_message", "repeated_import_message", "repeated_nested_enum", "repeated_foreign_enum", "repeated_import_enum", "repeated_string_piece", "repeated_cord", "repeated_lazy_message", "default_int32", "default_int64", "default_uint32", "default_uint64", "default_sint32", "default_sint64", "default_fixed32", "default_fixed64", "default_sfixed32", "default_sfixed64", "default_float", "default_double", "default_bool", "default_string", "default_bytes", "default_nested_enum", "default_foreign_enum", "default_import_enum", "default_string_piece", "default_cord", "oneof_uint32", "oneof_nested_message", "oneof_string", "oneof_bytes", "oneof_cord", "oneof_string_piece", "oneof_lazy_nested_message")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[TestAllTypes.NestedEnum]
        BAR: _ClassVar[TestAllTypes.NestedEnum]
        BAZ: _ClassVar[TestAllTypes.NestedEnum]
        NEG: _ClassVar[TestAllTypes.NestedEnum]
    FOO: TestAllTypes.NestedEnum
    BAR: TestAllTypes.NestedEnum
    BAZ: TestAllTypes.NestedEnum
    NEG: TestAllTypes.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("bb",)
        BB_FIELD_NUMBER: _ClassVar[int]
        bb: int
        def __init__(self, bb: _Optional[int] = ...) -> None: ...
    class OptionalGroup(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    class RepeatedGroup(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SINT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIXED32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIXED64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BOOL_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_IMPORT_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_CORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PUBLIC_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UNVERIFIED_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SINT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SINT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_IMPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_IMPORT_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CORD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INT32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INT64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_UINT32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_UINT64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SINT32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SINT64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIXED32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIXED64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BOOL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STRING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BYTES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_IMPORT_ENUM_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CORD_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    ONEOF_CORD_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_LAZY_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    optional_int32: int
    optional_int64: int
    optional_uint32: int
    optional_uint64: int
    optional_sint32: int
    optional_sint64: int
    optional_fixed32: int
    optional_fixed64: int
    optional_sfixed32: int
    optional_sfixed64: int
    optional_float: float
    optional_double: float
    optional_bool: bool
    optional_string: str
    optional_bytes: bytes
    optionalgroup: TestAllTypes.OptionalGroup
    optional_nested_message: TestAllTypes.NestedMessage
    optional_foreign_message: ForeignMessage
    optional_import_message: _unittest_import_pb2.ImportMessage
    optional_nested_enum: TestAllTypes.NestedEnum
    optional_foreign_enum: ForeignEnum
    optional_import_enum: _unittest_import_pb2.ImportEnum
    optional_string_piece: str
    optional_cord: str
    optional_bytes_cord: bytes
    optional_public_import_message: _unittest_import_public_pb2.PublicImportMessage
    optional_lazy_message: TestAllTypes.NestedMessage
    optional_unverified_lazy_message: TestAllTypes.NestedMessage
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    repeated_int64: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint32: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint64: _containers.RepeatedScalarFieldContainer[int]
    repeated_sint32: _containers.RepeatedScalarFieldContainer[int]
    repeated_sint64: _containers.RepeatedScalarFieldContainer[int]
    repeated_fixed32: _containers.RepeatedScalarFieldContainer[int]
    repeated_fixed64: _containers.RepeatedScalarFieldContainer[int]
    repeated_sfixed32: _containers.RepeatedScalarFieldContainer[int]
    repeated_sfixed64: _containers.RepeatedScalarFieldContainer[int]
    repeated_float: _containers.RepeatedScalarFieldContainer[float]
    repeated_double: _containers.RepeatedScalarFieldContainer[float]
    repeated_bool: _containers.RepeatedScalarFieldContainer[bool]
    repeated_string: _containers.RepeatedScalarFieldContainer[str]
    repeated_bytes: _containers.RepeatedScalarFieldContainer[bytes]
    repeatedgroup: _containers.RepeatedCompositeFieldContainer[TestAllTypes.RepeatedGroup]
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]
    repeated_foreign_message: _containers.RepeatedCompositeFieldContainer[ForeignMessage]
    repeated_import_message: _containers.RepeatedCompositeFieldContainer[_unittest_import_pb2.ImportMessage]
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypes.NestedEnum]
    repeated_foreign_enum: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    repeated_import_enum: _containers.RepeatedScalarFieldContainer[_unittest_import_pb2.ImportEnum]
    repeated_string_piece: _containers.RepeatedScalarFieldContainer[str]
    repeated_cord: _containers.RepeatedScalarFieldContainer[str]
    repeated_lazy_message: _containers.RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]
    default_int32: int
    default_int64: int
    default_uint32: int
    default_uint64: int
    default_sint32: int
    default_sint64: int
    default_fixed32: int
    default_fixed64: int
    default_sfixed32: int
    default_sfixed64: int
    default_float: float
    default_double: float
    default_bool: bool
    default_string: str
    default_bytes: bytes
    default_nested_enum: TestAllTypes.NestedEnum
    default_foreign_enum: ForeignEnum
    default_import_enum: _unittest_import_pb2.ImportEnum
    default_string_piece: str
    default_cord: str
    oneof_uint32: int
    oneof_nested_message: TestAllTypes.NestedMessage
    oneof_string: str
    oneof_bytes: bytes
    oneof_cord: str
    oneof_string_piece: str
    oneof_lazy_nested_message: TestAllTypes.NestedMessage
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optionalgroup: _Optional[_Union[TestAllTypes.OptionalGroup, _Mapping]] = ..., optional_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_foreign_message: _Optional[_Union[ForeignMessage, _Mapping]] = ..., optional_import_message: _Optional[_Union[_unittest_import_pb2.ImportMessage, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestAllTypes.NestedEnum, str]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnum, str]] = ..., optional_import_enum: _Optional[_Union[_unittest_import_pb2.ImportEnum, str]] = ..., optional_string_piece: _Optional[str] = ..., optional_cord: _Optional[str] = ..., optional_bytes_cord: _Optional[bytes] = ..., optional_public_import_message: _Optional[_Union[_unittest_import_public_pb2.PublicImportMessage, _Mapping]] = ..., optional_lazy_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_unverified_lazy_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeatedgroup: _Optional[_Iterable[_Union[TestAllTypes.RepeatedGroup, _Mapping]]] = ..., repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., repeated_foreign_message: _Optional[_Iterable[_Union[ForeignMessage, _Mapping]]] = ..., repeated_import_message: _Optional[_Iterable[_Union[_unittest_import_pb2.ImportMessage, _Mapping]]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypes.NestedEnum, str]]] = ..., repeated_foreign_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ..., repeated_import_enum: _Optional[_Iterable[_Union[_unittest_import_pb2.ImportEnum, str]]] = ..., repeated_string_piece: _Optional[_Iterable[str]] = ..., repeated_cord: _Optional[_Iterable[str]] = ..., repeated_lazy_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., default_int32: _Optional[int] = ..., default_int64: _Optional[int] = ..., default_uint32: _Optional[int] = ..., default_uint64: _Optional[int] = ..., default_sint32: _Optional[int] = ..., default_sint64: _Optional[int] = ..., default_fixed32: _Optional[int] = ..., default_fixed64: _Optional[int] = ..., default_sfixed32: _Optional[int] = ..., default_sfixed64: _Optional[int] = ..., default_float: _Optional[float] = ..., default_double: _Optional[float] = ..., default_bool: bool = ..., default_string: _Optional[str] = ..., default_bytes: _Optional[bytes] = ..., default_nested_enum: _Optional[_Union[TestAllTypes.NestedEnum, str]] = ..., default_foreign_enum: _Optional[_Union[ForeignEnum, str]] = ..., default_import_enum: _Optional[_Union[_unittest_import_pb2.ImportEnum, str]] = ..., default_string_piece: _Optional[str] = ..., default_cord: _Optional[str] = ..., oneof_uint32: _Optional[int] = ..., oneof_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ..., oneof_cord: _Optional[str] = ..., oneof_string_piece: _Optional[str] = ..., oneof_lazy_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ...) -> None: ...

class NestedTestAllTypes(_message.Message):
    __slots__ = ("child", "payload", "repeated_child", "lazy_child", "eager_child")
    CHILD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CHILD_FIELD_NUMBER: _ClassVar[int]
    LAZY_CHILD_FIELD_NUMBER: _ClassVar[int]
    EAGER_CHILD_FIELD_NUMBER: _ClassVar[int]
    child: NestedTestAllTypes
    payload: TestAllTypes
    repeated_child: _containers.RepeatedCompositeFieldContainer[NestedTestAllTypes]
    lazy_child: NestedTestAllTypes
    eager_child: TestAllTypes
    def __init__(self, child: _Optional[_Union[NestedTestAllTypes, _Mapping]] = ..., payload: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_child: _Optional[_Iterable[_Union[NestedTestAllTypes, _Mapping]]] = ..., lazy_child: _Optional[_Union[NestedTestAllTypes, _Mapping]] = ..., eager_child: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...

class TestDeprecatedFields(_message.Message):
    __slots__ = ("deprecated_int32", "deprecated_repeated_string", "deprecated_message", "deprecated_int32_in_oneof", "nested")
    DEPRECATED_INT32_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_INT32_IN_ONEOF_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    deprecated_int32: int
    deprecated_repeated_string: _containers.RepeatedScalarFieldContainer[str]
    deprecated_message: TestAllTypes.NestedMessage
    deprecated_int32_in_oneof: int
    nested: TestDeprecatedFields
    def __init__(self, deprecated_int32: _Optional[int] = ..., deprecated_repeated_string: _Optional[_Iterable[str]] = ..., deprecated_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., deprecated_int32_in_oneof: _Optional[int] = ..., nested: _Optional[_Union[TestDeprecatedFields, _Mapping]] = ...) -> None: ...

class TestDeprecatedMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ForeignMessage(_message.Message):
    __slots__ = ("c", "d")
    C_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    c: int
    d: int
    def __init__(self, c: _Optional[int] = ..., d: _Optional[int] = ...) -> None: ...

class TestReservedFields(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestAllExtensions(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class OptionalGroup_extension(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class RepeatedGroup_extension(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class TestMixedFieldsAndExtensions(_message.Message):
    __slots__ = ("a", "b")
    Extensions: _python_message._ExtensionDict
    C_FIELD_NUMBER: _ClassVar[int]
    c: _descriptor.FieldDescriptor
    D_FIELD_NUMBER: _ClassVar[int]
    d: _descriptor.FieldDescriptor
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, a: _Optional[int] = ..., b: _Optional[_Iterable[int]] = ...) -> None: ...

class TestGroup(_message.Message):
    __slots__ = ("optionalgroup", "optional_foreign_enum")
    class OptionalGroup(_message.Message):
        __slots__ = ("a", "zz")
        A_FIELD_NUMBER: _ClassVar[int]
        ZZ_FIELD_NUMBER: _ClassVar[int]
        a: int
        zz: int
        def __init__(self, a: _Optional[int] = ..., zz: _Optional[int] = ...) -> None: ...
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    optionalgroup: TestGroup.OptionalGroup
    optional_foreign_enum: ForeignEnum
    def __init__(self, optionalgroup: _Optional[_Union[TestGroup.OptionalGroup, _Mapping]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnum, str]] = ...) -> None: ...

class TestGroupExtension(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestNestedExtension(_message.Message):
    __slots__ = ()
    class OptionalGroup_extension(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    TEST_FIELD_NUMBER: _ClassVar[int]
    test: _descriptor.FieldDescriptor
    NESTED_STRING_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    nested_string_extension: _descriptor.FieldDescriptor
    OPTIONALGROUP_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    optionalgroup_extension: _descriptor.FieldDescriptor
    OPTIONAL_FOREIGN_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    optional_foreign_enum_extension: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class TestChildExtension(_message.Message):
    __slots__ = ("a", "b", "optional_extension")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    a: str
    b: str
    optional_extension: TestAllExtensions
    def __init__(self, a: _Optional[str] = ..., b: _Optional[str] = ..., optional_extension: _Optional[_Union[TestAllExtensions, _Mapping]] = ...) -> None: ...

class TestChildExtensionData(_message.Message):
    __slots__ = ("a", "b", "optional_extension")
    class NestedTestAllExtensionsData(_message.Message):
        __slots__ = ("dynamic",)
        class NestedDynamicExtensions(_message.Message):
            __slots__ = ("a", "b")
            A_FIELD_NUMBER: _ClassVar[int]
            B_FIELD_NUMBER: _ClassVar[int]
            a: int
            b: int
            def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...
        DYNAMIC_FIELD_NUMBER: _ClassVar[int]
        dynamic: TestChildExtensionData.NestedTestAllExtensionsData.NestedDynamicExtensions
        def __init__(self, dynamic: _Optional[_Union[TestChildExtensionData.NestedTestAllExtensionsData.NestedDynamicExtensions, _Mapping]] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    a: str
    b: str
    optional_extension: TestChildExtensionData.NestedTestAllExtensionsData
    def __init__(self, a: _Optional[str] = ..., b: _Optional[str] = ..., optional_extension: _Optional[_Union[TestChildExtensionData.NestedTestAllExtensionsData, _Mapping]] = ...) -> None: ...

class TestNestedChildExtension(_message.Message):
    __slots__ = ("a", "child")
    A_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    a: int
    child: TestChildExtension
    def __init__(self, a: _Optional[int] = ..., child: _Optional[_Union[TestChildExtension, _Mapping]] = ...) -> None: ...

class TestNestedChildExtensionData(_message.Message):
    __slots__ = ("a", "child")
    A_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    a: int
    child: TestChildExtensionData
    def __init__(self, a: _Optional[int] = ..., child: _Optional[_Union[TestChildExtensionData, _Mapping]] = ...) -> None: ...

class TestRequiredEnum(_message.Message):
    __slots__ = ("required_enum", "a")
    REQUIRED_ENUM_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    required_enum: ForeignEnum
    a: int
    def __init__(self, required_enum: _Optional[_Union[ForeignEnum, str]] = ..., a: _Optional[int] = ...) -> None: ...

class TestRequiredEnumNoMask(_message.Message):
    __slots__ = ("required_enum", "a")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TestRequiredEnumNoMask.NestedEnum]
        FOO: _ClassVar[TestRequiredEnumNoMask.NestedEnum]
        BAR: _ClassVar[TestRequiredEnumNoMask.NestedEnum]
        BAZ: _ClassVar[TestRequiredEnumNoMask.NestedEnum]
    UNSPECIFIED: TestRequiredEnumNoMask.NestedEnum
    FOO: TestRequiredEnumNoMask.NestedEnum
    BAR: TestRequiredEnumNoMask.NestedEnum
    BAZ: TestRequiredEnumNoMask.NestedEnum
    REQUIRED_ENUM_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    required_enum: TestRequiredEnumNoMask.NestedEnum
    a: int
    def __init__(self, required_enum: _Optional[_Union[TestRequiredEnumNoMask.NestedEnum, str]] = ..., a: _Optional[int] = ...) -> None: ...

class TestRequiredEnumMulti(_message.Message):
    __slots__ = ("required_enum_4", "a_3", "required_enum_2", "required_enum_1")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TestRequiredEnumMulti.NestedEnum]
        FOO: _ClassVar[TestRequiredEnumMulti.NestedEnum]
        BAR: _ClassVar[TestRequiredEnumMulti.NestedEnum]
        BAZ: _ClassVar[TestRequiredEnumMulti.NestedEnum]
    UNSPECIFIED: TestRequiredEnumMulti.NestedEnum
    FOO: TestRequiredEnumMulti.NestedEnum
    BAR: TestRequiredEnumMulti.NestedEnum
    BAZ: TestRequiredEnumMulti.NestedEnum
    REQUIRED_ENUM_4_FIELD_NUMBER: _ClassVar[int]
    A_3_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_2_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_1_FIELD_NUMBER: _ClassVar[int]
    required_enum_4: TestRequiredEnumMulti.NestedEnum
    a_3: int
    required_enum_2: TestRequiredEnumMulti.NestedEnum
    required_enum_1: ForeignEnum
    def __init__(self, required_enum_4: _Optional[_Union[TestRequiredEnumMulti.NestedEnum, str]] = ..., a_3: _Optional[int] = ..., required_enum_2: _Optional[_Union[TestRequiredEnumMulti.NestedEnum, str]] = ..., required_enum_1: _Optional[_Union[ForeignEnum, str]] = ...) -> None: ...

class TestRequiredNoMaskMulti(_message.Message):
    __slots__ = ("required_fixed32_80", "required_fixed32_70", "required_enum_64", "required_enum_4", "a_3", "required_enum_2", "required_enum_1")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TestRequiredNoMaskMulti.NestedEnum]
        FOO: _ClassVar[TestRequiredNoMaskMulti.NestedEnum]
        BAR: _ClassVar[TestRequiredNoMaskMulti.NestedEnum]
        BAZ: _ClassVar[TestRequiredNoMaskMulti.NestedEnum]
    UNSPECIFIED: TestRequiredNoMaskMulti.NestedEnum
    FOO: TestRequiredNoMaskMulti.NestedEnum
    BAR: TestRequiredNoMaskMulti.NestedEnum
    BAZ: TestRequiredNoMaskMulti.NestedEnum
    REQUIRED_FIXED32_80_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIXED32_70_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_64_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_4_FIELD_NUMBER: _ClassVar[int]
    A_3_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_2_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_1_FIELD_NUMBER: _ClassVar[int]
    required_fixed32_80: int
    required_fixed32_70: int
    required_enum_64: TestRequiredNoMaskMulti.NestedEnum
    required_enum_4: TestRequiredNoMaskMulti.NestedEnum
    a_3: int
    required_enum_2: TestRequiredNoMaskMulti.NestedEnum
    required_enum_1: ForeignEnum
    def __init__(self, required_fixed32_80: _Optional[int] = ..., required_fixed32_70: _Optional[int] = ..., required_enum_64: _Optional[_Union[TestRequiredNoMaskMulti.NestedEnum, str]] = ..., required_enum_4: _Optional[_Union[TestRequiredNoMaskMulti.NestedEnum, str]] = ..., a_3: _Optional[int] = ..., required_enum_2: _Optional[_Union[TestRequiredNoMaskMulti.NestedEnum, str]] = ..., required_enum_1: _Optional[_Union[ForeignEnum, str]] = ...) -> None: ...

class TestRequired(_message.Message):
    __slots__ = ("a", "dummy2", "b", "dummy4", "dummy5", "dummy6", "dummy7", "dummy8", "dummy9", "dummy10", "dummy11", "dummy12", "dummy13", "dummy14", "dummy15", "dummy16", "dummy17", "dummy18", "dummy19", "dummy20", "dummy21", "dummy22", "dummy23", "dummy24", "dummy25", "dummy26", "dummy27", "dummy28", "dummy29", "dummy30", "dummy31", "dummy32", "c", "optional_foreign")
    SINGLE_FIELD_NUMBER: _ClassVar[int]
    single: _descriptor.FieldDescriptor
    MULTI_FIELD_NUMBER: _ClassVar[int]
    multi: _descriptor.FieldDescriptor
    A_FIELD_NUMBER: _ClassVar[int]
    DUMMY2_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    DUMMY4_FIELD_NUMBER: _ClassVar[int]
    DUMMY5_FIELD_NUMBER: _ClassVar[int]
    DUMMY6_FIELD_NUMBER: _ClassVar[int]
    DUMMY7_FIELD_NUMBER: _ClassVar[int]
    DUMMY8_FIELD_NUMBER: _ClassVar[int]
    DUMMY9_FIELD_NUMBER: _ClassVar[int]
    DUMMY10_FIELD_NUMBER: _ClassVar[int]
    DUMMY11_FIELD_NUMBER: _ClassVar[int]
    DUMMY12_FIELD_NUMBER: _ClassVar[int]
    DUMMY13_FIELD_NUMBER: _ClassVar[int]
    DUMMY14_FIELD_NUMBER: _ClassVar[int]
    DUMMY15_FIELD_NUMBER: _ClassVar[int]
    DUMMY16_FIELD_NUMBER: _ClassVar[int]
    DUMMY17_FIELD_NUMBER: _ClassVar[int]
    DUMMY18_FIELD_NUMBER: _ClassVar[int]
    DUMMY19_FIELD_NUMBER: _ClassVar[int]
    DUMMY20_FIELD_NUMBER: _ClassVar[int]
    DUMMY21_FIELD_NUMBER: _ClassVar[int]
    DUMMY22_FIELD_NUMBER: _ClassVar[int]
    DUMMY23_FIELD_NUMBER: _ClassVar[int]
    DUMMY24_FIELD_NUMBER: _ClassVar[int]
    DUMMY25_FIELD_NUMBER: _ClassVar[int]
    DUMMY26_FIELD_NUMBER: _ClassVar[int]
    DUMMY27_FIELD_NUMBER: _ClassVar[int]
    DUMMY28_FIELD_NUMBER: _ClassVar[int]
    DUMMY29_FIELD_NUMBER: _ClassVar[int]
    DUMMY30_FIELD_NUMBER: _ClassVar[int]
    DUMMY31_FIELD_NUMBER: _ClassVar[int]
    DUMMY32_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_FIELD_NUMBER: _ClassVar[int]
    a: int
    dummy2: int
    b: int
    dummy4: int
    dummy5: int
    dummy6: int
    dummy7: int
    dummy8: int
    dummy9: int
    dummy10: int
    dummy11: int
    dummy12: int
    dummy13: int
    dummy14: int
    dummy15: int
    dummy16: int
    dummy17: int
    dummy18: int
    dummy19: int
    dummy20: int
    dummy21: int
    dummy22: int
    dummy23: int
    dummy24: int
    dummy25: int
    dummy26: int
    dummy27: int
    dummy28: int
    dummy29: int
    dummy30: int
    dummy31: int
    dummy32: int
    c: int
    optional_foreign: ForeignMessage
    def __init__(self, a: _Optional[int] = ..., dummy2: _Optional[int] = ..., b: _Optional[int] = ..., dummy4: _Optional[int] = ..., dummy5: _Optional[int] = ..., dummy6: _Optional[int] = ..., dummy7: _Optional[int] = ..., dummy8: _Optional[int] = ..., dummy9: _Optional[int] = ..., dummy10: _Optional[int] = ..., dummy11: _Optional[int] = ..., dummy12: _Optional[int] = ..., dummy13: _Optional[int] = ..., dummy14: _Optional[int] = ..., dummy15: _Optional[int] = ..., dummy16: _Optional[int] = ..., dummy17: _Optional[int] = ..., dummy18: _Optional[int] = ..., dummy19: _Optional[int] = ..., dummy20: _Optional[int] = ..., dummy21: _Optional[int] = ..., dummy22: _Optional[int] = ..., dummy23: _Optional[int] = ..., dummy24: _Optional[int] = ..., dummy25: _Optional[int] = ..., dummy26: _Optional[int] = ..., dummy27: _Optional[int] = ..., dummy28: _Optional[int] = ..., dummy29: _Optional[int] = ..., dummy30: _Optional[int] = ..., dummy31: _Optional[int] = ..., dummy32: _Optional[int] = ..., c: _Optional[int] = ..., optional_foreign: _Optional[_Union[ForeignMessage, _Mapping]] = ...) -> None: ...

class TestRequiredForeign(_message.Message):
    __slots__ = ("optional_message", "repeated_message", "dummy", "optional_lazy_message")
    OPTIONAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    optional_message: TestRequired
    repeated_message: _containers.RepeatedCompositeFieldContainer[TestRequired]
    dummy: int
    optional_lazy_message: NestedTestAllTypes
    def __init__(self, optional_message: _Optional[_Union[TestRequired, _Mapping]] = ..., repeated_message: _Optional[_Iterable[_Union[TestRequired, _Mapping]]] = ..., dummy: _Optional[int] = ..., optional_lazy_message: _Optional[_Union[NestedTestAllTypes, _Mapping]] = ...) -> None: ...

class TestRequiredMessage(_message.Message):
    __slots__ = ("optional_message", "repeated_message", "required_message")
    OPTIONAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    optional_message: TestRequired
    repeated_message: _containers.RepeatedCompositeFieldContainer[TestRequired]
    required_message: TestRequired
    def __init__(self, optional_message: _Optional[_Union[TestRequired, _Mapping]] = ..., repeated_message: _Optional[_Iterable[_Union[TestRequired, _Mapping]]] = ..., required_message: _Optional[_Union[TestRequired, _Mapping]] = ...) -> None: ...

class TestNestedRequiredForeign(_message.Message):
    __slots__ = ("child", "payload", "dummy", "required_enum", "required_enum_no_mask", "required_enum_multi", "required_no_mask")
    CHILD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_NO_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENUM_MULTI_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_NO_MASK_FIELD_NUMBER: _ClassVar[int]
    child: TestNestedRequiredForeign
    payload: TestRequiredForeign
    dummy: int
    required_enum: TestRequiredEnum
    required_enum_no_mask: TestRequiredEnumNoMask
    required_enum_multi: TestRequiredEnumMulti
    required_no_mask: TestRequiredNoMaskMulti
    def __init__(self, child: _Optional[_Union[TestNestedRequiredForeign, _Mapping]] = ..., payload: _Optional[_Union[TestRequiredForeign, _Mapping]] = ..., dummy: _Optional[int] = ..., required_enum: _Optional[_Union[TestRequiredEnum, _Mapping]] = ..., required_enum_no_mask: _Optional[_Union[TestRequiredEnumNoMask, _Mapping]] = ..., required_enum_multi: _Optional[_Union[TestRequiredEnumMulti, _Mapping]] = ..., required_no_mask: _Optional[_Union[TestRequiredNoMaskMulti, _Mapping]] = ...) -> None: ...

class TestForeignNested(_message.Message):
    __slots__ = ("foreign_nested",)
    FOREIGN_NESTED_FIELD_NUMBER: _ClassVar[int]
    foreign_nested: TestAllTypes.NestedMessage
    def __init__(self, foreign_nested: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ...) -> None: ...

class TestEmptyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestEmptyMessageWithExtensions(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestPickleNestedMessage(_message.Message):
    __slots__ = ()
    class NestedMessage(_message.Message):
        __slots__ = ("bb",)
        class NestedNestedMessage(_message.Message):
            __slots__ = ("cc",)
            CC_FIELD_NUMBER: _ClassVar[int]
            cc: int
            def __init__(self, cc: _Optional[int] = ...) -> None: ...
        BB_FIELD_NUMBER: _ClassVar[int]
        bb: int
        def __init__(self, bb: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class TestMultipleExtensionRanges(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestReallyLargeTagNumber(_message.Message):
    __slots__ = ("a", "bb")
    A_FIELD_NUMBER: _ClassVar[int]
    BB_FIELD_NUMBER: _ClassVar[int]
    a: int
    bb: int
    def __init__(self, a: _Optional[int] = ..., bb: _Optional[int] = ...) -> None: ...

class TestRecursiveMessage(_message.Message):
    __slots__ = ("a", "i")
    A_FIELD_NUMBER: _ClassVar[int]
    I_FIELD_NUMBER: _ClassVar[int]
    a: TestRecursiveMessage
    i: int
    def __init__(self, a: _Optional[_Union[TestRecursiveMessage, _Mapping]] = ..., i: _Optional[int] = ...) -> None: ...

class TestMutualRecursionA(_message.Message):
    __slots__ = ("bb", "subgroup", "subgroupr")
    class SubMessage(_message.Message):
        __slots__ = ("b",)
        B_FIELD_NUMBER: _ClassVar[int]
        b: TestMutualRecursionB
        def __init__(self, b: _Optional[_Union[TestMutualRecursionB, _Mapping]] = ...) -> None: ...
    class SubGroup(_message.Message):
        __slots__ = ("sub_message", "not_in_this_scc")
        SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NOT_IN_THIS_SCC_FIELD_NUMBER: _ClassVar[int]
        sub_message: TestMutualRecursionA.SubMessage
        not_in_this_scc: TestAllTypes
        def __init__(self, sub_message: _Optional[_Union[TestMutualRecursionA.SubMessage, _Mapping]] = ..., not_in_this_scc: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...
    class SubGroupR(_message.Message):
        __slots__ = ("payload",)
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        payload: TestAllTypes
        def __init__(self, payload: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...
    BB_FIELD_NUMBER: _ClassVar[int]
    SUBGROUP_FIELD_NUMBER: _ClassVar[int]
    SUBGROUPR_FIELD_NUMBER: _ClassVar[int]
    bb: TestMutualRecursionB
    subgroup: TestMutualRecursionA.SubGroup
    subgroupr: _containers.RepeatedCompositeFieldContainer[TestMutualRecursionA.SubGroupR]
    def __init__(self, bb: _Optional[_Union[TestMutualRecursionB, _Mapping]] = ..., subgroup: _Optional[_Union[TestMutualRecursionA.SubGroup, _Mapping]] = ..., subgroupr: _Optional[_Iterable[_Union[TestMutualRecursionA.SubGroupR, _Mapping]]] = ...) -> None: ...

class TestMutualRecursionB(_message.Message):
    __slots__ = ("a", "optional_int32")
    A_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    a: TestMutualRecursionA
    optional_int32: int
    def __init__(self, a: _Optional[_Union[TestMutualRecursionA, _Mapping]] = ..., optional_int32: _Optional[int] = ...) -> None: ...

class TestIsInitialized(_message.Message):
    __slots__ = ("sub_message",)
    class SubMessage(_message.Message):
        __slots__ = ("subgroup",)
        class SubGroup(_message.Message):
            __slots__ = ("i",)
            I_FIELD_NUMBER: _ClassVar[int]
            i: int
            def __init__(self, i: _Optional[int] = ...) -> None: ...
        SUBGROUP_FIELD_NUMBER: _ClassVar[int]
        subgroup: TestIsInitialized.SubMessage.SubGroup
        def __init__(self, subgroup: _Optional[_Union[TestIsInitialized.SubMessage.SubGroup, _Mapping]] = ...) -> None: ...
    SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sub_message: TestIsInitialized.SubMessage
    def __init__(self, sub_message: _Optional[_Union[TestIsInitialized.SubMessage, _Mapping]] = ...) -> None: ...

class TestDupFieldNumber(_message.Message):
    __slots__ = ("a", "foo", "bar")
    class Foo(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    class Bar(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    FOO_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    a: int
    foo: TestDupFieldNumber.Foo
    bar: TestDupFieldNumber.Bar
    def __init__(self, a: _Optional[int] = ..., foo: _Optional[_Union[TestDupFieldNumber.Foo, _Mapping]] = ..., bar: _Optional[_Union[TestDupFieldNumber.Bar, _Mapping]] = ...) -> None: ...

class TestEagerMessage(_message.Message):
    __slots__ = ("sub_message",)
    SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sub_message: TestAllTypes
    def __init__(self, sub_message: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...

class TestLazyMessage(_message.Message):
    __slots__ = ("sub_message",)
    SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sub_message: TestAllTypes
    def __init__(self, sub_message: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...

class TestLazyMessageRepeated(_message.Message):
    __slots__ = ("repeated_message",)
    REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    repeated_message: _containers.RepeatedCompositeFieldContainer[TestLazyMessage]
    def __init__(self, repeated_message: _Optional[_Iterable[_Union[TestLazyMessage, _Mapping]]] = ...) -> None: ...

class TestEagerMaybeLazy(_message.Message):
    __slots__ = ("message_foo", "message_bar", "message_baz")
    class NestedMessage(_message.Message):
        __slots__ = ("packed",)
        PACKED_FIELD_NUMBER: _ClassVar[int]
        packed: TestPackedTypes
        def __init__(self, packed: _Optional[_Union[TestPackedTypes, _Mapping]] = ...) -> None: ...
    MESSAGE_FOO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BAR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BAZ_FIELD_NUMBER: _ClassVar[int]
    message_foo: TestAllTypes
    message_bar: TestAllTypes
    message_baz: TestEagerMaybeLazy.NestedMessage
    def __init__(self, message_foo: _Optional[_Union[TestAllTypes, _Mapping]] = ..., message_bar: _Optional[_Union[TestAllTypes, _Mapping]] = ..., message_baz: _Optional[_Union[TestEagerMaybeLazy.NestedMessage, _Mapping]] = ...) -> None: ...

class TestNestedMessageHasBits(_message.Message):
    __slots__ = ("optional_nested_message",)
    class NestedMessage(_message.Message):
        __slots__ = ("nestedmessage_repeated_int32", "nestedmessage_repeated_foreignmessage")
        NESTEDMESSAGE_REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
        NESTEDMESSAGE_REPEATED_FOREIGNMESSAGE_FIELD_NUMBER: _ClassVar[int]
        nestedmessage_repeated_int32: _containers.RepeatedScalarFieldContainer[int]
        nestedmessage_repeated_foreignmessage: _containers.RepeatedCompositeFieldContainer[ForeignMessage]
        def __init__(self, nestedmessage_repeated_int32: _Optional[_Iterable[int]] = ..., nestedmessage_repeated_foreignmessage: _Optional[_Iterable[_Union[ForeignMessage, _Mapping]]] = ...) -> None: ...
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    optional_nested_message: TestNestedMessageHasBits.NestedMessage
    def __init__(self, optional_nested_message: _Optional[_Union[TestNestedMessageHasBits.NestedMessage, _Mapping]] = ...) -> None: ...

class TestCamelCaseFieldNames(_message.Message):
    __slots__ = ("PrimitiveField", "StringField", "EnumField", "MessageField", "StringPieceField", "CordField", "RepeatedPrimitiveField", "RepeatedStringField", "RepeatedEnumField", "RepeatedMessageField", "RepeatedStringPieceField", "RepeatedCordField")
    PRIMITIVEFIELD_FIELD_NUMBER: _ClassVar[int]
    STRINGFIELD_FIELD_NUMBER: _ClassVar[int]
    ENUMFIELD_FIELD_NUMBER: _ClassVar[int]
    MESSAGEFIELD_FIELD_NUMBER: _ClassVar[int]
    STRINGPIECEFIELD_FIELD_NUMBER: _ClassVar[int]
    CORDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATEDPRIMITIVEFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATEDSTRINGFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATEDENUMFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATEDMESSAGEFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATEDSTRINGPIECEFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATEDCORDFIELD_FIELD_NUMBER: _ClassVar[int]
    PrimitiveField: int
    StringField: str
    EnumField: ForeignEnum
    MessageField: ForeignMessage
    StringPieceField: str
    CordField: str
    RepeatedPrimitiveField: _containers.RepeatedScalarFieldContainer[int]
    RepeatedStringField: _containers.RepeatedScalarFieldContainer[str]
    RepeatedEnumField: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    RepeatedMessageField: _containers.RepeatedCompositeFieldContainer[ForeignMessage]
    RepeatedStringPieceField: _containers.RepeatedScalarFieldContainer[str]
    RepeatedCordField: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, PrimitiveField: _Optional[int] = ..., StringField: _Optional[str] = ..., EnumField: _Optional[_Union[ForeignEnum, str]] = ..., MessageField: _Optional[_Union[ForeignMessage, _Mapping]] = ..., StringPieceField: _Optional[str] = ..., CordField: _Optional[str] = ..., RepeatedPrimitiveField: _Optional[_Iterable[int]] = ..., RepeatedStringField: _Optional[_Iterable[str]] = ..., RepeatedEnumField: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ..., RepeatedMessageField: _Optional[_Iterable[_Union[ForeignMessage, _Mapping]]] = ..., RepeatedStringPieceField: _Optional[_Iterable[str]] = ..., RepeatedCordField: _Optional[_Iterable[str]] = ...) -> None: ...

class TestFieldOrderings(_message.Message):
    __slots__ = ("my_string", "my_int", "my_float", "optional_nested_message")
    Extensions: _python_message._ExtensionDict
    class NestedMessage(_message.Message):
        __slots__ = ("oo", "bb")
        OO_FIELD_NUMBER: _ClassVar[int]
        BB_FIELD_NUMBER: _ClassVar[int]
        oo: int
        bb: int
        def __init__(self, oo: _Optional[int] = ..., bb: _Optional[int] = ...) -> None: ...
    MY_STRING_FIELD_NUMBER: _ClassVar[int]
    MY_INT_FIELD_NUMBER: _ClassVar[int]
    MY_FLOAT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    my_string: str
    my_int: int
    my_float: float
    optional_nested_message: TestFieldOrderings.NestedMessage
    def __init__(self, my_string: _Optional[str] = ..., my_int: _Optional[int] = ..., my_float: _Optional[float] = ..., optional_nested_message: _Optional[_Union[TestFieldOrderings.NestedMessage, _Mapping]] = ...) -> None: ...

class TestExtensionOrderings1(_message.Message):
    __slots__ = ("my_string",)
    TEST_EXT_ORDERINGS1_FIELD_NUMBER: _ClassVar[int]
    test_ext_orderings1: _descriptor.FieldDescriptor
    MY_STRING_FIELD_NUMBER: _ClassVar[int]
    my_string: str
    def __init__(self, my_string: _Optional[str] = ...) -> None: ...

class TestExtensionOrderings2(_message.Message):
    __slots__ = ("my_string",)
    class TestExtensionOrderings3(_message.Message):
        __slots__ = ("my_string",)
        TEST_EXT_ORDERINGS3_FIELD_NUMBER: _ClassVar[int]
        test_ext_orderings3: _descriptor.FieldDescriptor
        MY_STRING_FIELD_NUMBER: _ClassVar[int]
        my_string: str
        def __init__(self, my_string: _Optional[str] = ...) -> None: ...
    TEST_EXT_ORDERINGS2_FIELD_NUMBER: _ClassVar[int]
    test_ext_orderings2: _descriptor.FieldDescriptor
    MY_STRING_FIELD_NUMBER: _ClassVar[int]
    my_string: str
    def __init__(self, my_string: _Optional[str] = ...) -> None: ...

class TestExtremeDefaultValues(_message.Message):
    __slots__ = ("escaped_bytes", "large_uint32", "large_uint64", "small_int32", "small_int64", "really_small_int32", "really_small_int64", "utf8_string", "zero_float", "one_float", "small_float", "negative_one_float", "negative_float", "large_float", "small_negative_float", "inf_double", "neg_inf_double", "nan_double", "inf_float", "neg_inf_float", "nan_float", "cpp_trigraph", "string_with_zero", "bytes_with_zero", "string_piece_with_zero", "cord_with_zero", "replacement_string")
    ESCAPED_BYTES_FIELD_NUMBER: _ClassVar[int]
    LARGE_UINT32_FIELD_NUMBER: _ClassVar[int]
    LARGE_UINT64_FIELD_NUMBER: _ClassVar[int]
    SMALL_INT32_FIELD_NUMBER: _ClassVar[int]
    SMALL_INT64_FIELD_NUMBER: _ClassVar[int]
    REALLY_SMALL_INT32_FIELD_NUMBER: _ClassVar[int]
    REALLY_SMALL_INT64_FIELD_NUMBER: _ClassVar[int]
    UTF8_STRING_FIELD_NUMBER: _ClassVar[int]
    ZERO_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ONE_FLOAT_FIELD_NUMBER: _ClassVar[int]
    SMALL_FLOAT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_ONE_FLOAT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FLOAT_FIELD_NUMBER: _ClassVar[int]
    LARGE_FLOAT_FIELD_NUMBER: _ClassVar[int]
    SMALL_NEGATIVE_FLOAT_FIELD_NUMBER: _ClassVar[int]
    INF_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    NEG_INF_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    NAN_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    INF_FLOAT_FIELD_NUMBER: _ClassVar[int]
    NEG_INF_FLOAT_FIELD_NUMBER: _ClassVar[int]
    NAN_FLOAT_FIELD_NUMBER: _ClassVar[int]
    CPP_TRIGRAPH_FIELD_NUMBER: _ClassVar[int]
    STRING_WITH_ZERO_FIELD_NUMBER: _ClassVar[int]
    BYTES_WITH_ZERO_FIELD_NUMBER: _ClassVar[int]
    STRING_PIECE_WITH_ZERO_FIELD_NUMBER: _ClassVar[int]
    CORD_WITH_ZERO_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_STRING_FIELD_NUMBER: _ClassVar[int]
    escaped_bytes: bytes
    large_uint32: int
    large_uint64: int
    small_int32: int
    small_int64: int
    really_small_int32: int
    really_small_int64: int
    utf8_string: str
    zero_float: float
    one_float: float
    small_float: float
    negative_one_float: float
    negative_float: float
    large_float: float
    small_negative_float: float
    inf_double: float
    neg_inf_double: float
    nan_double: float
    inf_float: float
    neg_inf_float: float
    nan_float: float
    cpp_trigraph: str
    string_with_zero: str
    bytes_with_zero: bytes
    string_piece_with_zero: str
    cord_with_zero: str
    replacement_string: str
    def __init__(self, escaped_bytes: _Optional[bytes] = ..., large_uint32: _Optional[int] = ..., large_uint64: _Optional[int] = ..., small_int32: _Optional[int] = ..., small_int64: _Optional[int] = ..., really_small_int32: _Optional[int] = ..., really_small_int64: _Optional[int] = ..., utf8_string: _Optional[str] = ..., zero_float: _Optional[float] = ..., one_float: _Optional[float] = ..., small_float: _Optional[float] = ..., negative_one_float: _Optional[float] = ..., negative_float: _Optional[float] = ..., large_float: _Optional[float] = ..., small_negative_float: _Optional[float] = ..., inf_double: _Optional[float] = ..., neg_inf_double: _Optional[float] = ..., nan_double: _Optional[float] = ..., inf_float: _Optional[float] = ..., neg_inf_float: _Optional[float] = ..., nan_float: _Optional[float] = ..., cpp_trigraph: _Optional[str] = ..., string_with_zero: _Optional[str] = ..., bytes_with_zero: _Optional[bytes] = ..., string_piece_with_zero: _Optional[str] = ..., cord_with_zero: _Optional[str] = ..., replacement_string: _Optional[str] = ...) -> None: ...

class SparseEnumMessage(_message.Message):
    __slots__ = ("sparse_enum",)
    SPARSE_ENUM_FIELD_NUMBER: _ClassVar[int]
    sparse_enum: TestSparseEnum
    def __init__(self, sparse_enum: _Optional[_Union[TestSparseEnum, str]] = ...) -> None: ...

class OneString(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class MoreString(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, data: _Optional[_Iterable[str]] = ...) -> None: ...

class OneBytes(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class MoreBytes(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, data: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ManyOptionalString(_message.Message):
    __slots__ = ("str1", "str2", "str3", "str4", "str5", "str6", "str7", "str8", "str9", "str10", "str11", "str12", "str13", "str14", "str15", "str16", "str17", "str18", "str19", "str20", "str21", "str22", "str23", "str24", "str25", "str26", "str27", "str28", "str29", "str30", "str31", "str32")
    STR1_FIELD_NUMBER: _ClassVar[int]
    STR2_FIELD_NUMBER: _ClassVar[int]
    STR3_FIELD_NUMBER: _ClassVar[int]
    STR4_FIELD_NUMBER: _ClassVar[int]
    STR5_FIELD_NUMBER: _ClassVar[int]
    STR6_FIELD_NUMBER: _ClassVar[int]
    STR7_FIELD_NUMBER: _ClassVar[int]
    STR8_FIELD_NUMBER: _ClassVar[int]
    STR9_FIELD_NUMBER: _ClassVar[int]
    STR10_FIELD_NUMBER: _ClassVar[int]
    STR11_FIELD_NUMBER: _ClassVar[int]
    STR12_FIELD_NUMBER: _ClassVar[int]
    STR13_FIELD_NUMBER: _ClassVar[int]
    STR14_FIELD_NUMBER: _ClassVar[int]
    STR15_FIELD_NUMBER: _ClassVar[int]
    STR16_FIELD_NUMBER: _ClassVar[int]
    STR17_FIELD_NUMBER: _ClassVar[int]
    STR18_FIELD_NUMBER: _ClassVar[int]
    STR19_FIELD_NUMBER: _ClassVar[int]
    STR20_FIELD_NUMBER: _ClassVar[int]
    STR21_FIELD_NUMBER: _ClassVar[int]
    STR22_FIELD_NUMBER: _ClassVar[int]
    STR23_FIELD_NUMBER: _ClassVar[int]
    STR24_FIELD_NUMBER: _ClassVar[int]
    STR25_FIELD_NUMBER: _ClassVar[int]
    STR26_FIELD_NUMBER: _ClassVar[int]
    STR27_FIELD_NUMBER: _ClassVar[int]
    STR28_FIELD_NUMBER: _ClassVar[int]
    STR29_FIELD_NUMBER: _ClassVar[int]
    STR30_FIELD_NUMBER: _ClassVar[int]
    STR31_FIELD_NUMBER: _ClassVar[int]
    STR32_FIELD_NUMBER: _ClassVar[int]
    str1: str
    str2: str
    str3: str
    str4: str
    str5: str
    str6: str
    str7: str
    str8: str
    str9: str
    str10: str
    str11: str
    str12: str
    str13: str
    str14: str
    str15: str
    str16: str
    str17: str
    str18: str
    str19: str
    str20: str
    str21: str
    str22: str
    str23: str
    str24: str
    str25: str
    str26: str
    str27: str
    str28: str
    str29: str
    str30: str
    str31: str
    str32: str
    def __init__(self, str1: _Optional[str] = ..., str2: _Optional[str] = ..., str3: _Optional[str] = ..., str4: _Optional[str] = ..., str5: _Optional[str] = ..., str6: _Optional[str] = ..., str7: _Optional[str] = ..., str8: _Optional[str] = ..., str9: _Optional[str] = ..., str10: _Optional[str] = ..., str11: _Optional[str] = ..., str12: _Optional[str] = ..., str13: _Optional[str] = ..., str14: _Optional[str] = ..., str15: _Optional[str] = ..., str16: _Optional[str] = ..., str17: _Optional[str] = ..., str18: _Optional[str] = ..., str19: _Optional[str] = ..., str20: _Optional[str] = ..., str21: _Optional[str] = ..., str22: _Optional[str] = ..., str23: _Optional[str] = ..., str24: _Optional[str] = ..., str25: _Optional[str] = ..., str26: _Optional[str] = ..., str27: _Optional[str] = ..., str28: _Optional[str] = ..., str29: _Optional[str] = ..., str30: _Optional[str] = ..., str31: _Optional[str] = ..., str32: _Optional[str] = ...) -> None: ...

class Int32Message(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...

class Uint32Message(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...

class Int64Message(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...

class Uint64Message(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...

class BoolMessage(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bool
    def __init__(self, data: bool = ...) -> None: ...

class TestOneof(_message.Message):
    __slots__ = ("foo_int", "foo_string", "foo_message", "foogroup")
    class FooGroup(_message.Message):
        __slots__ = ("a", "b")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: str
        def __init__(self, a: _Optional[int] = ..., b: _Optional[str] = ...) -> None: ...
    FOO_INT_FIELD_NUMBER: _ClassVar[int]
    FOO_STRING_FIELD_NUMBER: _ClassVar[int]
    FOO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FOOGROUP_FIELD_NUMBER: _ClassVar[int]
    foo_int: int
    foo_string: str
    foo_message: TestAllTypes
    foogroup: TestOneof.FooGroup
    def __init__(self, foo_int: _Optional[int] = ..., foo_string: _Optional[str] = ..., foo_message: _Optional[_Union[TestAllTypes, _Mapping]] = ..., foogroup: _Optional[_Union[TestOneof.FooGroup, _Mapping]] = ...) -> None: ...

class TestOneofBackwardsCompatible(_message.Message):
    __slots__ = ("foo_int", "foo_string", "foo_message", "foogroup")
    class FooGroup(_message.Message):
        __slots__ = ("a", "b")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: str
        def __init__(self, a: _Optional[int] = ..., b: _Optional[str] = ...) -> None: ...
    FOO_INT_FIELD_NUMBER: _ClassVar[int]
    FOO_STRING_FIELD_NUMBER: _ClassVar[int]
    FOO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FOOGROUP_FIELD_NUMBER: _ClassVar[int]
    foo_int: int
    foo_string: str
    foo_message: TestAllTypes
    foogroup: TestOneofBackwardsCompatible.FooGroup
    def __init__(self, foo_int: _Optional[int] = ..., foo_string: _Optional[str] = ..., foo_message: _Optional[_Union[TestAllTypes, _Mapping]] = ..., foogroup: _Optional[_Union[TestOneofBackwardsCompatible.FooGroup, _Mapping]] = ...) -> None: ...

class TestOneof2(_message.Message):
    __slots__ = ("foo_int", "foo_string", "foo_cord", "foo_string_piece", "foo_bytes", "foo_enum", "foo_message", "foogroup", "foo_lazy_message", "foo_bytes_cord", "bar_int", "bar_string", "bar_cord", "bar_string_piece", "bar_bytes", "bar_enum", "bar_string_with_empty_default", "bar_cord_with_empty_default", "bar_string_piece_with_empty_default", "bar_bytes_with_empty_default", "baz_int", "baz_string")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[TestOneof2.NestedEnum]
        FOO: _ClassVar[TestOneof2.NestedEnum]
        BAR: _ClassVar[TestOneof2.NestedEnum]
        BAZ: _ClassVar[TestOneof2.NestedEnum]
    UNKNOWN: TestOneof2.NestedEnum
    FOO: TestOneof2.NestedEnum
    BAR: TestOneof2.NestedEnum
    BAZ: TestOneof2.NestedEnum
    class FooGroup(_message.Message):
        __slots__ = ("a", "b")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: str
        def __init__(self, a: _Optional[int] = ..., b: _Optional[str] = ...) -> None: ...
    class NestedMessage(_message.Message):
        __slots__ = ("moo_int", "corge_int")
        MOO_INT_FIELD_NUMBER: _ClassVar[int]
        CORGE_INT_FIELD_NUMBER: _ClassVar[int]
        moo_int: int
        corge_int: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, moo_int: _Optional[int] = ..., corge_int: _Optional[_Iterable[int]] = ...) -> None: ...
    FOO_INT_FIELD_NUMBER: _ClassVar[int]
    FOO_STRING_FIELD_NUMBER: _ClassVar[int]
    FOO_CORD_FIELD_NUMBER: _ClassVar[int]
    FOO_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    FOO_BYTES_FIELD_NUMBER: _ClassVar[int]
    FOO_ENUM_FIELD_NUMBER: _ClassVar[int]
    FOO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FOOGROUP_FIELD_NUMBER: _ClassVar[int]
    FOO_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FOO_BYTES_CORD_FIELD_NUMBER: _ClassVar[int]
    BAR_INT_FIELD_NUMBER: _ClassVar[int]
    BAR_STRING_FIELD_NUMBER: _ClassVar[int]
    BAR_CORD_FIELD_NUMBER: _ClassVar[int]
    BAR_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    BAR_BYTES_FIELD_NUMBER: _ClassVar[int]
    BAR_ENUM_FIELD_NUMBER: _ClassVar[int]
    BAR_STRING_WITH_EMPTY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    BAR_CORD_WITH_EMPTY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    BAR_STRING_PIECE_WITH_EMPTY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    BAR_BYTES_WITH_EMPTY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    BAZ_INT_FIELD_NUMBER: _ClassVar[int]
    BAZ_STRING_FIELD_NUMBER: _ClassVar[int]
    foo_int: int
    foo_string: str
    foo_cord: str
    foo_string_piece: str
    foo_bytes: bytes
    foo_enum: TestOneof2.NestedEnum
    foo_message: TestOneof2.NestedMessage
    foogroup: TestOneof2.FooGroup
    foo_lazy_message: TestOneof2.NestedMessage
    foo_bytes_cord: bytes
    bar_int: int
    bar_string: str
    bar_cord: str
    bar_string_piece: str
    bar_bytes: bytes
    bar_enum: TestOneof2.NestedEnum
    bar_string_with_empty_default: str
    bar_cord_with_empty_default: str
    bar_string_piece_with_empty_default: str
    bar_bytes_with_empty_default: bytes
    baz_int: int
    baz_string: str
    def __init__(self, foo_int: _Optional[int] = ..., foo_string: _Optional[str] = ..., foo_cord: _Optional[str] = ..., foo_string_piece: _Optional[str] = ..., foo_bytes: _Optional[bytes] = ..., foo_enum: _Optional[_Union[TestOneof2.NestedEnum, str]] = ..., foo_message: _Optional[_Union[TestOneof2.NestedMessage, _Mapping]] = ..., foogroup: _Optional[_Union[TestOneof2.FooGroup, _Mapping]] = ..., foo_lazy_message: _Optional[_Union[TestOneof2.NestedMessage, _Mapping]] = ..., foo_bytes_cord: _Optional[bytes] = ..., bar_int: _Optional[int] = ..., bar_string: _Optional[str] = ..., bar_cord: _Optional[str] = ..., bar_string_piece: _Optional[str] = ..., bar_bytes: _Optional[bytes] = ..., bar_enum: _Optional[_Union[TestOneof2.NestedEnum, str]] = ..., bar_string_with_empty_default: _Optional[str] = ..., bar_cord_with_empty_default: _Optional[str] = ..., bar_string_piece_with_empty_default: _Optional[str] = ..., bar_bytes_with_empty_default: _Optional[bytes] = ..., baz_int: _Optional[int] = ..., baz_string: _Optional[str] = ...) -> None: ...

class TestRequiredOneof(_message.Message):
    __slots__ = ("foo_int", "foo_string", "foo_message", "foo_lazy_message")
    class NestedMessage(_message.Message):
        __slots__ = ("required_double",)
        REQUIRED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
        required_double: float
        def __init__(self, required_double: _Optional[float] = ...) -> None: ...
    FOO_INT_FIELD_NUMBER: _ClassVar[int]
    FOO_STRING_FIELD_NUMBER: _ClassVar[int]
    FOO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FOO_LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    foo_int: int
    foo_string: str
    foo_message: TestRequiredOneof.NestedMessage
    foo_lazy_message: TestRequiredOneof.NestedMessage
    def __init__(self, foo_int: _Optional[int] = ..., foo_string: _Optional[str] = ..., foo_message: _Optional[_Union[TestRequiredOneof.NestedMessage, _Mapping]] = ..., foo_lazy_message: _Optional[_Union[TestRequiredOneof.NestedMessage, _Mapping]] = ...) -> None: ...

class TestPackedTypes(_message.Message):
    __slots__ = ("packed_int32", "packed_int64", "packed_uint32", "packed_uint64", "packed_sint32", "packed_sint64", "packed_fixed32", "packed_fixed64", "packed_sfixed32", "packed_sfixed64", "packed_float", "packed_double", "packed_bool", "packed_enum")
    PACKED_INT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_UINT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_UINT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_SINT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_SINT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    PACKED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    PACKED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    PACKED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    PACKED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    PACKED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    PACKED_BOOL_FIELD_NUMBER: _ClassVar[int]
    PACKED_ENUM_FIELD_NUMBER: _ClassVar[int]
    packed_int32: _containers.RepeatedScalarFieldContainer[int]
    packed_int64: _containers.RepeatedScalarFieldContainer[int]
    packed_uint32: _containers.RepeatedScalarFieldContainer[int]
    packed_uint64: _containers.RepeatedScalarFieldContainer[int]
    packed_sint32: _containers.RepeatedScalarFieldContainer[int]
    packed_sint64: _containers.RepeatedScalarFieldContainer[int]
    packed_fixed32: _containers.RepeatedScalarFieldContainer[int]
    packed_fixed64: _containers.RepeatedScalarFieldContainer[int]
    packed_sfixed32: _containers.RepeatedScalarFieldContainer[int]
    packed_sfixed64: _containers.RepeatedScalarFieldContainer[int]
    packed_float: _containers.RepeatedScalarFieldContainer[float]
    packed_double: _containers.RepeatedScalarFieldContainer[float]
    packed_bool: _containers.RepeatedScalarFieldContainer[bool]
    packed_enum: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    def __init__(self, packed_int32: _Optional[_Iterable[int]] = ..., packed_int64: _Optional[_Iterable[int]] = ..., packed_uint32: _Optional[_Iterable[int]] = ..., packed_uint64: _Optional[_Iterable[int]] = ..., packed_sint32: _Optional[_Iterable[int]] = ..., packed_sint64: _Optional[_Iterable[int]] = ..., packed_fixed32: _Optional[_Iterable[int]] = ..., packed_fixed64: _Optional[_Iterable[int]] = ..., packed_sfixed32: _Optional[_Iterable[int]] = ..., packed_sfixed64: _Optional[_Iterable[int]] = ..., packed_float: _Optional[_Iterable[float]] = ..., packed_double: _Optional[_Iterable[float]] = ..., packed_bool: _Optional[_Iterable[bool]] = ..., packed_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ...) -> None: ...

class TestUnpackedTypes(_message.Message):
    __slots__ = ("unpacked_int32", "unpacked_int64", "unpacked_uint32", "unpacked_uint64", "unpacked_sint32", "unpacked_sint64", "unpacked_fixed32", "unpacked_fixed64", "unpacked_sfixed32", "unpacked_sfixed64", "unpacked_float", "unpacked_double", "unpacked_bool", "unpacked_enum")
    UNPACKED_INT32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_INT64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_UINT32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_UINT64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_SINT32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_SINT64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_BOOL_FIELD_NUMBER: _ClassVar[int]
    UNPACKED_ENUM_FIELD_NUMBER: _ClassVar[int]
    unpacked_int32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_int64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_uint32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_uint64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_sint32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_sint64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_fixed32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_fixed64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_sfixed32: _containers.RepeatedScalarFieldContainer[int]
    unpacked_sfixed64: _containers.RepeatedScalarFieldContainer[int]
    unpacked_float: _containers.RepeatedScalarFieldContainer[float]
    unpacked_double: _containers.RepeatedScalarFieldContainer[float]
    unpacked_bool: _containers.RepeatedScalarFieldContainer[bool]
    unpacked_enum: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    def __init__(self, unpacked_int32: _Optional[_Iterable[int]] = ..., unpacked_int64: _Optional[_Iterable[int]] = ..., unpacked_uint32: _Optional[_Iterable[int]] = ..., unpacked_uint64: _Optional[_Iterable[int]] = ..., unpacked_sint32: _Optional[_Iterable[int]] = ..., unpacked_sint64: _Optional[_Iterable[int]] = ..., unpacked_fixed32: _Optional[_Iterable[int]] = ..., unpacked_fixed64: _Optional[_Iterable[int]] = ..., unpacked_sfixed32: _Optional[_Iterable[int]] = ..., unpacked_sfixed64: _Optional[_Iterable[int]] = ..., unpacked_float: _Optional[_Iterable[float]] = ..., unpacked_double: _Optional[_Iterable[float]] = ..., unpacked_bool: _Optional[_Iterable[bool]] = ..., unpacked_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ...) -> None: ...

class TestPackedExtensions(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestUnpackedExtensions(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestDynamicExtensions(_message.Message):
    __slots__ = ("scalar_extension", "enum_extension", "dynamic_enum_extension", "message_extension", "dynamic_message_extension", "repeated_extension", "packed_extension")
    class DynamicEnumType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DYNAMIC_UNKNOWN: _ClassVar[TestDynamicExtensions.DynamicEnumType]
        DYNAMIC_FOO: _ClassVar[TestDynamicExtensions.DynamicEnumType]
        DYNAMIC_BAR: _ClassVar[TestDynamicExtensions.DynamicEnumType]
        DYNAMIC_BAZ: _ClassVar[TestDynamicExtensions.DynamicEnumType]
    DYNAMIC_UNKNOWN: TestDynamicExtensions.DynamicEnumType
    DYNAMIC_FOO: TestDynamicExtensions.DynamicEnumType
    DYNAMIC_BAR: TestDynamicExtensions.DynamicEnumType
    DYNAMIC_BAZ: TestDynamicExtensions.DynamicEnumType
    class DynamicMessageType(_message.Message):
        __slots__ = ("dynamic_field",)
        DYNAMIC_FIELD_FIELD_NUMBER: _ClassVar[int]
        dynamic_field: int
        def __init__(self, dynamic_field: _Optional[int] = ...) -> None: ...
    SCALAR_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_ENUM_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    REPEATED_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    PACKED_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    scalar_extension: int
    enum_extension: ForeignEnum
    dynamic_enum_extension: TestDynamicExtensions.DynamicEnumType
    message_extension: ForeignMessage
    dynamic_message_extension: TestDynamicExtensions.DynamicMessageType
    repeated_extension: _containers.RepeatedScalarFieldContainer[str]
    packed_extension: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, scalar_extension: _Optional[int] = ..., enum_extension: _Optional[_Union[ForeignEnum, str]] = ..., dynamic_enum_extension: _Optional[_Union[TestDynamicExtensions.DynamicEnumType, str]] = ..., message_extension: _Optional[_Union[ForeignMessage, _Mapping]] = ..., dynamic_message_extension: _Optional[_Union[TestDynamicExtensions.DynamicMessageType, _Mapping]] = ..., repeated_extension: _Optional[_Iterable[str]] = ..., packed_extension: _Optional[_Iterable[int]] = ...) -> None: ...

class TestRepeatedString(_message.Message):
    __slots__ = ("repeated_string1", "repeated_string2", "repeated_bytes11", "repeated_bytes12")
    REPEATED_STRING1_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING2_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES11_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES12_FIELD_NUMBER: _ClassVar[int]
    repeated_string1: _containers.RepeatedScalarFieldContainer[str]
    repeated_string2: _containers.RepeatedScalarFieldContainer[str]
    repeated_bytes11: _containers.RepeatedScalarFieldContainer[bytes]
    repeated_bytes12: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, repeated_string1: _Optional[_Iterable[str]] = ..., repeated_string2: _Optional[_Iterable[str]] = ..., repeated_bytes11: _Optional[_Iterable[bytes]] = ..., repeated_bytes12: _Optional[_Iterable[bytes]] = ...) -> None: ...

class TestRepeatedScalarDifferentTagSizes(_message.Message):
    __slots__ = ("repeated_fixed32", "repeated_int32", "repeated_fixed64", "repeated_int64", "repeated_float", "repeated_uint64")
    REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT64_FIELD_NUMBER: _ClassVar[int]
    repeated_fixed32: _containers.RepeatedScalarFieldContainer[int]
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    repeated_fixed64: _containers.RepeatedScalarFieldContainer[int]
    repeated_int64: _containers.RepeatedScalarFieldContainer[int]
    repeated_float: _containers.RepeatedScalarFieldContainer[float]
    repeated_uint64: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ...) -> None: ...

class TestParsingMerge(_message.Message):
    __slots__ = ("required_all_types", "optional_all_types", "repeated_all_types", "optionalgroup", "repeatedgroup")
    Extensions: _python_message._ExtensionDict
    class RepeatedFieldsGenerator(_message.Message):
        __slots__ = ("field1", "field2", "field3", "group1", "group2", "ext1", "ext2")
        class Group1(_message.Message):
            __slots__ = ("field1",)
            FIELD1_FIELD_NUMBER: _ClassVar[int]
            field1: TestAllTypes
            def __init__(self, field1: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...
        class Group2(_message.Message):
            __slots__ = ("field1",)
            FIELD1_FIELD_NUMBER: _ClassVar[int]
            field1: TestAllTypes
            def __init__(self, field1: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...
        FIELD1_FIELD_NUMBER: _ClassVar[int]
        FIELD2_FIELD_NUMBER: _ClassVar[int]
        FIELD3_FIELD_NUMBER: _ClassVar[int]
        GROUP1_FIELD_NUMBER: _ClassVar[int]
        GROUP2_FIELD_NUMBER: _ClassVar[int]
        EXT1_FIELD_NUMBER: _ClassVar[int]
        EXT2_FIELD_NUMBER: _ClassVar[int]
        field1: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
        field2: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
        field3: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
        group1: _containers.RepeatedCompositeFieldContainer[TestParsingMerge.RepeatedFieldsGenerator.Group1]
        group2: _containers.RepeatedCompositeFieldContainer[TestParsingMerge.RepeatedFieldsGenerator.Group2]
        ext1: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
        ext2: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
        def __init__(self, field1: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ..., field2: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ..., field3: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ..., group1: _Optional[_Iterable[_Union[TestParsingMerge.RepeatedFieldsGenerator.Group1, _Mapping]]] = ..., group2: _Optional[_Iterable[_Union[TestParsingMerge.RepeatedFieldsGenerator.Group2, _Mapping]]] = ..., ext1: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ..., ext2: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...
    class OptionalGroup(_message.Message):
        __slots__ = ("optional_group_all_types",)
        OPTIONAL_GROUP_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
        optional_group_all_types: TestAllTypes
        def __init__(self, optional_group_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...
    class RepeatedGroup(_message.Message):
        __slots__ = ("repeated_group_all_types",)
        REPEATED_GROUP_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
        repeated_group_all_types: TestAllTypes
        def __init__(self, repeated_group_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ...) -> None: ...
    OPTIONAL_EXT_FIELD_NUMBER: _ClassVar[int]
    optional_ext: _descriptor.FieldDescriptor
    REPEATED_EXT_FIELD_NUMBER: _ClassVar[int]
    repeated_ext: _descriptor.FieldDescriptor
    REQUIRED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    REPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
    required_all_types: TestAllTypes
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    optionalgroup: TestParsingMerge.OptionalGroup
    repeatedgroup: _containers.RepeatedCompositeFieldContainer[TestParsingMerge.RepeatedGroup]
    def __init__(self, required_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ..., optionalgroup: _Optional[_Union[TestParsingMerge.OptionalGroup, _Mapping]] = ..., repeatedgroup: _Optional[_Iterable[_Union[TestParsingMerge.RepeatedGroup, _Mapping]]] = ...) -> None: ...

class TestMergeException(_message.Message):
    __slots__ = ("all_extensions",)
    ALL_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    all_extensions: TestAllExtensions
    def __init__(self, all_extensions: _Optional[_Union[TestAllExtensions, _Mapping]] = ...) -> None: ...

class TestCommentInjectionMessage(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: str
    def __init__(self, a: _Optional[str] = ...) -> None: ...

class TestMessageSize(_message.Message):
    __slots__ = ("m1", "m2", "m3", "m4", "m5", "m6")
    M1_FIELD_NUMBER: _ClassVar[int]
    M2_FIELD_NUMBER: _ClassVar[int]
    M3_FIELD_NUMBER: _ClassVar[int]
    M4_FIELD_NUMBER: _ClassVar[int]
    M5_FIELD_NUMBER: _ClassVar[int]
    M6_FIELD_NUMBER: _ClassVar[int]
    m1: bool
    m2: int
    m3: bool
    m4: str
    m5: int
    m6: int
    def __init__(self, m1: bool = ..., m2: _Optional[int] = ..., m3: bool = ..., m4: _Optional[str] = ..., m5: _Optional[int] = ..., m6: _Optional[int] = ...) -> None: ...

class TestEagerlyVerifiedLazyMessage(_message.Message):
    __slots__ = ("lazy_message",)
    class LazyMessage(_message.Message):
        __slots__ = ("bytes_field",)
        BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
        bytes_field: bytes
        def __init__(self, bytes_field: _Optional[bytes] = ...) -> None: ...
    LAZY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    lazy_message: TestEagerlyVerifiedLazyMessage.LazyMessage
    def __init__(self, lazy_message: _Optional[_Union[TestEagerlyVerifiedLazyMessage.LazyMessage, _Mapping]] = ...) -> None: ...

class FooRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FooResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FooClientMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FooServerMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BarRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BarResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestJsonName(_message.Message):
    __slots__ = ("field_name1", "fieldName2", "FieldName3", "_field_name4", "FIELD_NAME5", "field_name6", "fieldname7")
    FIELD_NAME1_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME2_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME3_FIELD_NUMBER: _ClassVar[int]
    _FIELD_NAME4_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME5_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME6_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME7_FIELD_NUMBER: _ClassVar[int]
    field_name1: int
    fieldName2: int
    FieldName3: int
    _field_name4: int
    FIELD_NAME5: int
    field_name6: int
    fieldname7: int
    def __init__(self, field_name1: _Optional[int] = ..., fieldName2: _Optional[int] = ..., FieldName3: _Optional[int] = ..., _field_name4: _Optional[int] = ..., FIELD_NAME5: _Optional[int] = ..., field_name6: _Optional[int] = ..., fieldname7: _Optional[int] = ...) -> None: ...

class TestHugeFieldNumbers(_message.Message):
    __slots__ = ("optional_int32", "fixed_32", "repeated_int32", "packed_int32", "optional_enum", "optional_string", "optional_bytes", "optional_message", "optionalgroup", "string_string_map", "oneof_uint32", "oneof_test_all_types", "oneof_string", "oneof_bytes")
    Extensions: _python_message._ExtensionDict
    class OptionalGroup(_message.Message):
        __slots__ = ("group_a",)
        GROUP_A_FIELD_NUMBER: _ClassVar[int]
        group_a: int
        def __init__(self, group_a: _Optional[int] = ...) -> None: ...
    class StringStringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    FIXED_32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    STRING_STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_TEST_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    optional_int32: int
    fixed_32: int
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    packed_int32: _containers.RepeatedScalarFieldContainer[int]
    optional_enum: ForeignEnum
    optional_string: str
    optional_bytes: bytes
    optional_message: ForeignMessage
    optionalgroup: TestHugeFieldNumbers.OptionalGroup
    string_string_map: _containers.ScalarMap[str, str]
    oneof_uint32: int
    oneof_test_all_types: TestAllTypes
    oneof_string: str
    oneof_bytes: bytes
    def __init__(self, optional_int32: _Optional[int] = ..., fixed_32: _Optional[int] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., packed_int32: _Optional[_Iterable[int]] = ..., optional_enum: _Optional[_Union[ForeignEnum, str]] = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_message: _Optional[_Union[ForeignMessage, _Mapping]] = ..., optionalgroup: _Optional[_Union[TestHugeFieldNumbers.OptionalGroup, _Mapping]] = ..., string_string_map: _Optional[_Mapping[str, str]] = ..., oneof_uint32: _Optional[int] = ..., oneof_test_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ...) -> None: ...

class TestExtensionInsideTable(_message.Message):
    __slots__ = ("field1", "field2", "field3", "field4", "field6", "field7", "field8", "field9", "field10")
    Extensions: _python_message._ExtensionDict
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    FIELD2_FIELD_NUMBER: _ClassVar[int]
    FIELD3_FIELD_NUMBER: _ClassVar[int]
    FIELD4_FIELD_NUMBER: _ClassVar[int]
    FIELD6_FIELD_NUMBER: _ClassVar[int]
    FIELD7_FIELD_NUMBER: _ClassVar[int]
    FIELD8_FIELD_NUMBER: _ClassVar[int]
    FIELD9_FIELD_NUMBER: _ClassVar[int]
    FIELD10_FIELD_NUMBER: _ClassVar[int]
    field1: int
    field2: int
    field3: int
    field4: int
    field6: int
    field7: int
    field8: int
    field9: int
    field10: int
    def __init__(self, field1: _Optional[int] = ..., field2: _Optional[int] = ..., field3: _Optional[int] = ..., field4: _Optional[int] = ..., field6: _Optional[int] = ..., field7: _Optional[int] = ..., field8: _Optional[int] = ..., field9: _Optional[int] = ..., field10: _Optional[int] = ...) -> None: ...

class TestNestedGroupExtensionOuter(_message.Message):
    __slots__ = ("lay1optionalgroup",)
    class Layer1OptionalGroup(_message.Message):
        __slots__ = ("layer2repeatedgroup", "layer2anotheroptionalrepeatedgroup")
        class Layer2RepeatedGroup(_message.Message):
            __slots__ = ("another_field",)
            Extensions: _python_message._ExtensionDict
            ANOTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
            another_field: str
            def __init__(self, another_field: _Optional[str] = ...) -> None: ...
        class Layer2AnotherOptionalRepeatedGroup(_message.Message):
            __slots__ = ("but_why_tho",)
            BUT_WHY_THO_FIELD_NUMBER: _ClassVar[int]
            but_why_tho: str
            def __init__(self, but_why_tho: _Optional[str] = ...) -> None: ...
        LAYER2REPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
        LAYER2ANOTHEROPTIONALREPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
        layer2repeatedgroup: _containers.RepeatedCompositeFieldContainer[TestNestedGroupExtensionOuter.Layer1OptionalGroup.Layer2RepeatedGroup]
        layer2anotheroptionalrepeatedgroup: _containers.RepeatedCompositeFieldContainer[TestNestedGroupExtensionOuter.Layer1OptionalGroup.Layer2AnotherOptionalRepeatedGroup]
        def __init__(self, layer2repeatedgroup: _Optional[_Iterable[_Union[TestNestedGroupExtensionOuter.Layer1OptionalGroup.Layer2RepeatedGroup, _Mapping]]] = ..., layer2anotheroptionalrepeatedgroup: _Optional[_Iterable[_Union[TestNestedGroupExtensionOuter.Layer1OptionalGroup.Layer2AnotherOptionalRepeatedGroup, _Mapping]]] = ...) -> None: ...
    LAY1OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    lay1optionalgroup: TestNestedGroupExtensionOuter.Layer1OptionalGroup
    def __init__(self, lay1optionalgroup: _Optional[_Union[TestNestedGroupExtensionOuter.Layer1OptionalGroup, _Mapping]] = ...) -> None: ...

class TestNestedGroupExtensionInnerExtension(_message.Message):
    __slots__ = ("inner_name",)
    INNER_NAME_FIELD_NUMBER: _ClassVar[int]
    inner_name: str
    def __init__(self, inner_name: _Optional[str] = ...) -> None: ...

class TestExtensionRangeSerialize(_message.Message):
    __slots__ = ("foo_one", "foo_two", "foo_three", "foo_four")
    Extensions: _python_message._ExtensionDict
    BAR_ONE_FIELD_NUMBER: _ClassVar[int]
    bar_one: _descriptor.FieldDescriptor
    BAR_TWO_FIELD_NUMBER: _ClassVar[int]
    bar_two: _descriptor.FieldDescriptor
    BAR_THREE_FIELD_NUMBER: _ClassVar[int]
    bar_three: _descriptor.FieldDescriptor
    BAR_FOUR_FIELD_NUMBER: _ClassVar[int]
    bar_four: _descriptor.FieldDescriptor
    BAR_FIVE_FIELD_NUMBER: _ClassVar[int]
    bar_five: _descriptor.FieldDescriptor
    FOO_ONE_FIELD_NUMBER: _ClassVar[int]
    FOO_TWO_FIELD_NUMBER: _ClassVar[int]
    FOO_THREE_FIELD_NUMBER: _ClassVar[int]
    FOO_FOUR_FIELD_NUMBER: _ClassVar[int]
    foo_one: int
    foo_two: int
    foo_three: int
    foo_four: int
    def __init__(self, foo_one: _Optional[int] = ..., foo_two: _Optional[int] = ..., foo_three: _Optional[int] = ..., foo_four: _Optional[int] = ...) -> None: ...

class TestVerifyInt32Simple(_message.Message):
    __slots__ = ("optional_int32_1", "optional_int32_2", "optional_int32_63", "optional_int32_64")
    OPTIONAL_INT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_64_FIELD_NUMBER: _ClassVar[int]
    optional_int32_1: int
    optional_int32_2: int
    optional_int32_63: int
    optional_int32_64: int
    def __init__(self, optional_int32_1: _Optional[int] = ..., optional_int32_2: _Optional[int] = ..., optional_int32_63: _Optional[int] = ..., optional_int32_64: _Optional[int] = ...) -> None: ...

class TestVerifyInt32(_message.Message):
    __slots__ = ("optional_int32_1", "optional_int32_2", "optional_int32_63", "optional_int32_64", "optional_all_types", "repeated_all_types")
    OPTIONAL_INT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    optional_int32_1: int
    optional_int32_2: int
    optional_int32_63: int
    optional_int32_64: int
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    def __init__(self, optional_int32_1: _Optional[int] = ..., optional_int32_2: _Optional[int] = ..., optional_int32_63: _Optional[int] = ..., optional_int32_64: _Optional[int] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...

class TestVerifyMostlyInt32(_message.Message):
    __slots__ = ("optional_int64_30", "optional_int32_1", "optional_int32_2", "optional_int32_3", "optional_int32_4", "optional_int32_63", "optional_int32_64", "optional_all_types", "repeated_all_types")
    OPTIONAL_INT64_30_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_3_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_4_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    optional_int64_30: int
    optional_int32_1: int
    optional_int32_2: int
    optional_int32_3: int
    optional_int32_4: int
    optional_int32_63: int
    optional_int32_64: int
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    def __init__(self, optional_int64_30: _Optional[int] = ..., optional_int32_1: _Optional[int] = ..., optional_int32_2: _Optional[int] = ..., optional_int32_3: _Optional[int] = ..., optional_int32_4: _Optional[int] = ..., optional_int32_63: _Optional[int] = ..., optional_int32_64: _Optional[int] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...

class TestVerifyMostlyInt32BigFieldNumber(_message.Message):
    __slots__ = ("optional_int64_30", "optional_int32_300", "optional_int32_1", "optional_int32_2", "optional_int32_3", "optional_int32_4", "optional_int32_63", "optional_int32_64", "optional_all_types", "repeated_all_types")
    OPTIONAL_INT64_30_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_300_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_3_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_4_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    optional_int64_30: int
    optional_int32_300: int
    optional_int32_1: int
    optional_int32_2: int
    optional_int32_3: int
    optional_int32_4: int
    optional_int32_63: int
    optional_int32_64: int
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    def __init__(self, optional_int64_30: _Optional[int] = ..., optional_int32_300: _Optional[int] = ..., optional_int32_1: _Optional[int] = ..., optional_int32_2: _Optional[int] = ..., optional_int32_3: _Optional[int] = ..., optional_int32_4: _Optional[int] = ..., optional_int32_63: _Optional[int] = ..., optional_int32_64: _Optional[int] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...

class TestVerifyUint32Simple(_message.Message):
    __slots__ = ("optional_uint32_1", "optional_uint32_2", "optional_uint32_63", "optional_uint32_64")
    OPTIONAL_UINT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_64_FIELD_NUMBER: _ClassVar[int]
    optional_uint32_1: int
    optional_uint32_2: int
    optional_uint32_63: int
    optional_uint32_64: int
    def __init__(self, optional_uint32_1: _Optional[int] = ..., optional_uint32_2: _Optional[int] = ..., optional_uint32_63: _Optional[int] = ..., optional_uint32_64: _Optional[int] = ...) -> None: ...

class TestVerifyUint32(_message.Message):
    __slots__ = ("optional_uint32_1", "optional_uint32_2", "optional_uint32_63", "optional_uint32_64", "optional_all_types", "repeated_all_types")
    OPTIONAL_UINT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    optional_uint32_1: int
    optional_uint32_2: int
    optional_uint32_63: int
    optional_uint32_64: int
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    def __init__(self, optional_uint32_1: _Optional[int] = ..., optional_uint32_2: _Optional[int] = ..., optional_uint32_63: _Optional[int] = ..., optional_uint32_64: _Optional[int] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...

class TestVerifyOneUint32(_message.Message):
    __slots__ = ("optional_uint32_1", "optional_int32_2", "optional_int32_63", "optional_int32_64", "optional_all_types", "repeated_all_types")
    OPTIONAL_UINT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    optional_uint32_1: int
    optional_int32_2: int
    optional_int32_63: int
    optional_int32_64: int
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    def __init__(self, optional_uint32_1: _Optional[int] = ..., optional_int32_2: _Optional[int] = ..., optional_int32_63: _Optional[int] = ..., optional_int32_64: _Optional[int] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...

class TestVerifyOneInt32BigFieldNumber(_message.Message):
    __slots__ = ("optional_int32_65", "optional_int64_1", "optional_int64_2", "optional_int64_63", "optional_int64_64", "optional_all_types", "repeated_all_types")
    OPTIONAL_INT32_65_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    optional_int32_65: int
    optional_int64_1: int
    optional_int64_2: int
    optional_int64_63: int
    optional_int64_64: int
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    def __init__(self, optional_int32_65: _Optional[int] = ..., optional_int64_1: _Optional[int] = ..., optional_int64_2: _Optional[int] = ..., optional_int64_63: _Optional[int] = ..., optional_int64_64: _Optional[int] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...

class TestVerifyInt32BigFieldNumber(_message.Message):
    __slots__ = ("optional_int32_1000", "optional_int32_65", "optional_int32_1", "optional_int32_2", "optional_int32_63", "optional_int32_64", "optional_all_types", "repeated_all_types")
    OPTIONAL_INT32_1000_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_65_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    optional_int32_1000: int
    optional_int32_65: int
    optional_int32_1: int
    optional_int32_2: int
    optional_int32_63: int
    optional_int32_64: int
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    def __init__(self, optional_int32_1000: _Optional[int] = ..., optional_int32_65: _Optional[int] = ..., optional_int32_1: _Optional[int] = ..., optional_int32_2: _Optional[int] = ..., optional_int32_63: _Optional[int] = ..., optional_int32_64: _Optional[int] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...

class TestVerifyUint32BigFieldNumber(_message.Message):
    __slots__ = ("optional_uint32_1000", "optional_uint32_65", "optional_uint32_1", "optional_uint32_2", "optional_uint32_63", "optional_uint32_64", "optional_all_types", "repeated_all_types")
    OPTIONAL_UINT32_1000_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_65_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_2_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_63_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    optional_uint32_1000: int
    optional_uint32_65: int
    optional_uint32_1: int
    optional_uint32_2: int
    optional_uint32_63: int
    optional_uint32_64: int
    optional_all_types: TestAllTypes
    repeated_all_types: _containers.RepeatedCompositeFieldContainer[TestAllTypes]
    def __init__(self, optional_uint32_1000: _Optional[int] = ..., optional_uint32_65: _Optional[int] = ..., optional_uint32_1: _Optional[int] = ..., optional_uint32_2: _Optional[int] = ..., optional_uint32_63: _Optional[int] = ..., optional_uint32_64: _Optional[int] = ..., optional_all_types: _Optional[_Union[TestAllTypes, _Mapping]] = ..., repeated_all_types: _Optional[_Iterable[_Union[TestAllTypes, _Mapping]]] = ...) -> None: ...

class TestVerifyBigFieldNumberUint32(_message.Message):
    __slots__ = ("optional_nested",)
    class Nested(_message.Message):
        __slots__ = ("optional_uint32_5000", "optional_uint32_1000", "optional_uint32_66", "optional_uint32_65", "optional_uint32_1", "optional_uint32_2", "optional_uint32_63", "optional_uint32_64", "optional_nested", "repeated_nested")
        OPTIONAL_UINT32_5000_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_UINT32_1000_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_UINT32_66_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_UINT32_65_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_UINT32_1_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_UINT32_2_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_UINT32_63_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_UINT32_64_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_NESTED_FIELD_NUMBER: _ClassVar[int]
        REPEATED_NESTED_FIELD_NUMBER: _ClassVar[int]
        optional_uint32_5000: int
        optional_uint32_1000: int
        optional_uint32_66: int
        optional_uint32_65: int
        optional_uint32_1: int
        optional_uint32_2: int
        optional_uint32_63: int
        optional_uint32_64: int
        optional_nested: TestVerifyBigFieldNumberUint32.Nested
        repeated_nested: _containers.RepeatedCompositeFieldContainer[TestVerifyBigFieldNumberUint32.Nested]
        def __init__(self, optional_uint32_5000: _Optional[int] = ..., optional_uint32_1000: _Optional[int] = ..., optional_uint32_66: _Optional[int] = ..., optional_uint32_65: _Optional[int] = ..., optional_uint32_1: _Optional[int] = ..., optional_uint32_2: _Optional[int] = ..., optional_uint32_63: _Optional[int] = ..., optional_uint32_64: _Optional[int] = ..., optional_nested: _Optional[_Union[TestVerifyBigFieldNumberUint32.Nested, _Mapping]] = ..., repeated_nested: _Optional[_Iterable[_Union[TestVerifyBigFieldNumberUint32.Nested, _Mapping]]] = ...) -> None: ...
    OPTIONAL_NESTED_FIELD_NUMBER: _ClassVar[int]
    optional_nested: TestVerifyBigFieldNumberUint32.Nested
    def __init__(self, optional_nested: _Optional[_Union[TestVerifyBigFieldNumberUint32.Nested, _Mapping]] = ...) -> None: ...

class EnumParseTester(_message.Message):
    __slots__ = ("optional_seq_small_0_lowfield", "optional_seq_small_0_midfield", "optional_seq_small_0_hifield", "repeated_seq_small_0_lowfield", "repeated_seq_small_0_midfield", "repeated_seq_small_0_hifield", "packed_seq_small_0_lowfield", "packed_seq_small_0_midfield", "packed_seq_small_0_hifield", "optional_seq_small_1_lowfield", "optional_seq_small_1_midfield", "optional_seq_small_1_hifield", "repeated_seq_small_1_lowfield", "repeated_seq_small_1_midfield", "repeated_seq_small_1_hifield", "packed_seq_small_1_lowfield", "packed_seq_small_1_midfield", "packed_seq_small_1_hifield", "optional_seq_large_lowfield", "optional_seq_large_midfield", "optional_seq_large_hifield", "repeated_seq_large_lowfield", "repeated_seq_large_midfield", "repeated_seq_large_hifield", "packed_seq_large_lowfield", "packed_seq_large_midfield", "packed_seq_large_hifield", "optional_arbitrary_lowfield", "optional_arbitrary_midfield", "optional_arbitrary_hifield", "repeated_arbitrary_lowfield", "repeated_arbitrary_midfield", "repeated_arbitrary_hifield", "packed_arbitrary_lowfield", "packed_arbitrary_midfield", "packed_arbitrary_hifield", "other_field")
    Extensions: _python_message._ExtensionDict
    class SeqSmall0(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEQ_SMALL_0_DEFAULT: _ClassVar[EnumParseTester.SeqSmall0]
        SEQ_SMALL_0_1: _ClassVar[EnumParseTester.SeqSmall0]
        SEQ_SMALL_0_2: _ClassVar[EnumParseTester.SeqSmall0]
    SEQ_SMALL_0_DEFAULT: EnumParseTester.SeqSmall0
    SEQ_SMALL_0_1: EnumParseTester.SeqSmall0
    SEQ_SMALL_0_2: EnumParseTester.SeqSmall0
    class SeqSmall1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[EnumParseTester.SeqSmall1]
        SEQ_SMALL_1_DEFAULT: _ClassVar[EnumParseTester.SeqSmall1]
        SEQ_SMALL_1_2: _ClassVar[EnumParseTester.SeqSmall1]
        SEQ_SMALL_1_3: _ClassVar[EnumParseTester.SeqSmall1]
    UNKNOWN: EnumParseTester.SeqSmall1
    SEQ_SMALL_1_DEFAULT: EnumParseTester.SeqSmall1
    SEQ_SMALL_1_2: EnumParseTester.SeqSmall1
    SEQ_SMALL_1_3: EnumParseTester.SeqSmall1
    class SeqLarge(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEQ_LARGE_DEFAULT: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_0: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_1: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_2: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_3: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_4: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_5: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_6: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_7: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_8: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_9: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_10: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_11: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_12: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_13: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_14: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_15: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_16: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_17: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_18: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_19: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_20: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_21: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_22: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_23: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_24: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_25: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_26: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_27: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_28: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_29: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_30: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_31: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_32: _ClassVar[EnumParseTester.SeqLarge]
        SEQ_LARGE_33: _ClassVar[EnumParseTester.SeqLarge]
    SEQ_LARGE_DEFAULT: EnumParseTester.SeqLarge
    SEQ_LARGE_0: EnumParseTester.SeqLarge
    SEQ_LARGE_1: EnumParseTester.SeqLarge
    SEQ_LARGE_2: EnumParseTester.SeqLarge
    SEQ_LARGE_3: EnumParseTester.SeqLarge
    SEQ_LARGE_4: EnumParseTester.SeqLarge
    SEQ_LARGE_5: EnumParseTester.SeqLarge
    SEQ_LARGE_6: EnumParseTester.SeqLarge
    SEQ_LARGE_7: EnumParseTester.SeqLarge
    SEQ_LARGE_8: EnumParseTester.SeqLarge
    SEQ_LARGE_9: EnumParseTester.SeqLarge
    SEQ_LARGE_10: EnumParseTester.SeqLarge
    SEQ_LARGE_11: EnumParseTester.SeqLarge
    SEQ_LARGE_12: EnumParseTester.SeqLarge
    SEQ_LARGE_13: EnumParseTester.SeqLarge
    SEQ_LARGE_14: EnumParseTester.SeqLarge
    SEQ_LARGE_15: EnumParseTester.SeqLarge
    SEQ_LARGE_16: EnumParseTester.SeqLarge
    SEQ_LARGE_17: EnumParseTester.SeqLarge
    SEQ_LARGE_18: EnumParseTester.SeqLarge
    SEQ_LARGE_19: EnumParseTester.SeqLarge
    SEQ_LARGE_20: EnumParseTester.SeqLarge
    SEQ_LARGE_21: EnumParseTester.SeqLarge
    SEQ_LARGE_22: EnumParseTester.SeqLarge
    SEQ_LARGE_23: EnumParseTester.SeqLarge
    SEQ_LARGE_24: EnumParseTester.SeqLarge
    SEQ_LARGE_25: EnumParseTester.SeqLarge
    SEQ_LARGE_26: EnumParseTester.SeqLarge
    SEQ_LARGE_27: EnumParseTester.SeqLarge
    SEQ_LARGE_28: EnumParseTester.SeqLarge
    SEQ_LARGE_29: EnumParseTester.SeqLarge
    SEQ_LARGE_30: EnumParseTester.SeqLarge
    SEQ_LARGE_31: EnumParseTester.SeqLarge
    SEQ_LARGE_32: EnumParseTester.SeqLarge
    SEQ_LARGE_33: EnumParseTester.SeqLarge
    class Arbitrary(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARBITRARY_DEFAULT: _ClassVar[EnumParseTester.Arbitrary]
        ARBITRARY_1: _ClassVar[EnumParseTester.Arbitrary]
        ARBITRARY_2: _ClassVar[EnumParseTester.Arbitrary]
        ARBITRARY_3: _ClassVar[EnumParseTester.Arbitrary]
        ARBITRARY_MIN: _ClassVar[EnumParseTester.Arbitrary]
        ARBITRARY_MAX: _ClassVar[EnumParseTester.Arbitrary]
    ARBITRARY_DEFAULT: EnumParseTester.Arbitrary
    ARBITRARY_1: EnumParseTester.Arbitrary
    ARBITRARY_2: EnumParseTester.Arbitrary
    ARBITRARY_3: EnumParseTester.Arbitrary
    ARBITRARY_MIN: EnumParseTester.Arbitrary
    ARBITRARY_MAX: EnumParseTester.Arbitrary
    OPTIONAL_ARBITRARY_EXT_FIELD_NUMBER: _ClassVar[int]
    optional_arbitrary_ext: _descriptor.FieldDescriptor
    REPEATED_ARBITRARY_EXT_FIELD_NUMBER: _ClassVar[int]
    repeated_arbitrary_ext: _descriptor.FieldDescriptor
    PACKED_ARBITRARY_EXT_FIELD_NUMBER: _ClassVar[int]
    packed_arbitrary_ext: _descriptor.FieldDescriptor
    OPTIONAL_SEQ_SMALL_0_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SEQ_SMALL_0_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SEQ_SMALL_0_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_SMALL_0_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_SMALL_0_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_SMALL_0_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_SMALL_0_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_SMALL_0_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_SMALL_0_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SEQ_SMALL_1_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SEQ_SMALL_1_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SEQ_SMALL_1_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_SMALL_1_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_SMALL_1_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_SMALL_1_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_SMALL_1_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_SMALL_1_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_SMALL_1_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SEQ_LARGE_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SEQ_LARGE_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SEQ_LARGE_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_LARGE_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_LARGE_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SEQ_LARGE_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_LARGE_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_LARGE_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_SEQ_LARGE_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ARBITRARY_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ARBITRARY_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ARBITRARY_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ARBITRARY_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ARBITRARY_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ARBITRARY_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_ARBITRARY_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_ARBITRARY_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_ARBITRARY_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
    optional_seq_small_0_lowfield: EnumParseTester.SeqSmall0
    optional_seq_small_0_midfield: EnumParseTester.SeqSmall0
    optional_seq_small_0_hifield: EnumParseTester.SeqSmall0
    repeated_seq_small_0_lowfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall0]
    repeated_seq_small_0_midfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall0]
    repeated_seq_small_0_hifield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall0]
    packed_seq_small_0_lowfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall0]
    packed_seq_small_0_midfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall0]
    packed_seq_small_0_hifield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall0]
    optional_seq_small_1_lowfield: EnumParseTester.SeqSmall1
    optional_seq_small_1_midfield: EnumParseTester.SeqSmall1
    optional_seq_small_1_hifield: EnumParseTester.SeqSmall1
    repeated_seq_small_1_lowfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall1]
    repeated_seq_small_1_midfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall1]
    repeated_seq_small_1_hifield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall1]
    packed_seq_small_1_lowfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall1]
    packed_seq_small_1_midfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall1]
    packed_seq_small_1_hifield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqSmall1]
    optional_seq_large_lowfield: EnumParseTester.SeqLarge
    optional_seq_large_midfield: EnumParseTester.SeqLarge
    optional_seq_large_hifield: EnumParseTester.SeqLarge
    repeated_seq_large_lowfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqLarge]
    repeated_seq_large_midfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqLarge]
    repeated_seq_large_hifield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqLarge]
    packed_seq_large_lowfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqLarge]
    packed_seq_large_midfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqLarge]
    packed_seq_large_hifield: _containers.RepeatedScalarFieldContainer[EnumParseTester.SeqLarge]
    optional_arbitrary_lowfield: EnumParseTester.Arbitrary
    optional_arbitrary_midfield: EnumParseTester.Arbitrary
    optional_arbitrary_hifield: EnumParseTester.Arbitrary
    repeated_arbitrary_lowfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.Arbitrary]
    repeated_arbitrary_midfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.Arbitrary]
    repeated_arbitrary_hifield: _containers.RepeatedScalarFieldContainer[EnumParseTester.Arbitrary]
    packed_arbitrary_lowfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.Arbitrary]
    packed_arbitrary_midfield: _containers.RepeatedScalarFieldContainer[EnumParseTester.Arbitrary]
    packed_arbitrary_hifield: _containers.RepeatedScalarFieldContainer[EnumParseTester.Arbitrary]
    other_field: int
    def __init__(self, optional_seq_small_0_lowfield: _Optional[_Union[EnumParseTester.SeqSmall0, str]] = ..., optional_seq_small_0_midfield: _Optional[_Union[EnumParseTester.SeqSmall0, str]] = ..., optional_seq_small_0_hifield: _Optional[_Union[EnumParseTester.SeqSmall0, str]] = ..., repeated_seq_small_0_lowfield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall0, str]]] = ..., repeated_seq_small_0_midfield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall0, str]]] = ..., repeated_seq_small_0_hifield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall0, str]]] = ..., packed_seq_small_0_lowfield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall0, str]]] = ..., packed_seq_small_0_midfield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall0, str]]] = ..., packed_seq_small_0_hifield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall0, str]]] = ..., optional_seq_small_1_lowfield: _Optional[_Union[EnumParseTester.SeqSmall1, str]] = ..., optional_seq_small_1_midfield: _Optional[_Union[EnumParseTester.SeqSmall1, str]] = ..., optional_seq_small_1_hifield: _Optional[_Union[EnumParseTester.SeqSmall1, str]] = ..., repeated_seq_small_1_lowfield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall1, str]]] = ..., repeated_seq_small_1_midfield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall1, str]]] = ..., repeated_seq_small_1_hifield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall1, str]]] = ..., packed_seq_small_1_lowfield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall1, str]]] = ..., packed_seq_small_1_midfield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall1, str]]] = ..., packed_seq_small_1_hifield: _Optional[_Iterable[_Union[EnumParseTester.SeqSmall1, str]]] = ..., optional_seq_large_lowfield: _Optional[_Union[EnumParseTester.SeqLarge, str]] = ..., optional_seq_large_midfield: _Optional[_Union[EnumParseTester.SeqLarge, str]] = ..., optional_seq_large_hifield: _Optional[_Union[EnumParseTester.SeqLarge, str]] = ..., repeated_seq_large_lowfield: _Optional[_Iterable[_Union[EnumParseTester.SeqLarge, str]]] = ..., repeated_seq_large_midfield: _Optional[_Iterable[_Union[EnumParseTester.SeqLarge, str]]] = ..., repeated_seq_large_hifield: _Optional[_Iterable[_Union[EnumParseTester.SeqLarge, str]]] = ..., packed_seq_large_lowfield: _Optional[_Iterable[_Union[EnumParseTester.SeqLarge, str]]] = ..., packed_seq_large_midfield: _Optional[_Iterable[_Union[EnumParseTester.SeqLarge, str]]] = ..., packed_seq_large_hifield: _Optional[_Iterable[_Union[EnumParseTester.SeqLarge, str]]] = ..., optional_arbitrary_lowfield: _Optional[_Union[EnumParseTester.Arbitrary, str]] = ..., optional_arbitrary_midfield: _Optional[_Union[EnumParseTester.Arbitrary, str]] = ..., optional_arbitrary_hifield: _Optional[_Union[EnumParseTester.Arbitrary, str]] = ..., repeated_arbitrary_lowfield: _Optional[_Iterable[_Union[EnumParseTester.Arbitrary, str]]] = ..., repeated_arbitrary_midfield: _Optional[_Iterable[_Union[EnumParseTester.Arbitrary, str]]] = ..., repeated_arbitrary_hifield: _Optional[_Iterable[_Union[EnumParseTester.Arbitrary, str]]] = ..., packed_arbitrary_lowfield: _Optional[_Iterable[_Union[EnumParseTester.Arbitrary, str]]] = ..., packed_arbitrary_midfield: _Optional[_Iterable[_Union[EnumParseTester.Arbitrary, str]]] = ..., packed_arbitrary_hifield: _Optional[_Iterable[_Union[EnumParseTester.Arbitrary, str]]] = ..., other_field: _Optional[int] = ...) -> None: ...

class BoolParseTester(_message.Message):
    __slots__ = ("optional_bool_lowfield", "optional_bool_midfield", "optional_bool_hifield", "repeated_bool_lowfield", "repeated_bool_midfield", "repeated_bool_hifield", "packed_bool_lowfield", "packed_bool_midfield", "packed_bool_hifield", "other_field")
    Extensions: _python_message._ExtensionDict
    OPTIONAL_BOOL_EXT_FIELD_NUMBER: _ClassVar[int]
    optional_bool_ext: _descriptor.FieldDescriptor
    REPEATED_BOOL_EXT_FIELD_NUMBER: _ClassVar[int]
    repeated_bool_ext: _descriptor.FieldDescriptor
    PACKED_BOOL_EXT_FIELD_NUMBER: _ClassVar[int]
    packed_bool_ext: _descriptor.FieldDescriptor
    OPTIONAL_BOOL_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BOOL_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BOOL_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_BOOL_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_BOOL_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_BOOL_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
    optional_bool_lowfield: bool
    optional_bool_midfield: bool
    optional_bool_hifield: bool
    repeated_bool_lowfield: _containers.RepeatedScalarFieldContainer[bool]
    repeated_bool_midfield: _containers.RepeatedScalarFieldContainer[bool]
    repeated_bool_hifield: _containers.RepeatedScalarFieldContainer[bool]
    packed_bool_lowfield: _containers.RepeatedScalarFieldContainer[bool]
    packed_bool_midfield: _containers.RepeatedScalarFieldContainer[bool]
    packed_bool_hifield: _containers.RepeatedScalarFieldContainer[bool]
    other_field: int
    def __init__(self, optional_bool_lowfield: bool = ..., optional_bool_midfield: bool = ..., optional_bool_hifield: bool = ..., repeated_bool_lowfield: _Optional[_Iterable[bool]] = ..., repeated_bool_midfield: _Optional[_Iterable[bool]] = ..., repeated_bool_hifield: _Optional[_Iterable[bool]] = ..., packed_bool_lowfield: _Optional[_Iterable[bool]] = ..., packed_bool_midfield: _Optional[_Iterable[bool]] = ..., packed_bool_hifield: _Optional[_Iterable[bool]] = ..., other_field: _Optional[int] = ...) -> None: ...

class Int32ParseTester(_message.Message):
    __slots__ = ("optional_int32_lowfield", "optional_int32_midfield", "optional_int32_hifield", "repeated_int32_lowfield", "repeated_int32_midfield", "repeated_int32_hifield", "packed_int32_lowfield", "packed_int32_midfield", "packed_int32_hifield", "other_field")
    Extensions: _python_message._ExtensionDict
    OPTIONAL_INT32_EXT_FIELD_NUMBER: _ClassVar[int]
    optional_int32_ext: _descriptor.FieldDescriptor
    REPEATED_INT32_EXT_FIELD_NUMBER: _ClassVar[int]
    repeated_int32_ext: _descriptor.FieldDescriptor
    PACKED_INT32_EXT_FIELD_NUMBER: _ClassVar[int]
    packed_int32_ext: _descriptor.FieldDescriptor
    OPTIONAL_INT32_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT32_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT32_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT32_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT32_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
    optional_int32_lowfield: int
    optional_int32_midfield: int
    optional_int32_hifield: int
    repeated_int32_lowfield: _containers.RepeatedScalarFieldContainer[int]
    repeated_int32_midfield: _containers.RepeatedScalarFieldContainer[int]
    repeated_int32_hifield: _containers.RepeatedScalarFieldContainer[int]
    packed_int32_lowfield: _containers.RepeatedScalarFieldContainer[int]
    packed_int32_midfield: _containers.RepeatedScalarFieldContainer[int]
    packed_int32_hifield: _containers.RepeatedScalarFieldContainer[int]
    other_field: int
    def __init__(self, optional_int32_lowfield: _Optional[int] = ..., optional_int32_midfield: _Optional[int] = ..., optional_int32_hifield: _Optional[int] = ..., repeated_int32_lowfield: _Optional[_Iterable[int]] = ..., repeated_int32_midfield: _Optional[_Iterable[int]] = ..., repeated_int32_hifield: _Optional[_Iterable[int]] = ..., packed_int32_lowfield: _Optional[_Iterable[int]] = ..., packed_int32_midfield: _Optional[_Iterable[int]] = ..., packed_int32_hifield: _Optional[_Iterable[int]] = ..., other_field: _Optional[int] = ...) -> None: ...

class Int64ParseTester(_message.Message):
    __slots__ = ("optional_int64_lowfield", "optional_int64_midfield", "optional_int64_hifield", "repeated_int64_lowfield", "repeated_int64_midfield", "repeated_int64_hifield", "packed_int64_lowfield", "packed_int64_midfield", "packed_int64_hifield", "other_field")
    Extensions: _python_message._ExtensionDict
    OPTIONAL_INT64_EXT_FIELD_NUMBER: _ClassVar[int]
    optional_int64_ext: _descriptor.FieldDescriptor
    REPEATED_INT64_EXT_FIELD_NUMBER: _ClassVar[int]
    repeated_int64_ext: _descriptor.FieldDescriptor
    PACKED_INT64_EXT_FIELD_NUMBER: _ClassVar[int]
    packed_int64_ext: _descriptor.FieldDescriptor
    OPTIONAL_INT64_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT64_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT64_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    PACKED_INT64_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
    optional_int64_lowfield: int
    optional_int64_midfield: int
    optional_int64_hifield: int
    repeated_int64_lowfield: _containers.RepeatedScalarFieldContainer[int]
    repeated_int64_midfield: _containers.RepeatedScalarFieldContainer[int]
    repeated_int64_hifield: _containers.RepeatedScalarFieldContainer[int]
    packed_int64_lowfield: _containers.RepeatedScalarFieldContainer[int]
    packed_int64_midfield: _containers.RepeatedScalarFieldContainer[int]
    packed_int64_hifield: _containers.RepeatedScalarFieldContainer[int]
    other_field: int
    def __init__(self, optional_int64_lowfield: _Optional[int] = ..., optional_int64_midfield: _Optional[int] = ..., optional_int64_hifield: _Optional[int] = ..., repeated_int64_lowfield: _Optional[_Iterable[int]] = ..., repeated_int64_midfield: _Optional[_Iterable[int]] = ..., repeated_int64_hifield: _Optional[_Iterable[int]] = ..., packed_int64_lowfield: _Optional[_Iterable[int]] = ..., packed_int64_midfield: _Optional[_Iterable[int]] = ..., packed_int64_hifield: _Optional[_Iterable[int]] = ..., other_field: _Optional[int] = ...) -> None: ...

class InlinedStringIdxRegressionProto(_message.Message):
    __slots__ = ("str1", "sub", "str2", "str3")
    STR1_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    STR2_FIELD_NUMBER: _ClassVar[int]
    STR3_FIELD_NUMBER: _ClassVar[int]
    str1: str
    sub: InlinedStringIdxRegressionProto
    str2: str
    str3: bytes
    def __init__(self, str1: _Optional[str] = ..., sub: _Optional[_Union[InlinedStringIdxRegressionProto, _Mapping]] = ..., str2: _Optional[str] = ..., str3: _Optional[bytes] = ...) -> None: ...

class StringParseTester(_message.Message):
    __slots__ = ("optional_string_lowfield", "optional_string_midfield", "optional_string_hifield", "repeated_string_lowfield", "repeated_string_midfield", "repeated_string_hifield")
    Extensions: _python_message._ExtensionDict
    OPTIONAL_STRING_EXT_FIELD_NUMBER: _ClassVar[int]
    optional_string_ext: _descriptor.FieldDescriptor
    REPEATED_STRING_EXT_FIELD_NUMBER: _ClassVar[int]
    repeated_string_ext: _descriptor.FieldDescriptor
    OPTIONAL_STRING_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_LOWFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_MIDFIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_HIFIELD_FIELD_NUMBER: _ClassVar[int]
    optional_string_lowfield: str
    optional_string_midfield: str
    optional_string_hifield: str
    repeated_string_lowfield: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_midfield: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_hifield: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, optional_string_lowfield: _Optional[str] = ..., optional_string_midfield: _Optional[str] = ..., optional_string_hifield: _Optional[str] = ..., repeated_string_lowfield: _Optional[_Iterable[str]] = ..., repeated_string_midfield: _Optional[_Iterable[str]] = ..., repeated_string_hifield: _Optional[_Iterable[str]] = ...) -> None: ...

class BadFieldNames(_message.Message):
    __slots__ = ("OptionalInt32",)
    OPTIONALINT32_FIELD_NUMBER: _ClassVar[int]
    FOR_FIELD_NUMBER: _ClassVar[int]
    OptionalInt32: int
    def __init__(self, OptionalInt32: _Optional[int] = ..., **kwargs) -> None: ...

class TestNestedMessageRedaction(_message.Message):
    __slots__ = ("optional_unredacted_nested_string", "optional_redacted_nested_string")
    OPTIONAL_UNREDACTED_NESTED_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_REDACTED_NESTED_STRING_FIELD_NUMBER: _ClassVar[int]
    optional_unredacted_nested_string: str
    optional_redacted_nested_string: str
    def __init__(self, optional_unredacted_nested_string: _Optional[str] = ..., optional_redacted_nested_string: _Optional[str] = ...) -> None: ...

class RedactedFields(_message.Message):
    __slots__ = ("optional_redacted_string", "optional_unredacted_string", "repeated_redacted_string", "repeated_unredacted_string", "optional_redacted_message", "optional_unredacted_message", "repeated_redacted_message", "repeated_unredacted_message", "map_redacted_string", "map_unredacted_string")
    class MapRedactedStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MapUnredactedStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OPTIONAL_REDACTED_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UNREDACTED_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_REDACTED_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UNREDACTED_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_REDACTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UNREDACTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_REDACTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UNREDACTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_REDACTED_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_UNREDACTED_STRING_FIELD_NUMBER: _ClassVar[int]
    optional_redacted_string: str
    optional_unredacted_string: str
    repeated_redacted_string: _containers.RepeatedScalarFieldContainer[str]
    repeated_unredacted_string: _containers.RepeatedScalarFieldContainer[str]
    optional_redacted_message: TestNestedMessageRedaction
    optional_unredacted_message: TestNestedMessageRedaction
    repeated_redacted_message: _containers.RepeatedCompositeFieldContainer[TestNestedMessageRedaction]
    repeated_unredacted_message: _containers.RepeatedCompositeFieldContainer[TestNestedMessageRedaction]
    map_redacted_string: _containers.ScalarMap[str, str]
    map_unredacted_string: _containers.ScalarMap[str, str]
    def __init__(self, optional_redacted_string: _Optional[str] = ..., optional_unredacted_string: _Optional[str] = ..., repeated_redacted_string: _Optional[_Iterable[str]] = ..., repeated_unredacted_string: _Optional[_Iterable[str]] = ..., optional_redacted_message: _Optional[_Union[TestNestedMessageRedaction, _Mapping]] = ..., optional_unredacted_message: _Optional[_Union[TestNestedMessageRedaction, _Mapping]] = ..., repeated_redacted_message: _Optional[_Iterable[_Union[TestNestedMessageRedaction, _Mapping]]] = ..., repeated_unredacted_message: _Optional[_Iterable[_Union[TestNestedMessageRedaction, _Mapping]]] = ..., map_redacted_string: _Optional[_Mapping[str, str]] = ..., map_unredacted_string: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TestCord(_message.Message):
    __slots__ = ("optional_bytes_cord", "optional_bytes_cord_default")
    OPTIONAL_BYTES_CORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_CORD_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    optional_bytes_cord: bytes
    optional_bytes_cord_default: bytes
    def __init__(self, optional_bytes_cord: _Optional[bytes] = ..., optional_bytes_cord_default: _Optional[bytes] = ...) -> None: ...

class TestPackedEnumSmallRange(_message.Message):
    __slots__ = ("vals",)
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TestPackedEnumSmallRange.NestedEnum]
        FOO: _ClassVar[TestPackedEnumSmallRange.NestedEnum]
        BAR: _ClassVar[TestPackedEnumSmallRange.NestedEnum]
        BAZ: _ClassVar[TestPackedEnumSmallRange.NestedEnum]
    UNSPECIFIED: TestPackedEnumSmallRange.NestedEnum
    FOO: TestPackedEnumSmallRange.NestedEnum
    BAR: TestPackedEnumSmallRange.NestedEnum
    BAZ: TestPackedEnumSmallRange.NestedEnum
    VALS_FIELD_NUMBER: _ClassVar[int]
    vals: _containers.RepeatedScalarFieldContainer[TestPackedEnumSmallRange.NestedEnum]
    def __init__(self, vals: _Optional[_Iterable[_Union[TestPackedEnumSmallRange.NestedEnum, str]]] = ...) -> None: ...

class EnumsForBenchmark(_message.Message):
    __slots__ = ()
    class Flat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        A0: _ClassVar[EnumsForBenchmark.Flat]
        A1: _ClassVar[EnumsForBenchmark.Flat]
        A2: _ClassVar[EnumsForBenchmark.Flat]
        A3: _ClassVar[EnumsForBenchmark.Flat]
        A4: _ClassVar[EnumsForBenchmark.Flat]
        A5: _ClassVar[EnumsForBenchmark.Flat]
        A6: _ClassVar[EnumsForBenchmark.Flat]
        A7: _ClassVar[EnumsForBenchmark.Flat]
        A8: _ClassVar[EnumsForBenchmark.Flat]
        A9: _ClassVar[EnumsForBenchmark.Flat]
        A10: _ClassVar[EnumsForBenchmark.Flat]
        A11: _ClassVar[EnumsForBenchmark.Flat]
        A12: _ClassVar[EnumsForBenchmark.Flat]
        A13: _ClassVar[EnumsForBenchmark.Flat]
        A14: _ClassVar[EnumsForBenchmark.Flat]
        A15: _ClassVar[EnumsForBenchmark.Flat]
    A0: EnumsForBenchmark.Flat
    A1: EnumsForBenchmark.Flat
    A2: EnumsForBenchmark.Flat
    A3: EnumsForBenchmark.Flat
    A4: EnumsForBenchmark.Flat
    A5: EnumsForBenchmark.Flat
    A6: EnumsForBenchmark.Flat
    A7: EnumsForBenchmark.Flat
    A8: EnumsForBenchmark.Flat
    A9: EnumsForBenchmark.Flat
    A10: EnumsForBenchmark.Flat
    A11: EnumsForBenchmark.Flat
    A12: EnumsForBenchmark.Flat
    A13: EnumsForBenchmark.Flat
    A14: EnumsForBenchmark.Flat
    A15: EnumsForBenchmark.Flat
    class AlmostFlat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        B0: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B1: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B2: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B3: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B5: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B6: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B7: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B8: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B9: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B11: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B12: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B13: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B14: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B15: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B17: _ClassVar[EnumsForBenchmark.AlmostFlat]
        B19: _ClassVar[EnumsForBenchmark.AlmostFlat]
    B0: EnumsForBenchmark.AlmostFlat
    B1: EnumsForBenchmark.AlmostFlat
    B2: EnumsForBenchmark.AlmostFlat
    B3: EnumsForBenchmark.AlmostFlat
    B5: EnumsForBenchmark.AlmostFlat
    B6: EnumsForBenchmark.AlmostFlat
    B7: EnumsForBenchmark.AlmostFlat
    B8: EnumsForBenchmark.AlmostFlat
    B9: EnumsForBenchmark.AlmostFlat
    B11: EnumsForBenchmark.AlmostFlat
    B12: EnumsForBenchmark.AlmostFlat
    B13: EnumsForBenchmark.AlmostFlat
    B14: EnumsForBenchmark.AlmostFlat
    B15: EnumsForBenchmark.AlmostFlat
    B17: EnumsForBenchmark.AlmostFlat
    B19: EnumsForBenchmark.AlmostFlat
    class Sparse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        C0: _ClassVar[EnumsForBenchmark.Sparse]
        C536: _ClassVar[EnumsForBenchmark.Sparse]
        C8387: _ClassVar[EnumsForBenchmark.Sparse]
        C9673: _ClassVar[EnumsForBenchmark.Sparse]
        C10285: _ClassVar[EnumsForBenchmark.Sparse]
        C13318: _ClassVar[EnumsForBenchmark.Sparse]
        C15963: _ClassVar[EnumsForBenchmark.Sparse]
        C16439: _ClassVar[EnumsForBenchmark.Sparse]
        C18197: _ClassVar[EnumsForBenchmark.Sparse]
        C19430: _ClassVar[EnumsForBenchmark.Sparse]
        C20361: _ClassVar[EnumsForBenchmark.Sparse]
        C20706: _ClassVar[EnumsForBenchmark.Sparse]
        C21050: _ClassVar[EnumsForBenchmark.Sparse]
        C21906: _ClassVar[EnumsForBenchmark.Sparse]
        C27265: _ClassVar[EnumsForBenchmark.Sparse]
        C30109: _ClassVar[EnumsForBenchmark.Sparse]
        C31670: _ClassVar[EnumsForBenchmark.Sparse]
    C0: EnumsForBenchmark.Sparse
    C536: EnumsForBenchmark.Sparse
    C8387: EnumsForBenchmark.Sparse
    C9673: EnumsForBenchmark.Sparse
    C10285: EnumsForBenchmark.Sparse
    C13318: EnumsForBenchmark.Sparse
    C15963: EnumsForBenchmark.Sparse
    C16439: EnumsForBenchmark.Sparse
    C18197: EnumsForBenchmark.Sparse
    C19430: EnumsForBenchmark.Sparse
    C20361: EnumsForBenchmark.Sparse
    C20706: EnumsForBenchmark.Sparse
    C21050: EnumsForBenchmark.Sparse
    C21906: EnumsForBenchmark.Sparse
    C27265: EnumsForBenchmark.Sparse
    C30109: EnumsForBenchmark.Sparse
    C31670: EnumsForBenchmark.Sparse
    def __init__(self) -> None: ...

class TestMessageWithManyRepeatedPtrFields(_message.Message):
    __slots__ = ("repeated_string_1", "repeated_string_2", "repeated_string_3", "repeated_string_4", "repeated_string_5", "repeated_string_6", "repeated_string_7", "repeated_string_8", "repeated_string_9", "repeated_string_10", "repeated_string_11", "repeated_string_12", "repeated_string_13", "repeated_string_14", "repeated_string_15", "repeated_string_16", "repeated_string_17", "repeated_string_18", "repeated_string_19", "repeated_string_20", "repeated_string_21", "repeated_string_22", "repeated_string_23", "repeated_string_24", "repeated_string_25", "repeated_string_26", "repeated_string_27", "repeated_string_28", "repeated_string_29", "repeated_string_30", "repeated_string_31", "repeated_string_32")
    REPEATED_STRING_1_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_2_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_3_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_4_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_5_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_6_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_7_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_8_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_9_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_10_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_11_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_12_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_13_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_14_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_15_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_16_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_17_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_18_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_19_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_20_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_21_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_22_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_23_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_24_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_25_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_26_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_27_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_28_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_29_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_30_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_31_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_32_FIELD_NUMBER: _ClassVar[int]
    repeated_string_1: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_2: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_3: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_4: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_5: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_6: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_7: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_8: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_9: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_10: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_11: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_12: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_13: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_14: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_15: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_16: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_17: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_18: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_19: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_20: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_21: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_22: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_23: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_24: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_25: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_26: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_27: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_28: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_29: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_30: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_31: _containers.RepeatedScalarFieldContainer[str]
    repeated_string_32: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, repeated_string_1: _Optional[_Iterable[str]] = ..., repeated_string_2: _Optional[_Iterable[str]] = ..., repeated_string_3: _Optional[_Iterable[str]] = ..., repeated_string_4: _Optional[_Iterable[str]] = ..., repeated_string_5: _Optional[_Iterable[str]] = ..., repeated_string_6: _Optional[_Iterable[str]] = ..., repeated_string_7: _Optional[_Iterable[str]] = ..., repeated_string_8: _Optional[_Iterable[str]] = ..., repeated_string_9: _Optional[_Iterable[str]] = ..., repeated_string_10: _Optional[_Iterable[str]] = ..., repeated_string_11: _Optional[_Iterable[str]] = ..., repeated_string_12: _Optional[_Iterable[str]] = ..., repeated_string_13: _Optional[_Iterable[str]] = ..., repeated_string_14: _Optional[_Iterable[str]] = ..., repeated_string_15: _Optional[_Iterable[str]] = ..., repeated_string_16: _Optional[_Iterable[str]] = ..., repeated_string_17: _Optional[_Iterable[str]] = ..., repeated_string_18: _Optional[_Iterable[str]] = ..., repeated_string_19: _Optional[_Iterable[str]] = ..., repeated_string_20: _Optional[_Iterable[str]] = ..., repeated_string_21: _Optional[_Iterable[str]] = ..., repeated_string_22: _Optional[_Iterable[str]] = ..., repeated_string_23: _Optional[_Iterable[str]] = ..., repeated_string_24: _Optional[_Iterable[str]] = ..., repeated_string_25: _Optional[_Iterable[str]] = ..., repeated_string_26: _Optional[_Iterable[str]] = ..., repeated_string_27: _Optional[_Iterable[str]] = ..., repeated_string_28: _Optional[_Iterable[str]] = ..., repeated_string_29: _Optional[_Iterable[str]] = ..., repeated_string_30: _Optional[_Iterable[str]] = ..., repeated_string_31: _Optional[_Iterable[str]] = ..., repeated_string_32: _Optional[_Iterable[str]] = ...) -> None: ...
