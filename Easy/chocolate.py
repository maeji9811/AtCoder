import numpy as np

n = int(input())
d, x = tuple(map(int, input().split()))
a_array = [int(input()) for _ in range(n)]

result_array = [np.floor((d - 1)/a) + 1 for a in a_array]
print(int(sum(result_array)) + x)