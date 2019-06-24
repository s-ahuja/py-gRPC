# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: digestor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='digestor.proto',
  package='digestor',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x64igestor.proto\x12\x08\x64igestor\x1a\x1cgoogle/api/annotations.proto\"!\n\rDigestMessage\x12\x10\n\x08ToDigest\x18\x01 \x01(\t\"8\n\x0f\x44igestedMessage\x12\x10\n\x08\x44igested\x18\x01 \x01(\t\x12\x13\n\x0bWasDigested\x18\x02 \x01(\x08\x32O\n\x08\x44igestor\x12\x43\n\x0bGetDigestor\x12\x17.digestor.DigestMessage\x1a\x19.digestor.DigestedMessage\"\x00\x32h\n\x0c\x44igestorRest\x12X\n\x0bGetDigestor\x12\x17.digestor.DigestMessage\x1a\x19.digestor.DigestedMessage\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/v1/digest:\x01*b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_DIGESTMESSAGE = _descriptor.Descriptor(
  name='DigestMessage',
  full_name='digestor.DigestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ToDigest', full_name='digestor.DigestMessage.ToDigest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=91,
)


_DIGESTEDMESSAGE = _descriptor.Descriptor(
  name='DigestedMessage',
  full_name='digestor.DigestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Digested', full_name='digestor.DigestedMessage.Digested', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='WasDigested', full_name='digestor.DigestedMessage.WasDigested', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['DigestMessage'] = _DIGESTMESSAGE
DESCRIPTOR.message_types_by_name['DigestedMessage'] = _DIGESTEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DigestMessage = _reflection.GeneratedProtocolMessageType('DigestMessage', (_message.Message,), dict(
  DESCRIPTOR = _DIGESTMESSAGE,
  __module__ = 'digestor_pb2'
  # @@protoc_insertion_point(class_scope:digestor.DigestMessage)
  ))
_sym_db.RegisterMessage(DigestMessage)

DigestedMessage = _reflection.GeneratedProtocolMessageType('DigestedMessage', (_message.Message,), dict(
  DESCRIPTOR = _DIGESTEDMESSAGE,
  __module__ = 'digestor_pb2'
  # @@protoc_insertion_point(class_scope:digestor.DigestedMessage)
  ))
_sym_db.RegisterMessage(DigestedMessage)



_DIGESTOR = _descriptor.ServiceDescriptor(
  name='Digestor',
  full_name='digestor.Digestor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=151,
  serialized_end=230,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDigestor',
    full_name='digestor.Digestor.GetDigestor',
    index=0,
    containing_service=None,
    input_type=_DIGESTMESSAGE,
    output_type=_DIGESTEDMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIGESTOR)

DESCRIPTOR.services_by_name['Digestor'] = _DIGESTOR


_DIGESTORREST = _descriptor.ServiceDescriptor(
  name='DigestorRest',
  full_name='digestor.DigestorRest',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=232,
  serialized_end=336,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDigestor',
    full_name='digestor.DigestorRest.GetDigestor',
    index=0,
    containing_service=None,
    input_type=_DIGESTMESSAGE,
    output_type=_DIGESTEDMESSAGE,
    serialized_options=_b('\202\323\344\223\002\017\"\n/v1/digest:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_DIGESTORREST)

DESCRIPTOR.services_by_name['DigestorRest'] = _DIGESTORREST

# @@protoc_insertion_point(module_scope)