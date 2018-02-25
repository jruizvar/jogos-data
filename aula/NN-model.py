"""
    Create a model that learns to multiply by 7.

    The model in this example accomplishes the same 
    as the function:

    def multiply_by_seven(x):
        w = 7.
        y_pred = w * x
        return y_pred
"""
import numpy as np
import tensorflow as tf

n_neurons = 1
n_epochs = 1000
early_stop = 1.e-5
learning_rate = 0.1

x_train = np.array([[1.]])
y_train = np.array([[7.]])

x = tf.placeholder(tf.float32, [None, n_neurons])
y = tf.placeholder(tf.float32, [None, n_neurons])

y_pred = tf.layers.dense(x, n_neurons, use_bias=False)
loss = tf.losses.mean_squared_error(y, y_pred)

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    """ Training loop
    """
    for i in range(n_epochs):
        y_val, loss_val = sess.run([y_pred, loss],
                                   feed_dict={x: x_train, y: y_train})
        if i % 10 == 0:
            print("Epoch:", i)
            print("Loss value:", loss_val)
            print("Current predicted value:", y_val)
            print()
        if loss_val < early_stop:
            break

        train_op.run(feed_dict={x: x_train, y: y_train})

    """ Deploy trained model
    """
    x_test = np.array([[2.],
                       [3.],
                       [4.],
                       [5.],
                       [6.],
                       [7.],
                       [8.],
                       [9.]])

    y_test = y_pred.eval(feed_dict={x: x_test})
    print("Predictions on test set:")
    print(np.c_[x_test, y_test])
