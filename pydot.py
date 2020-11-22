import numpy as np

"""
author: huciwen
language:python3
implement np.dot() function,using python and numpy .

"""

a = np.array([19,2,3,4])
b = np.array([11,5,6,7])

out = np.array([])
#a[0] * b[0]
#a[1] * b[1]
#a[2] * b[2]

for a_index,a_val in enumerate(a):
  for b_index,b_val in enumerate(b):
      if a_index == b_index:
        result  = a_val * b_val
        out  = np.append(out,result)

# out array return float type,we need to convert to int, so using astype(np.int64) 
print(np.sum(out.astype(np.int64)))
print(np.dot(a,b))


