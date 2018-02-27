BUNDLE_PATH=/Users/liujiaheng/Desktop/Magenta/magenta/drum_kit_rnn.mag
CONFIG=drum_kit

drums_rnn_generate \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=/Users/liujiaheng/Desktop/Magenta/drums_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
#--primer_drums="[(36,)]"
--primer_midi=/Users/liujiaheng/Desktop/Magenta/magenta/magenta/models/melody_rnn/primer.mid
