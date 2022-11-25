# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/audio/audio_classifier/proto/audio_classifier_graph_options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.tasks.cc.components.processors.proto import classifier_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_classifier__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/audio/audio_classifier/proto/audio_classifier_graph_options.proto',
  package='mediapipe.tasks.audio.audio_classifier.proto',
  syntax='proto2',
  serialized_options=b'\n6com.google.mediapipe.tasks.audio.audioclassifier.protoB AudioClassifierGraphOptionsProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nTmediapipe/tasks/cc/audio/audio_classifier/proto/audio_classifier_graph_options.proto\x12,mediapipe.tasks.audio.audio_classifier.proto\x1a$mediapipe/framework/calculator.proto\x1aGmediapipe/tasks/cc/components/processors/proto/classifier_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xdb\x02\n\x1b\x41udioClassifierGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12Z\n\x12\x63lassifier_options\x18\x02 \x01(\x0b\x32>.mediapipe.tasks.components.processors.proto.ClassifierOptions\x12\'\n\x1f\x64\x65\x66\x61ult_input_audio_sample_rate\x18\x03 \x01(\x01\x32x\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8c\xfe\xb4\xd7\x01 \x01(\x0b\x32I.mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptionsBZ\n6com.google.mediapipe.tasks.audio.audioclassifier.protoB AudioClassifierGraphOptionsProto'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_classifier__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,])




_AUDIOCLASSIFIERGRAPHOPTIONS = _descriptor.Descriptor(
  name='AudioClassifierGraphOptions',
  full_name='mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classifier_options', full_name='mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptions.classifier_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_input_audio_sample_rate', full_name='mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptions.default_input_audio_sample_rate', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptions.ext', index=0,
      number=451755788, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=643,
)

_AUDIOCLASSIFIERGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
_AUDIOCLASSIFIERGRAPHOPTIONS.fields_by_name['classifier_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_classifier__options__pb2._CLASSIFIEROPTIONS
DESCRIPTOR.message_types_by_name['AudioClassifierGraphOptions'] = _AUDIOCLASSIFIERGRAPHOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AudioClassifierGraphOptions = _reflection.GeneratedProtocolMessageType('AudioClassifierGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCLASSIFIERGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.audio.audio_classifier.proto.audio_classifier_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptions)
  })
_sym_db.RegisterMessage(AudioClassifierGraphOptions)

_AUDIOCLASSIFIERGRAPHOPTIONS.extensions_by_name['ext'].message_type = _AUDIOCLASSIFIERGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_AUDIOCLASSIFIERGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)