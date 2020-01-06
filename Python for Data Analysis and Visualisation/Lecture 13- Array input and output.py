"""Tools:
np.save('myArray', object you want to save)
np.savez('zipArray.npz',x=Array1,y=Array2) --> zip file
archiveArray = np.load('myArray.npy)
archiveArray['x'] calls x
np.savetxt('myTextArray.txt',delimeter=',')
np.loadtxt('myTextArray.txt',delimeter=',')
"""

import numpy as np

arr = np.arange(5)

np.save('myArray','arr')

np.load('myArray.npy')
np.savez(z)

archive_arr = np.load('ziparray.npz')
