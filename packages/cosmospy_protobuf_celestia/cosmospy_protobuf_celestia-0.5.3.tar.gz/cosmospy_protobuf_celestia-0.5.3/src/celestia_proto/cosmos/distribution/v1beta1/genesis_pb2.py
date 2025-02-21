"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'cosmos/distribution/v1beta1/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/distribution/v1beta1/genesis.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\x1a\x19cosmos_proto/cosmos.proto"\x8a\x01\n\x15DelegatorWithdrawInfo\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x122\n\x10withdraw_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xd2\x01\n!ValidatorOutstandingRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12n\n\x13outstanding_rewards\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xbd\x01\n$ValidatorAccumulatedCommissionRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12V\n\x0baccumulated\x18\x02 \x01(\x0b2;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xc1\x01\n ValidatorHistoricalRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x0e\n\x06period\x18\x02 \x01(\x04\x12N\n\x07rewards\x18\x03 \x01(\x0b27.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xab\x01\n\x1dValidatorCurrentRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12K\n\x07rewards\x18\x02 \x01(\x0b24.cosmos.distribution.v1beta1.ValidatorCurrentRewardsB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xe2\x01\n\x1bDelegatorStartingInfoRecord\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12O\n\rstarting_info\x18\x03 \x01(\x0b22.cosmos.distribution.v1beta1.DelegatorStartingInfoB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xd1\x01\n\x19ValidatorSlashEventRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x0e\n\x06period\x18\x03 \x01(\x04\x12U\n\x15validator_slash_event\x18\x04 \x01(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x89\x07\n\x0cGenesisState\x129\n\x06params\x18\x01 \x01(\x0b2#.cosmos.distribution.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12<\n\x08fee_pool\x18\x02 \x01(\x0b2$.cosmos.distribution.v1beta1.FeePoolB\x04\xc8\xde\x1f\x00\x12Z\n\x18delegator_withdraw_infos\x18\x03 \x03(\x0b22.cosmos.distribution.v1beta1.DelegatorWithdrawInfoB\x04\xc8\xde\x1f\x00\x123\n\x11previous_proposer\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12a\n\x13outstanding_rewards\x18\x05 \x03(\x0b2>.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecordB\x04\xc8\xde\x1f\x00\x12r\n!validator_accumulated_commissions\x18\x06 \x03(\x0b2A.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecordB\x04\xc8\xde\x1f\x00\x12i\n\x1cvalidator_historical_rewards\x18\x07 \x03(\x0b2=.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecordB\x04\xc8\xde\x1f\x00\x12c\n\x19validator_current_rewards\x18\x08 \x03(\x0b2:.cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecordB\x04\xc8\xde\x1f\x00\x12`\n\x18delegator_starting_infos\x18\t \x03(\x0b28.cosmos.distribution.v1beta1.DelegatorStartingInfoRecordB\x04\xc8\xde\x1f\x00\x12\\\n\x16validator_slash_events\x18\n \x03(\x0b26.cosmos.distribution.v1beta1.ValidatorSlashEventRecordB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00B7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _globals['_DELEGATORWITHDRAWINFO'].fields_by_name['delegator_address']._loaded_options = None
    _globals['_DELEGATORWITHDRAWINFO'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_DELEGATORWITHDRAWINFO'].fields_by_name['withdraw_address']._loaded_options = None
    _globals['_DELEGATORWITHDRAWINFO'].fields_by_name['withdraw_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_DELEGATORWITHDRAWINFO']._loaded_options = None
    _globals['_DELEGATORWITHDRAWINFO']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD'].fields_by_name['validator_address']._loaded_options = None
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD'].fields_by_name['outstanding_rewards']._loaded_options = None
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD'].fields_by_name['outstanding_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD']._loaded_options = None
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD'].fields_by_name['validator_address']._loaded_options = None
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD'].fields_by_name['accumulated']._loaded_options = None
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD'].fields_by_name['accumulated']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD']._loaded_options = None
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_VALIDATORHISTORICALREWARDSRECORD'].fields_by_name['validator_address']._loaded_options = None
    _globals['_VALIDATORHISTORICALREWARDSRECORD'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_VALIDATORHISTORICALREWARDSRECORD'].fields_by_name['rewards']._loaded_options = None
    _globals['_VALIDATORHISTORICALREWARDSRECORD'].fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_VALIDATORHISTORICALREWARDSRECORD']._loaded_options = None
    _globals['_VALIDATORHISTORICALREWARDSRECORD']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_VALIDATORCURRENTREWARDSRECORD'].fields_by_name['validator_address']._loaded_options = None
    _globals['_VALIDATORCURRENTREWARDSRECORD'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_VALIDATORCURRENTREWARDSRECORD'].fields_by_name['rewards']._loaded_options = None
    _globals['_VALIDATORCURRENTREWARDSRECORD'].fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_VALIDATORCURRENTREWARDSRECORD']._loaded_options = None
    _globals['_VALIDATORCURRENTREWARDSRECORD']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_DELEGATORSTARTINGINFORECORD'].fields_by_name['delegator_address']._loaded_options = None
    _globals['_DELEGATORSTARTINGINFORECORD'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_DELEGATORSTARTINGINFORECORD'].fields_by_name['validator_address']._loaded_options = None
    _globals['_DELEGATORSTARTINGINFORECORD'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_DELEGATORSTARTINGINFORECORD'].fields_by_name['starting_info']._loaded_options = None
    _globals['_DELEGATORSTARTINGINFORECORD'].fields_by_name['starting_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_DELEGATORSTARTINGINFORECORD']._loaded_options = None
    _globals['_DELEGATORSTARTINGINFORECORD']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_VALIDATORSLASHEVENTRECORD'].fields_by_name['validator_address']._loaded_options = None
    _globals['_VALIDATORSLASHEVENTRECORD'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_VALIDATORSLASHEVENTRECORD'].fields_by_name['validator_slash_event']._loaded_options = None
    _globals['_VALIDATORSLASHEVENTRECORD'].fields_by_name['validator_slash_event']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_VALIDATORSLASHEVENTRECORD']._loaded_options = None
    _globals['_VALIDATORSLASHEVENTRECORD']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['fee_pool']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['fee_pool']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['delegator_withdraw_infos']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['delegator_withdraw_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['previous_proposer']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['previous_proposer']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_GENESISSTATE'].fields_by_name['outstanding_rewards']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['outstanding_rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['validator_accumulated_commissions']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['validator_accumulated_commissions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['validator_historical_rewards']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['validator_historical_rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['validator_current_rewards']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['validator_current_rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['delegator_starting_infos']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['delegator_starting_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['validator_slash_events']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['validator_slash_events']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._loaded_options = None
    _globals['_GENESISSTATE']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_DELEGATORWITHDRAWINFO']._serialized_start = 204
    _globals['_DELEGATORWITHDRAWINFO']._serialized_end = 342
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD']._serialized_start = 345
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD']._serialized_end = 555
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD']._serialized_start = 558
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD']._serialized_end = 747
    _globals['_VALIDATORHISTORICALREWARDSRECORD']._serialized_start = 750
    _globals['_VALIDATORHISTORICALREWARDSRECORD']._serialized_end = 943
    _globals['_VALIDATORCURRENTREWARDSRECORD']._serialized_start = 946
    _globals['_VALIDATORCURRENTREWARDSRECORD']._serialized_end = 1117
    _globals['_DELEGATORSTARTINGINFORECORD']._serialized_start = 1120
    _globals['_DELEGATORSTARTINGINFORECORD']._serialized_end = 1346
    _globals['_VALIDATORSLASHEVENTRECORD']._serialized_start = 1349
    _globals['_VALIDATORSLASHEVENTRECORD']._serialized_end = 1558
    _globals['_GENESISSTATE']._serialized_start = 1561
    _globals['_GENESISSTATE']._serialized_end = 2466