import numpy as np
x= [[1,2,3], [4,5,6], [7,1,0]]
x=np.array(x)
print(x)
print(x.sum(axis=0))
print(x.sum(axis=1))