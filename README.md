If you don't have `mnist.h5` in this directory, cd to this directory, and run the following commands:
  - `mkdir data`
  - download mnist.pkl.gz from deeplearning.net: `wget http://deeplearning.net/data/mnist/mnist.pkl.gz -O data/mnist.pkl.gz`
  - `python dataset.py`
  - this will build 3 files, `mnist_[train|val|test].h5`. Each has two datasets: 'inputs' and 'targets'.
