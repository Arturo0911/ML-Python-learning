#!/usr/bin/python3


"""
@author Arturo Negreiros

"""
import numpy as np

a1 = np.array([1, 2, 3]) # normal array
a2 = np.arange(10) #  array to range to 10
a3 = np.zeros((99,99)) # array with zeros and 2 rows and 3 columns
a4 = np.ones((2,3))
a5 = np.linspace(0,1,10)


# prints
print(a1)
print(a2)
print(a3)
print(a4)
print(type(a4))
print(a5)
