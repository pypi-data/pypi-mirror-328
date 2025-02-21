"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'cosmos/crisis/v1beta1/tx.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/crisis/v1beta1/tx.proto\x12\x15cosmos.crisis.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto"\x8b\x01\n\x12MsgVerifyInvariant\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x1d\n\x15invariant_module_name\x18\x02 \x01(\t\x12\x17\n\x0finvariant_route\x18\x03 \x01(\t:\x13\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender"\x1c\n\x1aMsgVerifyInvariantResponse2v\n\x03Msg\x12o\n\x0fVerifyInvariant\x12).cosmos.crisis.v1beta1.MsgVerifyInvariant\x1a1.cosmos.crisis.v1beta1.MsgVerifyInvariantResponseB-Z+github.com/cosmos/cosmos-sdk/x/crisis/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crisis.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/crisis/types'
    _globals['_MSGVERIFYINVARIANT'].fields_by_name['sender']._loaded_options = None
    _globals['_MSGVERIFYINVARIANT'].fields_by_name['sender']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGVERIFYINVARIANT']._loaded_options = None
    _globals['_MSGVERIFYINVARIANT']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender'
    _globals['_MSGVERIFYINVARIANT']._serialized_start = 132
    _globals['_MSGVERIFYINVARIANT']._serialized_end = 271
    _globals['_MSGVERIFYINVARIANTRESPONSE']._serialized_start = 273
    _globals['_MSGVERIFYINVARIANTRESPONSE']._serialized_end = 301
    _globals['_MSG']._serialized_start = 303
    _globals['_MSG']._serialized_end = 421