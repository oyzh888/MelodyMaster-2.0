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

# internal imports
import numpy as np
import six
import tensorflow as tf
import magenta
import os
from tensorflow.python.util import nest as tf_nest

mode='train'
sequence_example_file='/Users/liujiaheng/Desktop/Magenta/demo1/melody_rnn/sequence_examples/training_melodies.tfrecord'
sequence_example_file_paths = tf.gfile.Glob(
      os.path.expanduser(sequence_example_file))
inputs, labels, lengths = magenta.common.get_padded_batch(
sequence_example_file_paths, 120, 120,
shuffle=mode == 'train')
print(inputs)
print(labels)
print(labels)

