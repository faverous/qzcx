import tensorflow as tf
from data import batch_generator
from model import LSTM_PUE
import xlrd
import os


FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_string('name', 'default', 'name of the model')
tf.flags.DEFINE_integer('seq_len', 32, 'length of one seq')
tf.flags.DEFINE_integer('lstm_size', 64, 'size of hidden state of lstm')
tf.flags.DEFINE_integer('num_layers', 1, 'number of lstm layers')
tf.flags.DEFINE_string('checkpoint_path', 'model/default/', 'checkpoint path')


def main(_):
    # 如果路径正确，则获取最后一次保存的模型。
    if os.path.isdir(FLAGS.checkpoint_path):
        FLAGS.checkpoint_path = tf.train.latest_checkpoint(
            FLAGS.checkpoint_path)

    model = LSTM_PUE(
        sampling=True,
        seq_len=FLAGS.seq_len,
        target_len=1,
        lstm_size=FLAGS.lstm_size,
        num_layers=FLAGS.num_layers)

    model.test(FLAGS.checkpoint_path)


if __name__ == '__main__':
    tf.app.run()
