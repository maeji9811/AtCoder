import numpy as np
h = int(input())
x = int(np.floor(np.log(h) / np.log(2)))
y = sum([2**i for i in range(int(x))])
print(2**x + y)