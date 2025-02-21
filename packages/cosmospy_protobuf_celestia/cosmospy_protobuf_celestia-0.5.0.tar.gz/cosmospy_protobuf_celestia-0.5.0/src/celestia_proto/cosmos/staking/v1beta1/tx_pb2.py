"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'cosmos/staking/v1beta1/tx.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/staking/v1beta1/tx.proto\x12\x16cosmos.staking.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x17cosmos/msg/v1/msg.proto"\x82\x04\n\x12MsgCreateValidator\x12>\n\x0bdescription\x18\x01 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\x04\xc8\xde\x1f\x00\x12A\n\ncommission\x18\x02 \x01(\x0b2\'.cosmos.staking.v1beta1.CommissionRatesB\x04\xc8\xde\x1f\x00\x12Y\n\x13min_self_delegation\x18\x03 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int\x123\n\x11delegator_address\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x05 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12>\n\x06pubkey\x18\x06 \x01(\x0b2\x14.google.protobuf.AnyB\x18\xca\xb4-\x14cosmos.crypto.PubKey\x12.\n\x05value\x18\x07 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:4\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x82\xe7\xb0*\x11validator_address"\x1c\n\x1aMsgCreateValidatorResponse"\xd1\x02\n\x10MsgEditValidator\x12>\n\x0bdescription\x18\x01 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\x04\xc8\xde\x1f\x00\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12Q\n\x0fcommission_rate\x18\x03 \x01(\tB8\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12U\n\x13min_self_delegation\x18\x04 \x01(\tB8\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int:\x1e\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11validator_address"\x1a\n\x18MsgEditValidatorResponse"\xc4\x01\n\x0bMsgDelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x1a\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address"\x15\n\x13MsgDelegateResponse"\x88\x02\n\x12MsgBeginRedelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x127\n\x15validator_src_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x127\n\x15validator_dst_address\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x1a\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address"[\n\x1aMsgBeginRedelegateResponse\x12=\n\x0fcompletion_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"\xc6\x01\n\rMsgUndelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x1a\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address"V\n\x15MsgUndelegateResponse\x12=\n\x0fcompletion_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"\xee\x01\n\x1cMsgCancelUnbondingDelegation\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x17\n\x0fcreation_height\x18\x04 \x01(\x03:\x1a\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address"&\n$MsgCancelUnbondingDelegationResponse2\xac\x05\n\x03Msg\x12q\n\x0fCreateValidator\x12*.cosmos.staking.v1beta1.MsgCreateValidator\x1a2.cosmos.staking.v1beta1.MsgCreateValidatorResponse\x12k\n\rEditValidator\x12(.cosmos.staking.v1beta1.MsgEditValidator\x1a0.cosmos.staking.v1beta1.MsgEditValidatorResponse\x12\\\n\x08Delegate\x12#.cosmos.staking.v1beta1.MsgDelegate\x1a+.cosmos.staking.v1beta1.MsgDelegateResponse\x12q\n\x0fBeginRedelegate\x12*.cosmos.staking.v1beta1.MsgBeginRedelegate\x1a2.cosmos.staking.v1beta1.MsgBeginRedelegateResponse\x12b\n\nUndelegate\x12%.cosmos.staking.v1beta1.MsgUndelegate\x1a-.cosmos.staking.v1beta1.MsgUndelegateResponse\x12\x8f\x01\n\x19CancelUnbondingDelegation\x124.cosmos.staking.v1beta1.MsgCancelUnbondingDelegation\x1a<.cosmos.staking.v1beta1.MsgCancelUnbondingDelegationResponseB.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['description']._loaded_options = None
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['commission']._loaded_options = None
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['min_self_delegation']._loaded_options = None
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['min_self_delegation']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int'
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['delegator_address']._loaded_options = None
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['validator_address']._loaded_options = None
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['pubkey']._loaded_options = None
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['pubkey']._serialized_options = b'\xca\xb4-\x14cosmos.crypto.PubKey'
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['value']._loaded_options = None
    _globals['_MSGCREATEVALIDATOR'].fields_by_name['value']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGCREATEVALIDATOR']._loaded_options = None
    _globals['_MSGCREATEVALIDATOR']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x82\xe7\xb0*\x11validator_address'
    _globals['_MSGEDITVALIDATOR'].fields_by_name['description']._loaded_options = None
    _globals['_MSGEDITVALIDATOR'].fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGEDITVALIDATOR'].fields_by_name['validator_address']._loaded_options = None
    _globals['_MSGEDITVALIDATOR'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGEDITVALIDATOR'].fields_by_name['commission_rate']._loaded_options = None
    _globals['_MSGEDITVALIDATOR'].fields_by_name['commission_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec'
    _globals['_MSGEDITVALIDATOR'].fields_by_name['min_self_delegation']._loaded_options = None
    _globals['_MSGEDITVALIDATOR'].fields_by_name['min_self_delegation']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int'
    _globals['_MSGEDITVALIDATOR']._loaded_options = None
    _globals['_MSGEDITVALIDATOR']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11validator_address'
    _globals['_MSGDELEGATE'].fields_by_name['delegator_address']._loaded_options = None
    _globals['_MSGDELEGATE'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGDELEGATE'].fields_by_name['validator_address']._loaded_options = None
    _globals['_MSGDELEGATE'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGDELEGATE'].fields_by_name['amount']._loaded_options = None
    _globals['_MSGDELEGATE'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGDELEGATE']._loaded_options = None
    _globals['_MSGDELEGATE']._serialized_options = b'\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address'
    _globals['_MSGBEGINREDELEGATE'].fields_by_name['delegator_address']._loaded_options = None
    _globals['_MSGBEGINREDELEGATE'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGBEGINREDELEGATE'].fields_by_name['validator_src_address']._loaded_options = None
    _globals['_MSGBEGINREDELEGATE'].fields_by_name['validator_src_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGBEGINREDELEGATE'].fields_by_name['validator_dst_address']._loaded_options = None
    _globals['_MSGBEGINREDELEGATE'].fields_by_name['validator_dst_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGBEGINREDELEGATE'].fields_by_name['amount']._loaded_options = None
    _globals['_MSGBEGINREDELEGATE'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGBEGINREDELEGATE']._loaded_options = None
    _globals['_MSGBEGINREDELEGATE']._serialized_options = b'\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address'
    _globals['_MSGBEGINREDELEGATERESPONSE'].fields_by_name['completion_time']._loaded_options = None
    _globals['_MSGBEGINREDELEGATERESPONSE'].fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_MSGUNDELEGATE'].fields_by_name['delegator_address']._loaded_options = None
    _globals['_MSGUNDELEGATE'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGUNDELEGATE'].fields_by_name['validator_address']._loaded_options = None
    _globals['_MSGUNDELEGATE'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGUNDELEGATE'].fields_by_name['amount']._loaded_options = None
    _globals['_MSGUNDELEGATE'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGUNDELEGATE']._loaded_options = None
    _globals['_MSGUNDELEGATE']._serialized_options = b'\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address'
    _globals['_MSGUNDELEGATERESPONSE'].fields_by_name['completion_time']._loaded_options = None
    _globals['_MSGUNDELEGATERESPONSE'].fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_MSGCANCELUNBONDINGDELEGATION'].fields_by_name['delegator_address']._loaded_options = None
    _globals['_MSGCANCELUNBONDINGDELEGATION'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGCANCELUNBONDINGDELEGATION'].fields_by_name['validator_address']._loaded_options = None
    _globals['_MSGCANCELUNBONDINGDELEGATION'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGCANCELUNBONDINGDELEGATION'].fields_by_name['amount']._loaded_options = None
    _globals['_MSGCANCELUNBONDINGDELEGATION'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGCANCELUNBONDINGDELEGATION']._loaded_options = None
    _globals['_MSGCANCELUNBONDINGDELEGATION']._serialized_options = b'\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address'
    _globals['_MSGCREATEVALIDATOR']._serialized_start = 264
    _globals['_MSGCREATEVALIDATOR']._serialized_end = 778
    _globals['_MSGCREATEVALIDATORRESPONSE']._serialized_start = 780
    _globals['_MSGCREATEVALIDATORRESPONSE']._serialized_end = 808
    _globals['_MSGEDITVALIDATOR']._serialized_start = 811
    _globals['_MSGEDITVALIDATOR']._serialized_end = 1148
    _globals['_MSGEDITVALIDATORRESPONSE']._serialized_start = 1150
    _globals['_MSGEDITVALIDATORRESPONSE']._serialized_end = 1176
    _globals['_MSGDELEGATE']._serialized_start = 1179
    _globals['_MSGDELEGATE']._serialized_end = 1375
    _globals['_MSGDELEGATERESPONSE']._serialized_start = 1377
    _globals['_MSGDELEGATERESPONSE']._serialized_end = 1398
    _globals['_MSGBEGINREDELEGATE']._serialized_start = 1401
    _globals['_MSGBEGINREDELEGATE']._serialized_end = 1665
    _globals['_MSGBEGINREDELEGATERESPONSE']._serialized_start = 1667
    _globals['_MSGBEGINREDELEGATERESPONSE']._serialized_end = 1758
    _globals['_MSGUNDELEGATE']._serialized_start = 1761
    _globals['_MSGUNDELEGATE']._serialized_end = 1959
    _globals['_MSGUNDELEGATERESPONSE']._serialized_start = 1961
    _globals['_MSGUNDELEGATERESPONSE']._serialized_end = 2047
    _globals['_MSGCANCELUNBONDINGDELEGATION']._serialized_start = 2050
    _globals['_MSGCANCELUNBONDINGDELEGATION']._serialized_end = 2288
    _globals['_MSGCANCELUNBONDINGDELEGATIONRESPONSE']._serialized_start = 2290
    _globals['_MSGCANCELUNBONDINGDELEGATIONRESPONSE']._serialized_end = 2328
    _globals['_MSG']._serialized_start = 2331
    _globals['_MSG']._serialized_end = 3015