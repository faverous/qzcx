# coding: utf-8
import tensorflow as tf
import numpy as np
import time
import os
from data import batch_generator, out_excel
import random


class LSTM_PUE:
    def __init__(
            self, batch_size=64, seq_len=50, target_len=5, lstm_size=64,
            num_layers=2, learning_rate=0.001, sampling=False, train_keep_prob=0.5):

        if sampling is True:
            batch_size = 1

        self.batch_size = batch_size  # 每个bacth中的序列个数
        self.seq_len = seq_len  # 时间序列的长度
        self.target_len = target_len
        self.lstm_size = lstm_size  # 隐层lstm模块数量
        self.num_layers = num_layers  # 堆叠的lstm层数
        self.learning_rate = learning_rate
        self.train_keep_prob = train_keep_prob

        tf.reset_default_graph()

        self.inputs, self.targets, self.keep_prob = self.build_inputs(
            self.batch_size, self.seq_len, self.target_len)
        self.prediction = self.build_LSTM(
            self.inputs, self.batch_size, self.lstm_size, self.num_layers, self.keep_prob)
        self.optimizer = self.build_loss_and_optimizer(
            self.prediction, self.targets, self.learning_rate)

        self.saver = tf.train.Saver()

    def build_inputs(self, batch_size, seq_len, target_len):
        """
        构造输入层
        """
        with tf.name_scope('inputs'):
            inputs = tf.placeholder(tf.float32, shape=(
                batch_size, seq_len, 51), name='inputs')
            targets = tf.placeholder(tf.float32, shape=(
                batch_size, target_len, 1), name='targets')
            # 定义keep_prob参数用来控制dropout的保留节点数。
            keep_prob = tf.placeholder(tf.float32, name='keep_prob')

        return inputs, targets, keep_prob

    def build_LSTM(self, inputs, batch_size, lstm_size, num_layers, keep_prob):
        """
        构造LSTM层
        """
        def get_lstm_cell(lstm_size, keep_prob):
            lstm_cell = tf.contrib.rnn.LSTMCell(
                lstm_size, initializer=tf.random_uniform_initializer(-0.1, 0.1, seed=2))
            drop = tf.contrib.rnn.DropoutWrapper(
                lstm_cell, output_keep_prob=keep_prob)
            return drop

        with tf.name_scope('lstm'):
            cell = tf.nn.rnn_cell.MultiRNNCell(
                [get_lstm_cell(lstm_size, keep_prob) for _ in range(num_layers)])

            self.initial_state = cell.zero_state(batch_size, tf.float32)
            self.lstm_outputs, self.final_state = tf.nn.dynamic_rnn(
                cell, inputs, initial_state=self.initial_state)

            # 对于final_state的shape还有一些疑问
            #final_state = tf.concat(final_state, 0)
            # 注意，lstm的state有h和c两条组成的tuple。

            outputs = self.lstm_outputs[:, -1, :]

        with tf.variable_scope("prediction"):
            self.W_out = tf.Variable(tf.truncated_normal(
                [lstm_size, 1], stddev=0.1))
            self.b_out = tf.Variable(tf.constant(0.1, shape=[1, ]))
            prediction = tf.matmul(outputs, self.W_out) + self.b_out

        return prediction

    def build_loss_and_optimizer(self, prediction, targets, learning_rate):
        with tf.name_scope('loss'):
            self.loss = tf.reduce_mean(tf.square(tf.reshape(
                prediction, [-1]) - tf.reshape(targets, [-1])))

        with tf.name_scope('optimizer'):
            # 使用梯度下降算法训练
            optimizer = tf.train.GradientDescentOptimizer(
                learning_rate).minimize(self.loss)

        return optimizer

    def train(self, max_steps, save_path, save_every_n, log_every_n):
        self.session = tf.Session()
        with self.session as sess:
            sess.run(tf.global_variables_initializer())
            # Train network
            step = 0
            new_state = sess.run(self.initial_state)
            print(123)
            # for x, y in batch_generator:
            arrX = batch_generator(
                "sz_maxmin_a_train.xlsx", self.batch_size, self.seq_len)
            total_loss = []
            while True:
                step += 1
                n = random.randint(0, len(arrX) - self.batch_size)
                x = arrX[n:n + self.batch_size, :, :-1]
                y = arrX[n:n + self.batch_size, -1:, -1:]

                start = time.time()
                feed = {self.inputs: x,
                        self.targets: y,
                        self.keep_prob: self.train_keep_prob,
                        self.initial_state: new_state}
                batch_loss, new_state, _ = sess.run([self.loss,
                                                     self.final_state,
                                                     self.optimizer],
                                                    feed_dict=feed)

                end = time.time()
                # control the print lines
                if step % log_every_n == 0:
                    print('step: {}/{}... '.format(step, max_steps),
                          'loss: {:.4f}... '.format(batch_loss),
                          '{:.4f} sec/batch'.format((end - start)))
                    # 存一下loss
                    total_loss.append(batch_loss)
                if (step % save_every_n == 0):
                    self.saver.save(sess, os.path.join(
                        save_path, 'model'), global_step=step)
                if step >= max_steps:
                    break
            self.saver.save(sess, os.path.join(
                save_path, 'model'), global_step=step)

        out_excel(total_loss, "total_loss.xlsx")

    def test(self, checkpoint_path):
        self.session = tf.Session()
        with self.session as sess:
            # 参数初始化
            sess.run(tf.global_variables_initializer())
            # 加载模型
            self.saver.restore(sess, checkpoint_path)
            print('Restored from: {}'.format(checkpoint_path))
            # test
            new_state = sess.run(self.initial_state)
            #pre_output = np.zeros(shape=(self.lstm_size, 1), dtype=tf.float32)
            # for x, y in batch_generator:
            arrX = batch_generator(
                "sz_maxmin_a_test.xlsx", self.batch_size, self.seq_len)

            predictions = []
            for i in range(len(arrX)):
                # 逐条取测试数据
                x = arrX[i:i + self.batch_size, :, :-1]
                y = arrX[i:i + self.batch_size, -1:, -1:]
                # print(x)
                # print(y)
                feed = {self.inputs: x,
                        self.keep_prob: 1,
                        self.initial_state: new_state}
                preds, output, new_state = sess.run([self.prediction,
                                                     self.lstm_outputs,
                                                     self.final_state],
                                                    feed_dict=feed)

                print(y, preds)
                predictions.append(preds)

        out_excel(predictions, "predictions.xlsx")

    """
    def load(self, checkpoint):
        
        加载模型
        
        self.session = tf.Session()
        self.saver.restore(self.session, checkpoint)
        print('Restored from: {}'.format(checkpoint))
    """
