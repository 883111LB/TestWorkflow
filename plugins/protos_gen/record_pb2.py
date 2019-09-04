# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='record.proto',
  package='stock_testing',
  syntax='proto3',
  serialized_options=_b('\n\026com.chi.ssetest.protosB\nTestRecord'),
  serialized_pb=_b('\n\x0crecord.proto\x12\rstock_testing\"\xcb\x01\n\x13TestExecutionRecord\x12\r\n\x05jobID\x18\x01 \x01(\t\x12\x10\n\x08runnerID\x18\x02 \x01(\t\x12\x12\n\ntestcaseID\x18\x03 \x01(\t\x12\x10\n\x08recordID\x18\x04 \x01(\t\x12\x0e\n\x06isPass\x18\x05 \x01(\x08\x12\x11\n\tstartTime\x18\x06 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x07 \x01(\x03\x12\x10\n\x08paramStr\x18\x08 \x01(\t\x12\x11\n\tresultStr\x18\t \x01(\t\x12\x14\n\x0c\x65xceptionStr\x18\n \x01(\t\"q\n\x15RunnerExecutionRecord\x12\r\n\x05jobID\x18\x01 \x01(\t\x12\x10\n\x08runnerID\x18\x02 \x01(\t\x12\x10\n\x08runCount\x18\x03 \x01(\x05\x12\x14\n\x0c\x66\x61ilureCount\x18\x04 \x01(\x05\x12\x0f\n\x07runTime\x18\x05 \x01(\x03\x42$\n\x16\x63om.chi.ssetest.protosB\nTestRecordb\x06proto3')
)




_TESTEXECUTIONRECORD = _descriptor.Descriptor(
  name='TestExecutionRecord',
  full_name='stock_testing.TestExecutionRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobID', full_name='stock_testing.TestExecutionRecord.jobID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runnerID', full_name='stock_testing.TestExecutionRecord.runnerID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='testcaseID', full_name='stock_testing.TestExecutionRecord.testcaseID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recordID', full_name='stock_testing.TestExecutionRecord.recordID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isPass', full_name='stock_testing.TestExecutionRecord.isPass', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='stock_testing.TestExecutionRecord.startTime', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='stock_testing.TestExecutionRecord.endTime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramStr', full_name='stock_testing.TestExecutionRecord.paramStr', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultStr', full_name='stock_testing.TestExecutionRecord.resultStr', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exceptionStr', full_name='stock_testing.TestExecutionRecord.exceptionStr', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=235,
)


_RUNNEREXECUTIONRECORD = _descriptor.Descriptor(
  name='RunnerExecutionRecord',
  full_name='stock_testing.RunnerExecutionRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobID', full_name='stock_testing.RunnerExecutionRecord.jobID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runnerID', full_name='stock_testing.RunnerExecutionRecord.runnerID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runCount', full_name='stock_testing.RunnerExecutionRecord.runCount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failureCount', full_name='stock_testing.RunnerExecutionRecord.failureCount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runTime', full_name='stock_testing.RunnerExecutionRecord.runTime', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=237,
  serialized_end=350,
)

DESCRIPTOR.message_types_by_name['TestExecutionRecord'] = _TESTEXECUTIONRECORD
DESCRIPTOR.message_types_by_name['RunnerExecutionRecord'] = _RUNNEREXECUTIONRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestExecutionRecord = _reflection.GeneratedProtocolMessageType('TestExecutionRecord', (_message.Message,), dict(
  DESCRIPTOR = _TESTEXECUTIONRECORD,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:stock_testing.TestExecutionRecord)
  ))
_sym_db.RegisterMessage(TestExecutionRecord)

RunnerExecutionRecord = _reflection.GeneratedProtocolMessageType('RunnerExecutionRecord', (_message.Message,), dict(
  DESCRIPTOR = _RUNNEREXECUTIONRECORD,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:stock_testing.RunnerExecutionRecord)
  ))
_sym_db.RegisterMessage(RunnerExecutionRecord)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)