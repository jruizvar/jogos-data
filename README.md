# Let's play football

## Requirements
**Python** distribution providing common data science packages like NumPy, SciPy, scikit-learn, and TensorFlow. 

We strongly recommend:
- [Intel® Distribution for Python](https://software.intel.com/en-us/distribution-for-python)

## Initial setup
```shell
# Create environment
conda create -n tf python=3.5 numpy scipy scikit-learn
source activate tf

# Install tensorflow
pip install tensorflow

# Clone this repository
git clone git@github.com:jruizvar/jogos-data.git
cd jogos-data
```

## Your mission
The directory [data](https://github.com/jruizvar/jogos-data/tree/master/data) contains 99 files corresponding to 99 football matches in a tournament confronting two teams.

Each file consists of two columns and 90 rows, and they represent the goals scored in each minute of the game. For instance, the [line 11 in game 1](https://github.com/jruizvar/jogos-data/blob/master/data/jogo1.txt#L11) indicates that the second team scores one goal in that minute.

Your mission is to find the final score for every match. Count the points obtained by each team along the tournament, and determine who is the champion.

Try to implement your solution in [TensorFlow](https://www.tensorflow.org/).
