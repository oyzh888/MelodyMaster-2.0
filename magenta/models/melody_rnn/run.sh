BUNDLE_PATH=/Users/liujiaheng/Desktop/Magenta/magenta/magenta/models/melody_rnn/basic_rnn.mag 
CONFIG=basic_rnn

melody_rnn_generate \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--primer_midi=/Users/liujiaheng/Desktop/Magenta/magenta/magenta/models/melody_rnn/primer.mid

melody_rnn_create_dataset \
--config=basic_rnn \
--input=/Users/liujiaheng/Desktop/Magenta/out1.tfrecord \
--output_dir=/Users/liujiaheng/Desktop/Magenta/melody_rnn/sequence_examples1 \
--eval_ratio=0.10
/Users/liujiaheng/Desktop/Magenta
melody_rnn_train \
--config=basic_rnn \
--run_dir=/Users/liujiaheng/Desktop/Magenta/melody_rnn/logdir/run1 \
--sequence_example_file=/Users/liujiaheng/Desktop/Magenta/melody_rnn/sequence_examples/training_melodies.tfrecord \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--num_training_steps=200

melody_rnn_generate \
--config=basic_rnn \
--run_dir=/Users/liujiaheng/Desktop/Magenta/melody_rnn/logdir/run1 \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--primer_midi=/Users/liujiaheng/Desktop/Magenta/magenta/magenta/models/melody_rnn/primer.mid 