"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'cosmos/slashing/v1beta1/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/slashing/v1beta1/genesis.proto\x12\x17cosmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\x1a\x19cosmos_proto/cosmos.proto"\xd5\x01\n\x0cGenesisState\x125\n\x06params\x18\x01 \x01(\x0b2\x1f.cosmos.slashing.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12A\n\rsigning_infos\x18\x02 \x03(\x0b2$.cosmos.slashing.v1beta1.SigningInfoB\x04\xc8\xde\x1f\x00\x12K\n\rmissed_blocks\x18\x03 \x03(\x0b2..cosmos.slashing.v1beta1.ValidatorMissedBlocksB\x04\xc8\xde\x1f\x00"\x8d\x01\n\x0bSigningInfo\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12S\n\x16validator_signing_info\x18\x02 \x01(\x0b2-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\x04\xc8\xde\x1f\x00"\x85\x01\n\x15ValidatorMissedBlocks\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12A\n\rmissed_blocks\x18\x02 \x03(\x0b2$.cosmos.slashing.v1beta1.MissedBlockB\x04\xc8\xde\x1f\x00",\n\x0bMissedBlock\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x0e\n\x06missed\x18\x02 \x01(\x08B/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
    _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['signing_infos']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['signing_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['missed_blocks']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['missed_blocks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_SIGNINGINFO'].fields_by_name['address']._loaded_options = None
    _globals['_SIGNINGINFO'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_SIGNINGINFO'].fields_by_name['validator_signing_info']._loaded_options = None
    _globals['_SIGNINGINFO'].fields_by_name['validator_signing_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['address']._loaded_options = None
    _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['missed_blocks']._loaded_options = None
    _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['missed_blocks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 156
    _globals['_GENESISSTATE']._serialized_end = 369
    _globals['_SIGNINGINFO']._serialized_start = 372
    _globals['_SIGNINGINFO']._serialized_end = 513
    _globals['_VALIDATORMISSEDBLOCKS']._serialized_start = 516
    _globals['_VALIDATORMISSEDBLOCKS']._serialized_end = 649
    _globals['_MISSEDBLOCK']._serialized_start = 651
    _globals['_MISSEDBLOCK']._serialized_end = 695