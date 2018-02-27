# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Provides function to build an event sequence RNN model's graph."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from magenta.models.melody_rnn import melody_rnn_config_flags

from magenta.music.note_sequence_io import note_sequence_record_iterator
# internal imports
import numpy as np
import os
import tensorflow as tf
import magenta

from tensorflow.python.util import nest as tf_nest





def get_build_graph_fn(mode, config, sequence_example_file_paths=None):
  """Returns a function that builds the TensorFlow graph.

  Args:
    mode: 'train', 'eval', or 'generate'. Only mode related ops are added to
        the graph.
    config: An EventSequenceRnnConfig containing the encoder/decoder and HParams
        to use.
    sequence_example_file_paths: A list of paths to TFRecord files containing
        tf.train.SequenceExample protos. Only needed for training and
        evaluation.

  Returns:
    A function that builds the TF ops when called.

  Raises:
    ValueError: If mode is not 'train', 'eval', or 'generate'.
  """

  hparams = config.hparams
  encoder_decoder = config.encoder_decoder

  tf.logging.info('hparams = %s', hparams.values())

  input_size = encoder_decoder.input_size
  num_classes = encoder_decoder.num_classes
  no_event_label = encoder_decoder.default_event_label
  """Builds the Tensorflow graph."""
  inputs, labels, lengths = None, None, None

  if mode == 'train' or mode == 'eval':
    inputs, labels, lengths = magenta.common.get_padded_batch(
        sequence_example_file_paths, hparams.batch_size, input_size,
          shuffle=mode == 'train')
    with tf.Session() as sess:
        init_op=tf.global_variables_initializer()
        sess.run(init_op)
        coord=tf.train.Coordinator()
        threads=tf.train.start_queue_runners(coord=coord)
        try:
            #while not coord.should_stop():
            for i in range(2):
                e1,e2,e3=sess.run([inputs,labels,lengths])
                print(e1)
                print('hello\n')
                print(e2)
                print('hello1\n')
                print(e3)
                print('hello3\n')
        except tf.errors.OutOfRangeError:
            print('Done nothing')
        finally:
            coord.request_stop()
        coord.request_stop()
        coord.join(threads)
if __name__ == '__main__':
  sequence_example_file = (
      '/Users/liujiaheng/Desktop/Magenta/demo1/melody_rnn/sequence_examples/training_melodies.tfrecord')
  sequence_example_file_paths = tf.gfile.Glob(
      os.path.expanduser(sequence_example_file))
  config = melody_rnn_config_flags.config_from_flags()
  get_build_graph_fn('train',config,sequence_example_file_paths)