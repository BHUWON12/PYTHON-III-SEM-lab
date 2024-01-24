'''12. using a numpy module create an array
 and check the following: 
1. Type of array 2. Axes of array 
3. Shape of array 4. Type of elements in array.'''
import numpy as np 
narray =np.array([[1,2,3],["a","b","c"]])
print("type of array: {type(narray)}")
print("dimention of array: ",narray.ndim)
print("shape of array:",narray.shape)
print("data of an array:",narray.dtype.type)