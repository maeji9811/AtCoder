import numpy as np

n, k = tuple(map(int, input().split(' ')))

if (2 * n) < k:
    print(n)
elif n < k:
    print(abs(n - k))
else:
    t = n % k
    print(min(t, k-t))

