"""
    Sessions in Tensorflow
"""
import tensorflow as tf

a = tf.constant([[2, 1], [-1, 0]], name='a')
b = tf.constant([[1, 0], [0, 1]], name='b')
c = tf.add(a, b, name='c')
# d = tf.multiply(a, b, name='d')
d = tf.matmul(a, b, name='d')
print(a)

with tf.Session() as sess:
    a_val = a.eval()
    b_val = b.eval()
    c_val = c.eval()
    d_val = d.eval()
    print("\nThe value of a:\n", a_val)
    print("\nThe value of b:\n", b_val)
    print("\nThe value of c:\n", c_val)
    print("\nThe value of d:\n", d_val)
    print()
