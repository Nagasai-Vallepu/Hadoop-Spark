import numpy as np
arr=np.array([(12, 23, 34),(19, 43, 17)])
print(arr)			# Displays elements in nested list format
print(arr.ndim)		# Displays 2 D array
print(arr.size)		# Displays no. of elements
print(arr.shape)	# Displays shape of 2D array
print(arr.strides)	# Displays strides as 12, 4
print(arr.flags)	# Displays default properties of ndarray.
print(arr.dtype)	# Display default data type of array created thru NumPy

arr = arr.reshape(3, 2)	# It will reshape the array
print(arr)