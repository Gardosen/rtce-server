# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbadmin/shop.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbrpc import tbrpc_pb2 as tbrpc_dot_tbrpc__pb2
from tbmatch import shop_pb2 as tbmatch_dot_shop__pb2
from tbmatch import query_pb2 as tbmatch_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbadmin/shop.proto',
  package='tbadmin',
  syntax='proto2',
  serialized_pb=_b('\n\x12tbadmin/shop.proto\x12\x07tbadmin\x1a\x11tbrpc/tbrpc.proto\x1a\x12tbmatch/shop.proto\x1a\x13tbmatch/query.proto\"\xfd\x02\n\rOrderCriteria\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12*\n\x0corder_status\x18\x02 \x01(\x0e\x32\x14.tbmatch.OrderStatus\x12\'\n\x0bmodify_time\x18\x03 \x01(\x0b\x32\x12.tbmatch.TimeRange\x12&\n\x10min_total_amount\x18\x05 \x01(\x0b\x32\x0c.tbrpc.Money\x12&\n\x10max_total_amount\x18\x06 \x01(\x0b\x32\x0c.tbrpc.Money\x12\x1b\n\x13use_account_balance\x18\n \x01(\x08\x12,\n\x0e\x62ill_last_name\x18\x0b \x01(\x0b\x32\x14.tbmatch.StringMatch\x12\'\n\tbill_city\x18\x0c \x01(\x0b\x32\x14.tbmatch.StringMatch\x12)\n\x0b\x62ill_region\x18\r \x01(\x0b\x32\x14.tbmatch.StringMatch\x12\x14\n\x0c\x62ill_country\x18\x0e \x01(\t\"\x8c\x01\n\x1bSearchPurchaseOrdersRequest\x12(\n\x08\x63riteria\x18\x01 \x01(\x0b\x32\x16.tbadmin.OrderCriteria\x12 \n\x04sort\x18\x02 \x01(\x0b\x32\x12.tbmatch.OrderSort\x12\x0e\n\x06offset\x18\x05 \x01(\x05\x12\x11\n\x05limit\x18\x06 \x01(\x05:\x02\x31\x30\"Y\n\x1aSearchPurchaseOrdersResult\x12&\n\x06orders\x18\x01 \x03(\x0b\x32\x16.tbmatch.PurchaseOrder\x12\x13\n\x0b\x65nd_of_data\x18\x02 \x01(\x08\"0\n\x18SyncPurchaseOrderRequest\x12\x14\n\x0corder_number\x18\x01 \x01(\x03\"0\n\x18VoidPurchaseOrderRequest\x12\x14\n\x0corder_number\x18\x01 \x01(\x03\"2\n\x1aRefundPurchaseOrderRequest\x12\x14\n\x0corder_number\x18\x01 \x01(\x03\x32\xe3\x02\n\x10ShopAdminService\x12g\n\x14SearchPurchaseOrders\x12$.tbadmin.SearchPurchaseOrdersRequest\x1a#.tbadmin.SearchPurchaseOrdersResult\"\x04\xc8\xf3\x18\x16\x12J\n\x11SyncPurchaseOrder\x12!.tbadmin.SyncPurchaseOrderRequest\x1a\x0c.tbrpc.Empty\"\x04\xc8\xf3\x18\x16\x12J\n\x11VoidPurchaseOrder\x12!.tbadmin.VoidPurchaseOrderRequest\x1a\x0c.tbrpc.Empty\"\x04\xc8\xf3\x18\x17\x12N\n\x13RefundPurchaseOrder\x12#.tbadmin.RefundPurchaseOrderRequest\x1a\x0c.tbrpc.Empty\"\x04\xc8\xf3\x18\x17')
  ,
  dependencies=[tbrpc_dot_tbrpc__pb2.DESCRIPTOR,tbmatch_dot_shop__pb2.DESCRIPTOR,tbmatch_dot_query__pb2.DESCRIPTOR,])




_ORDERCRITERIA = _descriptor.Descriptor(
  name='OrderCriteria',
  full_name='tbadmin.OrderCriteria',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='tbadmin.OrderCriteria.account_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_status', full_name='tbadmin.OrderCriteria.order_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modify_time', full_name='tbadmin.OrderCriteria.modify_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_total_amount', full_name='tbadmin.OrderCriteria.min_total_amount', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_total_amount', full_name='tbadmin.OrderCriteria.max_total_amount', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_account_balance', full_name='tbadmin.OrderCriteria.use_account_balance', index=5,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bill_last_name', full_name='tbadmin.OrderCriteria.bill_last_name', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bill_city', full_name='tbadmin.OrderCriteria.bill_city', index=7,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bill_region', full_name='tbadmin.OrderCriteria.bill_region', index=8,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bill_country', full_name='tbadmin.OrderCriteria.bill_country', index=9,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=473,
)


_SEARCHPURCHASEORDERSREQUEST = _descriptor.Descriptor(
  name='SearchPurchaseOrdersRequest',
  full_name='tbadmin.SearchPurchaseOrdersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='criteria', full_name='tbadmin.SearchPurchaseOrdersRequest.criteria', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort', full_name='tbadmin.SearchPurchaseOrdersRequest.sort', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='tbadmin.SearchPurchaseOrdersRequest.offset', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='tbadmin.SearchPurchaseOrdersRequest.limit', index=3,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=616,
)


_SEARCHPURCHASEORDERSRESULT = _descriptor.Descriptor(
  name='SearchPurchaseOrdersResult',
  full_name='tbadmin.SearchPurchaseOrdersResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orders', full_name='tbadmin.SearchPurchaseOrdersResult.orders', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_of_data', full_name='tbadmin.SearchPurchaseOrdersResult.end_of_data', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=618,
  serialized_end=707,
)


_SYNCPURCHASEORDERREQUEST = _descriptor.Descriptor(
  name='SyncPurchaseOrderRequest',
  full_name='tbadmin.SyncPurchaseOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_number', full_name='tbadmin.SyncPurchaseOrderRequest.order_number', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=709,
  serialized_end=757,
)


_VOIDPURCHASEORDERREQUEST = _descriptor.Descriptor(
  name='VoidPurchaseOrderRequest',
  full_name='tbadmin.VoidPurchaseOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_number', full_name='tbadmin.VoidPurchaseOrderRequest.order_number', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=759,
  serialized_end=807,
)


_REFUNDPURCHASEORDERREQUEST = _descriptor.Descriptor(
  name='RefundPurchaseOrderRequest',
  full_name='tbadmin.RefundPurchaseOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_number', full_name='tbadmin.RefundPurchaseOrderRequest.order_number', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=859,
)

_ORDERCRITERIA.fields_by_name['order_status'].enum_type = tbmatch_dot_shop__pb2._ORDERSTATUS
_ORDERCRITERIA.fields_by_name['modify_time'].message_type = tbmatch_dot_query__pb2._TIMERANGE
_ORDERCRITERIA.fields_by_name['min_total_amount'].message_type = tbrpc_dot_tbrpc__pb2._MONEY
_ORDERCRITERIA.fields_by_name['max_total_amount'].message_type = tbrpc_dot_tbrpc__pb2._MONEY
_ORDERCRITERIA.fields_by_name['bill_last_name'].message_type = tbmatch_dot_query__pb2._STRINGMATCH
_ORDERCRITERIA.fields_by_name['bill_city'].message_type = tbmatch_dot_query__pb2._STRINGMATCH
_ORDERCRITERIA.fields_by_name['bill_region'].message_type = tbmatch_dot_query__pb2._STRINGMATCH
_SEARCHPURCHASEORDERSREQUEST.fields_by_name['criteria'].message_type = _ORDERCRITERIA
_SEARCHPURCHASEORDERSREQUEST.fields_by_name['sort'].message_type = tbmatch_dot_shop__pb2._ORDERSORT
_SEARCHPURCHASEORDERSRESULT.fields_by_name['orders'].message_type = tbmatch_dot_shop__pb2._PURCHASEORDER
DESCRIPTOR.message_types_by_name['OrderCriteria'] = _ORDERCRITERIA
DESCRIPTOR.message_types_by_name['SearchPurchaseOrdersRequest'] = _SEARCHPURCHASEORDERSREQUEST
DESCRIPTOR.message_types_by_name['SearchPurchaseOrdersResult'] = _SEARCHPURCHASEORDERSRESULT
DESCRIPTOR.message_types_by_name['SyncPurchaseOrderRequest'] = _SYNCPURCHASEORDERREQUEST
DESCRIPTOR.message_types_by_name['VoidPurchaseOrderRequest'] = _VOIDPURCHASEORDERREQUEST
DESCRIPTOR.message_types_by_name['RefundPurchaseOrderRequest'] = _REFUNDPURCHASEORDERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderCriteria = _reflection.GeneratedProtocolMessageType('OrderCriteria', (_message.Message,), dict(
  DESCRIPTOR = _ORDERCRITERIA,
  __module__ = 'tbadmin.shop_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.OrderCriteria)
  ))
_sym_db.RegisterMessage(OrderCriteria)

SearchPurchaseOrdersRequest = _reflection.GeneratedProtocolMessageType('SearchPurchaseOrdersRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPURCHASEORDERSREQUEST,
  __module__ = 'tbadmin.shop_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.SearchPurchaseOrdersRequest)
  ))
_sym_db.RegisterMessage(SearchPurchaseOrdersRequest)

SearchPurchaseOrdersResult = _reflection.GeneratedProtocolMessageType('SearchPurchaseOrdersResult', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPURCHASEORDERSRESULT,
  __module__ = 'tbadmin.shop_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.SearchPurchaseOrdersResult)
  ))
_sym_db.RegisterMessage(SearchPurchaseOrdersResult)

SyncPurchaseOrderRequest = _reflection.GeneratedProtocolMessageType('SyncPurchaseOrderRequest', (_message.Message,), dict(
  DESCRIPTOR = _SYNCPURCHASEORDERREQUEST,
  __module__ = 'tbadmin.shop_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.SyncPurchaseOrderRequest)
  ))
_sym_db.RegisterMessage(SyncPurchaseOrderRequest)

VoidPurchaseOrderRequest = _reflection.GeneratedProtocolMessageType('VoidPurchaseOrderRequest', (_message.Message,), dict(
  DESCRIPTOR = _VOIDPURCHASEORDERREQUEST,
  __module__ = 'tbadmin.shop_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.VoidPurchaseOrderRequest)
  ))
_sym_db.RegisterMessage(VoidPurchaseOrderRequest)

RefundPurchaseOrderRequest = _reflection.GeneratedProtocolMessageType('RefundPurchaseOrderRequest', (_message.Message,), dict(
  DESCRIPTOR = _REFUNDPURCHASEORDERREQUEST,
  __module__ = 'tbadmin.shop_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.RefundPurchaseOrderRequest)
  ))
_sym_db.RegisterMessage(RefundPurchaseOrderRequest)



_SHOPADMINSERVICE = _descriptor.ServiceDescriptor(
  name='ShopAdminService',
  full_name='tbadmin.ShopAdminService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=862,
  serialized_end=1217,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchPurchaseOrders',
    full_name='tbadmin.ShopAdminService.SearchPurchaseOrders',
    index=0,
    containing_service=None,
    input_type=_SEARCHPURCHASEORDERSREQUEST,
    output_type=_SEARCHPURCHASEORDERSRESULT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\026')),
  ),
  _descriptor.MethodDescriptor(
    name='SyncPurchaseOrder',
    full_name='tbadmin.ShopAdminService.SyncPurchaseOrder',
    index=1,
    containing_service=None,
    input_type=_SYNCPURCHASEORDERREQUEST,
    output_type=tbrpc_dot_tbrpc__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\026')),
  ),
  _descriptor.MethodDescriptor(
    name='VoidPurchaseOrder',
    full_name='tbadmin.ShopAdminService.VoidPurchaseOrder',
    index=2,
    containing_service=None,
    input_type=_VOIDPURCHASEORDERREQUEST,
    output_type=tbrpc_dot_tbrpc__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\027')),
  ),
  _descriptor.MethodDescriptor(
    name='RefundPurchaseOrder',
    full_name='tbadmin.ShopAdminService.RefundPurchaseOrder',
    index=3,
    containing_service=None,
    input_type=_REFUNDPURCHASEORDERREQUEST,
    output_type=tbrpc_dot_tbrpc__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\027')),
  ),
])
_sym_db.RegisterServiceDescriptor(_SHOPADMINSERVICE)

DESCRIPTOR.services_by_name['ShopAdminService'] = _SHOPADMINSERVICE

# @@protoc_insertion_point(module_scope)
