import numpy as np
#
n, m = tuple(map(int, input().split()))
input_list = [list(map(int, input().split())) for _ in range(m)]
input_array = np.array(input_list).reshape(-1, 2)

l_max = np.max(input_array[:, 0])
r_min = np.min(input_array[:, 1])

if l_max <= r_min:
    print(r_min - l_max + 1)
else:
    print(0)
