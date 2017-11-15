# Let's play football

## Requirements
A distribution of **Python** providing common data science packages like NumPy, SciPy, scikit-learn, and TensorFlow. Our recommendation is:
- [Intel® Distribution for Python](https://software.intel.com/en-us/distribution-for-python)

## Initial setup
```shell
conda create -n tf python=3.5 numpy scipy scikit-learn
source activate tf
pip install tensorflow
git clone git@github.com:jruizvar/jogos-data.git
cd jogos-data
```

## Your mission
The folder [data](https://github.com/jruizvar/jogos-data/tree/master/data) contains 100 files corresponding to 100 football matches of a tournament confronting two teams.

Each file contains two columns and 90 rows, and they represent the goals at every minute of the game. For instance, the [line 11 in game 1](https://github.com/jruizvar/jogos-data/blob/master/data/jogo1.txt#L11) indicates that the second team scores one goal at that minute.

Your mission is to find the final score of every match. Count the points obtained by the each team along the tournament, and determine who is the champion.

Your solution must be implemented in [TensorFlow](https://www.tensorflow.org/).
