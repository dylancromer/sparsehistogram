# python_groupby
Testing ground for Python 3 code attempting to perform a certain groupby-esque operation on lists of coordinates and weights

## Description

`groupbybin` is a function which, provided with an ordered list of coordinates {(x,y,z,w)}, with w a weight, bins the data according to x,y,z position and adds the weights w belonging to the same bin. Thus, `groupbybin` is a map from {(x,y,z,w)} to a function mapping {(xbin,ybin,zbin}) -> {w}. 

The implementation is styled so that the function is ready to accept Python 3 lists of the form [[x1,y1,z1,w1],...]. However, with little modification this function is adaptable to other inputs.
