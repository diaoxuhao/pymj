import numpy as np
import pprint
import matplotlib.pyplot as plt
from scipy import linalg
a = np.array([[1,2,3],
              [4,5,6],
			  [7,8,9]])
print("type = ",a.dtype,
      "shape = ",a.shape,
	  "rank = ",a.itemsize)


b = np.arange(0,100,0.1)

c = np.fromfunction(lambda x,y:x+y,(5,5),dtype = np.float)
d = c[0,1:3]
d[1] = 111
print(c)#注意！这里和list不同，d和c共享内存

a = np.arange(0,10);
b = np.arange(5,15);
print(a)
print(np.transpose(a));
b = b.reshape(-1,1)
print(b*a)
print(a*b)
b = b.reshape(1,-1)
print(np.inner(a,b))
c = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(c)
print(c*np.array([1,1,1]).reshape(-1,1))
d = c.transpose();
pprint.pprint(d)
pprint.pprint(np.transpose(c)*np.array([1,1,1]).reshape(-1,1))

A = np.random.randn(100,100)
B = np.sum(A,axis=1)
pprint.pprint(B)
x = linalg.solve(A,B)
pprint.pprint(x)
