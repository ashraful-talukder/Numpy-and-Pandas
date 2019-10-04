import numpy as np

np.arange(10)

np.arange(2,10)

np.arange(2,10,3)

arr=np.arange(10)

arr.ndim  #shows the dimension

arr.shape  #shows the array's shape

arr.size  #shows the arry size

arr.dtype  #shows the array's data type

arr.itemsize   #shows the array's each item's size

arr.itemsize*arr.size

ar1=([1,2,3],[4,3,5])
nar=np.asarray(ar1)

np.linspace(1,4,num=4) # it provides 4 numbers from 1 to 4 with same distance
np.linspace(1,4,num=8) # it provides 8 numbers from 1 to 4 with same distance
np.linspace(1,4,num=8,endpoint=False) # it provides 4 numbers from 1 to 4 with same distance excluding endpoint

q=np.zeros((3,4),dtype='int32')  #it provides a zero matrics

np.random.random((3,4))  #it generates a given dimension's matrix which values ar random between 0 and 1

var=np.random.random((4,5))

np.max(var,axis=0) #all the maximum values in each column
np.max(var,axis=1) #all the maximum values in each row
np.max(var) #maximum value from the whole matrix

np.min(var,axis=0) #all the minimum values in each column
np.min(var,axis=1) #all the minimum values in each row
np.min(var) #minimum value from the whole matrix

np.median(var,axis=0) #all the median values in each column
np.median(var,axis=1) #all the median values in each row
np.median(var) #median from the whole matrix

new=np.reshape(var,(20,))
new=np.reshape(var,(20,1))

#Slicing

a=np.random.random((4,5))
a[:,:] #all the values
a[1:3,:] #all the columns but only 2nd and 3rd rows
a[:,1:3] #all the rows but only 2nd and 3rd columns

a[:,[1,3]] #you can also write like this