"""
    Placeholder in tensorflow
"""
import numpy as np
import tensorflow as tf

"""
    RANK 2
"""
a = tf.placeholder(tf.int32, shape=(90, 2), name='a')

placar = tf.reduce_sum(a, axis=0, name='placar')

print("\nPlaceholders in TensorFlow\n")
print(a)
print()

with tf.Session() as sess:
    data = np.loadtxt('data/jogo1.txt')
    a_val = a.eval(feed_dict={a: data})
    placar_val = placar.eval(feed_dict={a: data})
    print("The value of a:\n", a_val)
    print("\nThe value of placar:\n", placar_val)
    print()
