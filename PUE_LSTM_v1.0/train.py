import tensorflow as tf
from data import batch_generator
from model import LSTM_PUE
import xlrd
import os


FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_string('name', 'default', 'name of the model')
tf.flags.DEFINE_integer('batch_size', 32, 'number of seqs in one batch')
tf.flags.DEFINE_integer('seq_len', 32, 'length of one seq')
tf.flags.DEFINE_integer('lstm_size', 64, 'size of hidden state of lstm')
tf.flags.DEFINE_integer('num_layers', 1, 'number of lstm layers')
tf.flags.DEFINE_float('learning_rate', 0.001, 'learning_rate')
tf.flags.DEFINE_float('train_keep_prob', 0.5, 'dropout rate during training')
tf.flags.DEFINE_integer('max_steps', 10000, 'max steps to train')
tf.flags.DEFINE_integer('save_every_n', 500, 'save the model every n steps')
tf.flags.DEFINE_integer('log_every_n', 50, 'log to the screen every n steps')


def main(_):
    model_path = os.path.join('model', FLAGS.name)
    if not os.path.exists(model_path):
        os.makedirs(model_path)

    # 这里想生成一个generato作为mini-batch生成器，但是还没有改好
    #g = batch_generator("ceshi.xlsx", FLAGS.batch_size, FLAGS.seq_len)

    model = LSTM_PUE(
        batch_size=FLAGS.batch_size,
        seq_len=FLAGS.seq_len,
        target_len=1,
        lstm_size=FLAGS.lstm_size,
        num_layers=FLAGS.num_layers,
        learning_rate=FLAGS.learning_rate,
        train_keep_prob=FLAGS.train_keep_prob)

    model.train(
        max_steps=FLAGS.max_steps,
        save_path=model_path,
        save_every_n=FLAGS.save_every_n,
        log_every_n=FLAGS.log_every_n)


if __name__ == '__main__':
    tf.app.run()
