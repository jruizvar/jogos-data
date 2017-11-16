"""
    Variables in tensorflow
"""
import tensorflow as tf

"""
    RANK 0
"""
a = tf.Variable(4, name='a')
b = tf.Variable(3, name='b')
c = tf.add(a, b, name='c')

print("Variables in TF\n")
print(a)
print(b)
print(c)
print()

with tf.Session() as sess:
    sess.run(a.initializer)
    sess.run(b.initializer)
    a_val = a.eval()
    b_val = b.eval()
    c_val = c.eval()
    print("The value of a:", a_val)
    print("The value of b:", b_val)
    print("The value of c:", c_val)
    print()
