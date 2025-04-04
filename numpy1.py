#np.zeros((2,2))- creates an array of size 2,2 with zeros
#variable.shape- prints the size of the array
#np.arange(15)- creates an array from 0 to the specified limit
#np.linspace(#,#,#)-creates an array of evenly spaced values over a specified interval
#np.empty((#,#))-creates an array of random values of the size #,#
#np.empty_like(linspace)- creates an array of random values from the linespace command
#np.identity(#)- creates a 2d array of an identity matrix of #
#variable.reshape(#,#)- returns a new array with the specified shape, reshaping the original array without changing its data
#variable.ravel()- convert a multi-dimensional array into a one-dimensional array
#np.array(variable)- changes the array to matrix format
#variable.T- prints the transpose of the array
#variable.ndim- prints the number of axis
#variable.size- prints the total number of elements
#variable.argmax or variable.argmin prints the max or min of the array
#variable.argsort()- sorts the array
#np.where(arguement)- finds the number in the array depending on the arguement passed
#

import numpy as np
myarr=np.array([[3,6,32,7]],np.int64)
print(myarr[0,1])
zeros=np.zeros((1,2))
print(zeros)
print(np.arange(25))
print(np.linspace(1,5,5))