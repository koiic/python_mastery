"""
  NumPy
First among these is NumPy. The main NumPy features are three-fold: its mathematical functions (e.g. sin, log, floor), its random submodule (useful for random sampling), and the NumPy ndarray object.

A NumPy array is similar to a mathematical n-dimensional matrix. For example,

x11x21⋮xd1x12x22⋮xd2x13x23⋮xd3……⋱…x1nx2n⋮xdn
[x11x12x13…x1nx21x22x23…x2n⋮⋮⋮⋱⋮xd1xd2xd3…xdn]
 
A NumPy array could be 1-dimensional (e.g. [1, 5, 20, 34, ...]), 2-dimensional (as above), or many dimensions. It's important to note that all the rows and columns of the 2-dimensional array are the same length. That will be true for all dimensions of arrays.
"""

import numpy as np

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists)

# create a numpy array
an_array = np.array(list_of_lists)
print(an_array)

non_rectangular = [[1, 2], [4, 5, 6], [7, 8, 9]]
print(non_rectangular)

non_rectangular_array = np.array(non_rectangular)
print(non_rectangular_array)

# check the shape and datatype
print(an_array.shape, an_array.dtype)
print(non_rectangular_array.shape, non_rectangular_array.dtype)

# The first case, an_array, is a 2-dimensional 3x3 array (of integers). In contrast, non_rectangular_array is a 1-dimensional length 3 array (of objects, namely list objects).

# numpy conveinience functions
linspace = np.linspace(1, 10, 10)
"""
    Return evenly spaced numbers over a specified interval.

    Returns `num` evenly spaced samples, calculated over the
    interval [`start`, `stop`].

    The endpoint of the interval can optionally be excluded.
"""
print(linspace)

n_range = np.arange(1, 10, 1.5)
print(n_range)

log_space = np.logspace(1, 10, 10)
print(log_space)

zeros = np.zeros(10)
print(zeros)

diagonal = np.diag([1, 2, 3, 4])
print(diagonal)

eye = np.eye(5)
print(eye)
