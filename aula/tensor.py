"""
    First steps in TensorFlow
"""
import tensorflow as tf

print()
print("Hello TensorFlow version: ", tf.__version__)
print()

"""
    RANK 0
"""
number = tf.constant(4, name='number')
animal = tf.constant("elephant", name='animal')
mathpi = tf.constant(3.1416, name='matphi')
print("Tensor of rank 0\n")
print(number)
print(animal)
print(mathpi)
print()

"""
    RANK 1
"""
weekend = tf.constant(['saturday', 'sunday'], name='weekend')
primes = tf.constant([2, 3, 5, 7], name='primes')
print("Tensor of rank 1\n")
print(weekend)
print(primes)
print()

"""
    RANK 2
"""
matrix = tf.constant([[1, 2, 3], [4, 5, 6]], name='matrix')
print("Tensor of rank 2\n")
print(matrix)
print()
