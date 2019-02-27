# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kin/authentication/v1/authentication_common.proto

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
import kik_unofficial.protobuf.common_model_pb2 as common__model__pb2
from kik_unofficial.protobuf.common.v1 import model_pb2 as common_dot_v1_dot_model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kin/authentication/v1/authentication_common.proto',
  package='common.kin.authentication.v1',
  syntax='proto3',
  serialized_pb=_b('\n1kin/authentication/v1/authentication_common.proto\x12\x1c\x63ommon.kin.authentication.v1\x1a\x19protobuf_validation.proto\x1a\x12\x63ommon_model.proto\x1a\x15\x63ommon/v1/model.proto\"_\n\x07OfferId\x12$\n\nproduct_id\x18\x01 \x01(\x0b\x32\x0e.common.XiUuidH\x00\x12%\n\x10\x66\x65\x61ture_offer_id\x18\x02 \x01(\tB\t\xca\x9d%\x05(\x01\x30\x80\x01H\x00\x42\x07\n\x05value\"l\n\x08OfferJwt\x12\x39\n\x02id\x18\x01 \x01(\x0b\x32%.common.kin.authentication.v1.OfferIdB\x06\xca\x9d%\x02\x08\x01\x12%\n\x03jwt\x18\x02 \x01(\x0b\x32\x10.common.v1.XiJWTB\x06\xca\x9d%\x02\x08\x01\x42\x84\x01\n com.kik.kin.authentication.modelZ`github.com/kikinteractive/xiphias-model-common/generated/go/kin/authentication/v1;authenticationb\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,common__model__pb2.DESCRIPTOR,common_dot_v1_dot_model__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_OFFERID = _descriptor.Descriptor(
  name='OfferId',
  full_name='common.kin.authentication.v1.OfferId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='common.kin.authentication.v1.OfferId.product_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_offer_id', full_name='common.kin.authentication.v1.OfferId.feature_offer_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005(\0010\200\001'))),
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
    _descriptor.OneofDescriptor(
      name='value', full_name='common.kin.authentication.v1.OfferId.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=153,
  serialized_end=248,
)


_OFFERJWT = _descriptor.Descriptor(
  name='OfferJwt',
  full_name='common.kin.authentication.v1.OfferJwt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='common.kin.authentication.v1.OfferJwt.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='jwt', full_name='common.kin.authentication.v1.OfferJwt.jwt', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=250,
  serialized_end=358,
)

_OFFERID.fields_by_name['product_id'].message_type = common__model__pb2._XIUUID
_OFFERID.oneofs_by_name['value'].fields.append(
  _OFFERID.fields_by_name['product_id'])
_OFFERID.fields_by_name['product_id'].containing_oneof = _OFFERID.oneofs_by_name['value']
_OFFERID.oneofs_by_name['value'].fields.append(
  _OFFERID.fields_by_name['feature_offer_id'])
_OFFERID.fields_by_name['feature_offer_id'].containing_oneof = _OFFERID.oneofs_by_name['value']
_OFFERJWT.fields_by_name['id'].message_type = _OFFERID
_OFFERJWT.fields_by_name['jwt'].message_type = common_dot_v1_dot_model__pb2._XIJWT
DESCRIPTOR.message_types_by_name['OfferId'] = _OFFERID
DESCRIPTOR.message_types_by_name['OfferJwt'] = _OFFERJWT

OfferId = _reflection.GeneratedProtocolMessageType('OfferId', (_message.Message,), dict(
  DESCRIPTOR = _OFFERID,
  __module__ = 'kin.authentication.v1.authentication_common_pb2'
  # @@protoc_insertion_point(class_scope:common.kin.authentication.v1.OfferId)
  ))
_sym_db.RegisterMessage(OfferId)

OfferJwt = _reflection.GeneratedProtocolMessageType('OfferJwt', (_message.Message,), dict(
  DESCRIPTOR = _OFFERJWT,
  __module__ = 'kin.authentication.v1.authentication_common_pb2'
  # @@protoc_insertion_point(class_scope:common.kin.authentication.v1.OfferJwt)
  ))
_sym_db.RegisterMessage(OfferJwt)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.kik.kin.authentication.modelZ`github.com/kikinteractive/xiphias-model-common/generated/go/kin/authentication/v1;authentication'))
_OFFERID.fields_by_name['feature_offer_id'].has_options = True
_OFFERID.fields_by_name['feature_offer_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005(\0010\200\001'))
_OFFERJWT.fields_by_name['id'].has_options = True
_OFFERJWT.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_OFFERJWT.fields_by_name['jwt'].has_options = True
_OFFERJWT.fields_by_name['jwt']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
# @@protoc_insertion_point(module_scope)
