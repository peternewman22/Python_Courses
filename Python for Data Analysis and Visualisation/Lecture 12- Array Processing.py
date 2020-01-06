"""Tools:
np.meshgrid(points,points)
zip --> process the things
Boolean Logic
np.where(condition,A,B)
.any()
.all()
.sum()
.std()
.mean()
.sort()
.var()
.unique()
.in1d()
"""

import numpy as np
# to be able to visualize a bit better
import matplotlib.pyplot as plt


# setting the points along one side of the grid
points = np.arange(-5,5,0.01)

#create the grid
dx,dy = np.meshgrid(points,points)

#evaluative function using sine, which is one of the universal functions
z = (np.sin(dx))+(np.sin(dy))

#plot the image
plt.imshow(z)

#plot with the colour bar
plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x)+sin(y)')


# numpy where

A = np.array([1,2,3,4])

B = np.array([100,200,300,400])

# creating a boolean array
condition = np.array([True,True,False,False])

# go through the two diffferen arrays and select the relevant answer
answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]
#print(answer)

answer2 = np.where(condition,A,B)
#print(answer2)

# Now we extend the where command
from numpy.random import randn
arr = randn(5,5)
#print(arr)

#print(np.where(arr<0,0,arr))

# more statistical processing
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(arr.sum())
print(arr.std())
print(arr.var())
print(arr.mean())


# bool array
bool_arr = np.array([True,False,True])
print(bool_arr.any())
print(bool_arr.all())

countries = np.array(["France","Germany","USA","Russia","USA","Mexico","Germany"])
print(np.unique(countries))

#check the presence in a list
print(np.in1d(["France","USA","Sweden"],countries))

