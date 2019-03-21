# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groups/v2/groups_common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='groups/v2/groups_common.proto',
  package='common.groups.v2',
  syntax='proto3',
  serialized_pb=_b('\n\x1dgroups/v2/groups_common.proto\x12\x10\x63ommon.groups.v2\x1a\x19protobuf_validation.proto\"G\n\x11PublicGroupFields\x12\x32\n\x07hashtag\x18\x01 \x01(\x0b\x32\x19.common.groups.v2.HashtagB\x06\xca\x9d%\x02\x08\x01\"3\n\x07Hashtag\x12(\n\x07hashtag\x18\x01 \x01(\tB\x17\xca\x9d%\x13\x08\x01\x12\x0f^#[\\w\\.]{2,32}$By\n\x15\x63om.kik.gen.groups.v2ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/groups/v2;groups\xa2\x02\x11KPBCommonGroupsV2b\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PUBLICGROUPFIELDS = _descriptor.Descriptor(
  name='PublicGroupFields',
  full_name='common.groups.v2.PublicGroupFields',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashtag', full_name='common.groups.v2.PublicGroupFields.hashtag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=149,
)


_HASHTAG = _descriptor.Descriptor(
  name='Hashtag',
  full_name='common.groups.v2.Hashtag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashtag', full_name='common.groups.v2.Hashtag.hashtag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\023\010\001\022\017^#[\\w\\.]{2,32}$'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=202,
)

_PUBLICGROUPFIELDS.fields_by_name['hashtag'].message_type = _HASHTAG
DESCRIPTOR.message_types_by_name['PublicGroupFields'] = _PUBLICGROUPFIELDS
DESCRIPTOR.message_types_by_name['Hashtag'] = _HASHTAG

PublicGroupFields = _reflection.GeneratedProtocolMessageType('PublicGroupFields', (_message.Message,), dict(
  DESCRIPTOR = _PUBLICGROUPFIELDS,
  __module__ = 'groups.v2.groups_common_pb2'
  # @@protoc_insertion_point(class_scope:common.groups.v2.PublicGroupFields)
  ))
_sym_db.RegisterMessage(PublicGroupFields)

Hashtag = _reflection.GeneratedProtocolMessageType('Hashtag', (_message.Message,), dict(
  DESCRIPTOR = _HASHTAG,
  __module__ = 'groups.v2.groups_common_pb2'
  # @@protoc_insertion_point(class_scope:common.groups.v2.Hashtag)
  ))
_sym_db.RegisterMessage(Hashtag)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.kik.gen.groups.v2ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/groups/v2;groups\242\002\021KPBCommonGroupsV2'))
_PUBLICGROUPFIELDS.fields_by_name['hashtag'].has_options = True
_PUBLICGROUPFIELDS.fields_by_name['hashtag']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_HASHTAG.fields_by_name['hashtag'].has_options = True
_HASHTAG.fields_by_name['hashtag']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\023\010\001\022\017^#[\\w\\.]{2,32}$'))
# @@protoc_insertion_point(module_scope)
