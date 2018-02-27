INPUT_DIRECTORY=/Users/liujiaheng/Desktop/Magenta/dataset_midi 
# TFRecord file that will contain NoteSequence protocol buffers.
SEQUENCES_TFRECORD=/Users/liujiaheng/Desktop/Magenta/notesequences.tfrecord

convert_dir_to_note_sequences \
  --input_dir=$INPUT_DIRECTORY \
  --output_file=$SEQUENCES_TFRECORD \
  --recursive
