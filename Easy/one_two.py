import numpy as np

x = int(''.join(input().split(' ')))

r = np.sqrt(x)
i, f = tuple(map(int, str(r).split('.')))
if f == 0:
    print('Yes')
else:
    print('No')

