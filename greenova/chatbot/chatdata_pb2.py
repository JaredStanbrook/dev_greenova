# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chatdata.proto
# Protobuf Python Version: 6.30.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    1,
    '',
    'chatdata.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x63hatdata.proto\x12\x08tutorial\"?\n\x0f\x43hatBotResponse\x12\x0e\n\x06prompt\x18\x01 \x02(\t\x12\x10\n\x08response\x18\x02 \x02(\t\x12\n\n\x02id\x18\x03 \x02(\x05\">\n\x0e\x43hatBotPrompts\x12,\n\tresponses\x18\x01 \x03(\x0b\x32\x19.tutorial.ChatBotResponse')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chatdata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CHATBOTRESPONSE']._serialized_start = 28
    _globals['_CHATBOTRESPONSE']._serialized_end = 91
    _globals['_CHATBOTPROMPTS']._serialized_start = 93
    _globals['_CHATBOTPROMPTS']._serialized_end = 155
# @@protoc_insertion_point(module_scope)
