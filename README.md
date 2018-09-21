# python-sparsehistogram
A short python 3 function which computes the sparse (no empty bins) histogram of a 3D dataset (weights optional)

## Description
This script offers a function which quickly computes the histogram of a dataset stored as a python list, in sparse form. That is, no empty bins are represented; only bins with nonzero count or weight are stored. The function is written for 3D points with optional weights, but is trivially adapted to any dimension. 

It has been tested on 3D weighted and unweighted datasets. It is roughly as fast as using numpy's histogram function on a numpy array, but has the advantage that for fine resolutions and large datasets (order 10^6-10^7 points), it doesn't have horrible memory scaling. Numpy histograms will scale as the number of bins (which is the number of bins in each dimension to the power of the dimension, e.g. for 3D, n_bins^3), whereas sparsehist scales linearly with the size of the dataset in memory usage.
