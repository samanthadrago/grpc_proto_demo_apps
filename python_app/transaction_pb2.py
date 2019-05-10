# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11transaction.proto\x12\x02pb\"\xce\x01\n\x0bTransaction\x12\x12\n\naccount_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x02\x12\x18\n\x10transaction_date\x18\x03 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0f\n\x07\x66x_rate\x18\x05 \x01(\x02\x12\x31\n\x0c\x61\x63\x63ount_type\x18\x06 \x01(\x0e\x32\x1b.pb.Transaction.AccountType\"(\n\x0b\x41\x63\x63ountType\x12\x08\n\x04\x42\x41NK\x10\x00\x12\x0f\n\x0b\x43REDIT_CARD\x10\x01\"5\n\x0cTransactions\x12%\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x0f.pb.Transaction\"\x0e\n\x0c\x46\x65tchRequest2O\n\x12TransactionService\x12\x39\n\x11\x46\x65tchTransactions\x12\x10.pb.FetchRequest\x1a\x10.pb.Transactions\"\x00\x62\x06proto3')
)



_TRANSACTION_ACCOUNTTYPE = _descriptor.EnumDescriptor(
  name='AccountType',
  full_name='pb.Transaction.AccountType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BANK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREDIT_CARD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=192,
  serialized_end=232,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTION_ACCOUNTTYPE)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='pb.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='pb.Transaction.account_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='pb.Transaction.amount', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_date', full_name='pb.Transaction.transaction_date', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pb.Transaction.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fx_rate', full_name='pb.Transaction.fx_rate', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_type', full_name='pb.Transaction.account_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSACTION_ACCOUNTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=232,
)


_TRANSACTIONS = _descriptor.Descriptor(
  name='Transactions',
  full_name='pb.Transactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='pb.Transactions.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=234,
  serialized_end=287,
)


_FETCHREQUEST = _descriptor.Descriptor(
  name='FetchRequest',
  full_name='pb.FetchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=289,
  serialized_end=303,
)

_TRANSACTION.fields_by_name['account_type'].enum_type = _TRANSACTION_ACCOUNTTYPE
_TRANSACTION_ACCOUNTTYPE.containing_type = _TRANSACTION
_TRANSACTIONS.fields_by_name['transactions'].message_type = _TRANSACTION
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['Transactions'] = _TRANSACTIONS
DESCRIPTOR.message_types_by_name['FetchRequest'] = _FETCHREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:pb.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

Transactions = _reflection.GeneratedProtocolMessageType('Transactions', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONS,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:pb.Transactions)
  ))
_sym_db.RegisterMessage(Transactions)

FetchRequest = _reflection.GeneratedProtocolMessageType('FetchRequest', (_message.Message,), dict(
  DESCRIPTOR = _FETCHREQUEST,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:pb.FetchRequest)
  ))
_sym_db.RegisterMessage(FetchRequest)



_TRANSACTIONSERVICE = _descriptor.ServiceDescriptor(
  name='TransactionService',
  full_name='pb.TransactionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=305,
  serialized_end=384,
  methods=[
  _descriptor.MethodDescriptor(
    name='FetchTransactions',
    full_name='pb.TransactionService.FetchTransactions',
    index=0,
    containing_service=None,
    input_type=_FETCHREQUEST,
    output_type=_TRANSACTIONS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSACTIONSERVICE)

DESCRIPTOR.services_by_name['TransactionService'] = _TRANSACTIONSERVICE

# @@protoc_insertion_point(module_scope)