# Class demonstrations

## [tensor.py](tensor.py)
- First steps in [TensorFlow](https://www.tensorflow.org/)
- Introduce tensors of type [tf.constant](https://www.tensorflow.org/api_docs/python/tf/constant)

## [session.py](session.py)
- Create a [tf.Session](https://www.tensorflow.org/api_docs/python/tf/Session)
- Evaluate tensors in a session with [eval](https://www.tensorflow.org/api_docs/python/tf/Tensor#eval)
- Multiply matrices with [tf.matmul](https://www.tensorflow.org/api_docs/python/tf/matmul)

## [variable.py](variable.py)
- Introduce tensors of type [tf.Variable](https://www.tensorflow.org/api_docs/python/tf/Variable)
- Initialize variables

## [placeholder.py](placeholder.py)
- Introduce tensors of type [tf.placeholder](https://www.tensorflow.org/api_docs/python/tf/placeholder)
- Example of the method [tf.reduce_sum](https://www.tensorflow.org/api_docs/python/tf/reduce_sum)

## [NN-model.py](NN-model.py)
- Create a neural network model that learns to multiply.
- Introduce high level methods:
  - [tf.layers.dense](https://www.tensorflow.org/api_docs/python/tf/layers/dense)
  - [tf.losses.mean_squared_error](https://www.tensorflow.org/api_docs/python/tf/losses/mean_squared_error)
  - [tf.train.AdamOptimizer](https://www.tensorflow.org/api_docs/python/tf/train/AdamOptimizer)
