"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'cosmos/vesting/v1beta1/vesting.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/vesting/v1beta1/vesting.proto\x12\x16cosmos.vesting.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/auth/v1beta1/auth.proto"\xa2\x03\n\x12BaseVestingAccount\x12<\n\x0cbase_account\x18\x01 \x01(\x0b2 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12e\n\x10original_vesting\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12c\n\x0edelegated_free\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12f\n\x11delegated_vesting\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x10\n\x08end_time\x18\x05 \x01(\x03:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\x88\x01\n\x18ContinuousVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x12\n\nstart_time\x18\x02 \x01(\x03:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"q\n\x15DelayedVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"{\n\x06Period\x12\x0e\n\x06length\x18\x01 \x01(\x03\x12[\n\x06amount\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x04\x98\xa0\x1f\x00"\xc5\x01\n\x16PeriodicVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12=\n\x0fvesting_periods\x18\x03 \x03(\x0b2\x1e.cosmos.vesting.v1beta1.PeriodB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"r\n\x16PermanentLockedAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00B3Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.vesting.v1beta1.vesting_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['base_account']._loaded_options = None
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['base_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['original_vesting']._loaded_options = None
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['original_vesting']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['delegated_free']._loaded_options = None
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['delegated_free']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['delegated_vesting']._loaded_options = None
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['delegated_vesting']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_BASEVESTINGACCOUNT']._loaded_options = None
    _globals['_BASEVESTINGACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _globals['_CONTINUOUSVESTINGACCOUNT'].fields_by_name['base_vesting_account']._loaded_options = None
    _globals['_CONTINUOUSVESTINGACCOUNT'].fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_CONTINUOUSVESTINGACCOUNT']._loaded_options = None
    _globals['_CONTINUOUSVESTINGACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _globals['_DELAYEDVESTINGACCOUNT'].fields_by_name['base_vesting_account']._loaded_options = None
    _globals['_DELAYEDVESTINGACCOUNT'].fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_DELAYEDVESTINGACCOUNT']._loaded_options = None
    _globals['_DELAYEDVESTINGACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _globals['_PERIOD'].fields_by_name['amount']._loaded_options = None
    _globals['_PERIOD'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_PERIOD']._loaded_options = None
    _globals['_PERIOD']._serialized_options = b'\x98\xa0\x1f\x00'
    _globals['_PERIODICVESTINGACCOUNT'].fields_by_name['base_vesting_account']._loaded_options = None
    _globals['_PERIODICVESTINGACCOUNT'].fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_PERIODICVESTINGACCOUNT'].fields_by_name['vesting_periods']._loaded_options = None
    _globals['_PERIODICVESTINGACCOUNT'].fields_by_name['vesting_periods']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PERIODICVESTINGACCOUNT']._loaded_options = None
    _globals['_PERIODICVESTINGACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _globals['_PERMANENTLOCKEDACCOUNT'].fields_by_name['base_vesting_account']._loaded_options = None
    _globals['_PERMANENTLOCKEDACCOUNT'].fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_PERMANENTLOCKEDACCOUNT']._loaded_options = None
    _globals['_PERMANENTLOCKEDACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _globals['_BASEVESTINGACCOUNT']._serialized_start = 151
    _globals['_BASEVESTINGACCOUNT']._serialized_end = 569
    _globals['_CONTINUOUSVESTINGACCOUNT']._serialized_start = 572
    _globals['_CONTINUOUSVESTINGACCOUNT']._serialized_end = 708
    _globals['_DELAYEDVESTINGACCOUNT']._serialized_start = 710
    _globals['_DELAYEDVESTINGACCOUNT']._serialized_end = 823
    _globals['_PERIOD']._serialized_start = 825
    _globals['_PERIOD']._serialized_end = 948
    _globals['_PERIODICVESTINGACCOUNT']._serialized_start = 951
    _globals['_PERIODICVESTINGACCOUNT']._serialized_end = 1148
    _globals['_PERMANENTLOCKEDACCOUNT']._serialized_start = 1150
    _globals['_PERMANENTLOCKEDACCOUNT']._serialized_end = 1264