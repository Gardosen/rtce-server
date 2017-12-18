# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbadmin/report.proto

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
from tbmatch import match_pb2 as tbmatch_dot_match__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbadmin/report.proto',
  package='tbadmin',
  syntax='proto2',
  serialized_pb=_b('\n\x14tbadmin/report.proto\x12\x07tbadmin\x1a\x11tbrpc/tbrpc.proto\x1a\x13tbmatch/match.proto\"Y\n\x14\x43rashBuildIdentifier\x12\x18\n\x10\x62uild_identifier\x18\x01 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x02 \x01(\t\x12\x15\n\rbuild_version\x18\x03 \x01(\t\"\x87\x01\n\x0f\x43rashCollection\x12\x18\n\x10\x63rash_identifier\x18\x01 \x01(\t\x12\x18\n\x10\x62uild_identifier\x18\x02 \x01(\t\x12\x13\n\x0boccurrences\x18\x03 \x01(\x04\x12\x16\n\x0eusers_affected\x18\x04 \x01(\x04\x12\x13\n\x0bstack_trace\x18\x05 \x01(\t\"f\n\x0cSymbolHeader\x12\x13\n\x0bsymbol_path\x18\x01 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x02 \x01(\t\x12\x15\n\rbuild_version\x18\x03 \x01(\t\x12\x18\n\x10symbol_directory\x18\x04 \x01(\t\"\x8e\x01\n\x11\x43rashReportHeader\x12\x13\n\x0breport_path\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x10\n\x08\x61pp_name\x18\x03 \x01(\t\x12\x15\n\rbuild_version\x18\x04 \x01(\t\x12\x12\n\nmachine_id\x18\x05 \x01(\t\x12\x14\n\x0c\x63rash_number\x18\x06 \x01(\t\"8\n\x12ListDesyncsRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x12\n\x05limit\x18\x02 \x01(\x05:\x03\x32\x30\x30\"@\n\x11ListDesyncsResult\x12+\n\x06\x64\x65sync\x18\x01 \x03(\x0b\x32\x1b.tbmatch.DesyncReportHeader\"l\n\x12ListCrashesRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x12\n\x05limit\x18\x02 \x01(\x05:\x03\x32\x30\x30\x12\x18\n\x10\x62uild_identifier\x18\x03 \x01(\t\x12\x18\n\x10\x63rash_identifier\x18\x04 \x01(\t\"n\n\x11ListCrashesResult\x12,\n\ncollection\x18\x01 \x01(\x0b\x32\x18.tbadmin.CrashCollection\x12+\n\x07reports\x18\x02 \x03(\x0b\x32\x1a.tbadmin.CrashReportHeader\"F\n ListCrashBuildIdentifiersRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x12\n\x05limit\x18\x02 \x01(\x05:\x03\x32\x30\x30\"U\n\x1fListCrashBuildIdentifiersResult\x12\x32\n\x0bidentifiers\x18\x01 \x03(\x0b\x32\x1d.tbadmin.CrashBuildIdentifier\"[\n\x1bListCrashCollectionsRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x12\n\x05limit\x18\x02 \x01(\x05:\x03\x32\x30\x30\x12\x18\n\x10\x62uild_identifier\x18\x03 \x01(\t\"K\n\x1aListCrashCollectionsResult\x12-\n\x0b\x63ollections\x18\x01 \x03(\x0b\x32\x18.tbadmin.CrashCollection2\x90\x03\n\x11\x46\x61ilReportService\x12L\n\x0bListDesyncs\x12\x1b.tbadmin.ListDesyncsRequest\x1a\x1a.tbadmin.ListDesyncsResult\"\x04\xc8\xf3\x18\x12\x12L\n\x0bListCrashes\x12\x1b.tbadmin.ListCrashesRequest\x1a\x1a.tbadmin.ListCrashesResult\"\x04\xc8\xf3\x18\x12\x12v\n\x19ListCrashBuildIdentifiers\x12).tbadmin.ListCrashBuildIdentifiersRequest\x1a(.tbadmin.ListCrashBuildIdentifiersResult\"\x04\xc8\xf3\x18\x12\x12g\n\x14ListCrashCollections\x12$.tbadmin.ListCrashCollectionsRequest\x1a#.tbadmin.ListCrashCollectionsResult\"\x04\xc8\xf3\x18\x12')
  ,
  dependencies=[tbrpc_dot_tbrpc__pb2.DESCRIPTOR,tbmatch_dot_match__pb2.DESCRIPTOR,])




_CRASHBUILDIDENTIFIER = _descriptor.Descriptor(
  name='CrashBuildIdentifier',
  full_name='tbadmin.CrashBuildIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_identifier', full_name='tbadmin.CrashBuildIdentifier.build_identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='tbadmin.CrashBuildIdentifier.app_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_version', full_name='tbadmin.CrashBuildIdentifier.build_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=73,
  serialized_end=162,
)


_CRASHCOLLECTION = _descriptor.Descriptor(
  name='CrashCollection',
  full_name='tbadmin.CrashCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='crash_identifier', full_name='tbadmin.CrashCollection.crash_identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_identifier', full_name='tbadmin.CrashCollection.build_identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='occurrences', full_name='tbadmin.CrashCollection.occurrences', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='users_affected', full_name='tbadmin.CrashCollection.users_affected', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stack_trace', full_name='tbadmin.CrashCollection.stack_trace', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=165,
  serialized_end=300,
)


_SYMBOLHEADER = _descriptor.Descriptor(
  name='SymbolHeader',
  full_name='tbadmin.SymbolHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol_path', full_name='tbadmin.SymbolHeader.symbol_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='tbadmin.SymbolHeader.app_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_version', full_name='tbadmin.SymbolHeader.build_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol_directory', full_name='tbadmin.SymbolHeader.symbol_directory', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=302,
  serialized_end=404,
)


_CRASHREPORTHEADER = _descriptor.Descriptor(
  name='CrashReportHeader',
  full_name='tbadmin.CrashReportHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='report_path', full_name='tbadmin.CrashReportHeader.report_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='tbadmin.CrashReportHeader.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='tbadmin.CrashReportHeader.app_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_version', full_name='tbadmin.CrashReportHeader.build_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='machine_id', full_name='tbadmin.CrashReportHeader.machine_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crash_number', full_name='tbadmin.CrashReportHeader.crash_number', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=407,
  serialized_end=549,
)


_LISTDESYNCSREQUEST = _descriptor.Descriptor(
  name='ListDesyncsRequest',
  full_name='tbadmin.ListDesyncsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='tbadmin.ListDesyncsRequest.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='tbadmin.ListDesyncsRequest.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=200,
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
  serialized_start=551,
  serialized_end=607,
)


_LISTDESYNCSRESULT = _descriptor.Descriptor(
  name='ListDesyncsResult',
  full_name='tbadmin.ListDesyncsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='desync', full_name='tbadmin.ListDesyncsResult.desync', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=609,
  serialized_end=673,
)


_LISTCRASHESREQUEST = _descriptor.Descriptor(
  name='ListCrashesRequest',
  full_name='tbadmin.ListCrashesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='tbadmin.ListCrashesRequest.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='tbadmin.ListCrashesRequest.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=200,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_identifier', full_name='tbadmin.ListCrashesRequest.build_identifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crash_identifier', full_name='tbadmin.ListCrashesRequest.crash_identifier', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=675,
  serialized_end=783,
)


_LISTCRASHESRESULT = _descriptor.Descriptor(
  name='ListCrashesResult',
  full_name='tbadmin.ListCrashesResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection', full_name='tbadmin.ListCrashesResult.collection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reports', full_name='tbadmin.ListCrashesResult.reports', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=785,
  serialized_end=895,
)


_LISTCRASHBUILDIDENTIFIERSREQUEST = _descriptor.Descriptor(
  name='ListCrashBuildIdentifiersRequest',
  full_name='tbadmin.ListCrashBuildIdentifiersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='tbadmin.ListCrashBuildIdentifiersRequest.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='tbadmin.ListCrashBuildIdentifiersRequest.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=200,
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
  serialized_start=897,
  serialized_end=967,
)


_LISTCRASHBUILDIDENTIFIERSRESULT = _descriptor.Descriptor(
  name='ListCrashBuildIdentifiersResult',
  full_name='tbadmin.ListCrashBuildIdentifiersResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='tbadmin.ListCrashBuildIdentifiersResult.identifiers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=969,
  serialized_end=1054,
)


_LISTCRASHCOLLECTIONSREQUEST = _descriptor.Descriptor(
  name='ListCrashCollectionsRequest',
  full_name='tbadmin.ListCrashCollectionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='tbadmin.ListCrashCollectionsRequest.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='tbadmin.ListCrashCollectionsRequest.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=200,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_identifier', full_name='tbadmin.ListCrashCollectionsRequest.build_identifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1056,
  serialized_end=1147,
)


_LISTCRASHCOLLECTIONSRESULT = _descriptor.Descriptor(
  name='ListCrashCollectionsResult',
  full_name='tbadmin.ListCrashCollectionsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collections', full_name='tbadmin.ListCrashCollectionsResult.collections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1149,
  serialized_end=1224,
)

_LISTDESYNCSRESULT.fields_by_name['desync'].message_type = tbmatch_dot_match__pb2._DESYNCREPORTHEADER
_LISTCRASHESRESULT.fields_by_name['collection'].message_type = _CRASHCOLLECTION
_LISTCRASHESRESULT.fields_by_name['reports'].message_type = _CRASHREPORTHEADER
_LISTCRASHBUILDIDENTIFIERSRESULT.fields_by_name['identifiers'].message_type = _CRASHBUILDIDENTIFIER
_LISTCRASHCOLLECTIONSRESULT.fields_by_name['collections'].message_type = _CRASHCOLLECTION
DESCRIPTOR.message_types_by_name['CrashBuildIdentifier'] = _CRASHBUILDIDENTIFIER
DESCRIPTOR.message_types_by_name['CrashCollection'] = _CRASHCOLLECTION
DESCRIPTOR.message_types_by_name['SymbolHeader'] = _SYMBOLHEADER
DESCRIPTOR.message_types_by_name['CrashReportHeader'] = _CRASHREPORTHEADER
DESCRIPTOR.message_types_by_name['ListDesyncsRequest'] = _LISTDESYNCSREQUEST
DESCRIPTOR.message_types_by_name['ListDesyncsResult'] = _LISTDESYNCSRESULT
DESCRIPTOR.message_types_by_name['ListCrashesRequest'] = _LISTCRASHESREQUEST
DESCRIPTOR.message_types_by_name['ListCrashesResult'] = _LISTCRASHESRESULT
DESCRIPTOR.message_types_by_name['ListCrashBuildIdentifiersRequest'] = _LISTCRASHBUILDIDENTIFIERSREQUEST
DESCRIPTOR.message_types_by_name['ListCrashBuildIdentifiersResult'] = _LISTCRASHBUILDIDENTIFIERSRESULT
DESCRIPTOR.message_types_by_name['ListCrashCollectionsRequest'] = _LISTCRASHCOLLECTIONSREQUEST
DESCRIPTOR.message_types_by_name['ListCrashCollectionsResult'] = _LISTCRASHCOLLECTIONSRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CrashBuildIdentifier = _reflection.GeneratedProtocolMessageType('CrashBuildIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _CRASHBUILDIDENTIFIER,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.CrashBuildIdentifier)
  ))
_sym_db.RegisterMessage(CrashBuildIdentifier)

CrashCollection = _reflection.GeneratedProtocolMessageType('CrashCollection', (_message.Message,), dict(
  DESCRIPTOR = _CRASHCOLLECTION,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.CrashCollection)
  ))
_sym_db.RegisterMessage(CrashCollection)

SymbolHeader = _reflection.GeneratedProtocolMessageType('SymbolHeader', (_message.Message,), dict(
  DESCRIPTOR = _SYMBOLHEADER,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.SymbolHeader)
  ))
_sym_db.RegisterMessage(SymbolHeader)

CrashReportHeader = _reflection.GeneratedProtocolMessageType('CrashReportHeader', (_message.Message,), dict(
  DESCRIPTOR = _CRASHREPORTHEADER,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.CrashReportHeader)
  ))
_sym_db.RegisterMessage(CrashReportHeader)

ListDesyncsRequest = _reflection.GeneratedProtocolMessageType('ListDesyncsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTDESYNCSREQUEST,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.ListDesyncsRequest)
  ))
_sym_db.RegisterMessage(ListDesyncsRequest)

ListDesyncsResult = _reflection.GeneratedProtocolMessageType('ListDesyncsResult', (_message.Message,), dict(
  DESCRIPTOR = _LISTDESYNCSRESULT,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.ListDesyncsResult)
  ))
_sym_db.RegisterMessage(ListDesyncsResult)

ListCrashesRequest = _reflection.GeneratedProtocolMessageType('ListCrashesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCRASHESREQUEST,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.ListCrashesRequest)
  ))
_sym_db.RegisterMessage(ListCrashesRequest)

ListCrashesResult = _reflection.GeneratedProtocolMessageType('ListCrashesResult', (_message.Message,), dict(
  DESCRIPTOR = _LISTCRASHESRESULT,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.ListCrashesResult)
  ))
_sym_db.RegisterMessage(ListCrashesResult)

ListCrashBuildIdentifiersRequest = _reflection.GeneratedProtocolMessageType('ListCrashBuildIdentifiersRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCRASHBUILDIDENTIFIERSREQUEST,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.ListCrashBuildIdentifiersRequest)
  ))
_sym_db.RegisterMessage(ListCrashBuildIdentifiersRequest)

ListCrashBuildIdentifiersResult = _reflection.GeneratedProtocolMessageType('ListCrashBuildIdentifiersResult', (_message.Message,), dict(
  DESCRIPTOR = _LISTCRASHBUILDIDENTIFIERSRESULT,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.ListCrashBuildIdentifiersResult)
  ))
_sym_db.RegisterMessage(ListCrashBuildIdentifiersResult)

ListCrashCollectionsRequest = _reflection.GeneratedProtocolMessageType('ListCrashCollectionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCRASHCOLLECTIONSREQUEST,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.ListCrashCollectionsRequest)
  ))
_sym_db.RegisterMessage(ListCrashCollectionsRequest)

ListCrashCollectionsResult = _reflection.GeneratedProtocolMessageType('ListCrashCollectionsResult', (_message.Message,), dict(
  DESCRIPTOR = _LISTCRASHCOLLECTIONSRESULT,
  __module__ = 'tbadmin.report_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.ListCrashCollectionsResult)
  ))
_sym_db.RegisterMessage(ListCrashCollectionsResult)



_FAILREPORTSERVICE = _descriptor.ServiceDescriptor(
  name='FailReportService',
  full_name='tbadmin.FailReportService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1227,
  serialized_end=1627,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListDesyncs',
    full_name='tbadmin.FailReportService.ListDesyncs',
    index=0,
    containing_service=None,
    input_type=_LISTDESYNCSREQUEST,
    output_type=_LISTDESYNCSRESULT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\022')),
  ),
  _descriptor.MethodDescriptor(
    name='ListCrashes',
    full_name='tbadmin.FailReportService.ListCrashes',
    index=1,
    containing_service=None,
    input_type=_LISTCRASHESREQUEST,
    output_type=_LISTCRASHESRESULT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\022')),
  ),
  _descriptor.MethodDescriptor(
    name='ListCrashBuildIdentifiers',
    full_name='tbadmin.FailReportService.ListCrashBuildIdentifiers',
    index=2,
    containing_service=None,
    input_type=_LISTCRASHBUILDIDENTIFIERSREQUEST,
    output_type=_LISTCRASHBUILDIDENTIFIERSRESULT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\022')),
  ),
  _descriptor.MethodDescriptor(
    name='ListCrashCollections',
    full_name='tbadmin.FailReportService.ListCrashCollections',
    index=3,
    containing_service=None,
    input_type=_LISTCRASHCOLLECTIONSREQUEST,
    output_type=_LISTCRASHCOLLECTIONSRESULT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\022')),
  ),
])
_sym_db.RegisterServiceDescriptor(_FAILREPORTSERVICE)

DESCRIPTOR.services_by_name['FailReportService'] = _FAILREPORTSERVICE

# @@protoc_insertion_point(module_scope)
