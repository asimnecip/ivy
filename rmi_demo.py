import numpy as np
import inspect
import ivy

arr = np.array([[3,6,6],[4,5,1]])

print(arr)
ravel = np.ravel_multi_index(arr, (7,6))
print(ravel)

print(ivy.unravel_index(ravel, [7,6]))
