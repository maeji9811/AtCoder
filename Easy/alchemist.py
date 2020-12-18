import numpy as np

n = int(input())
v_array = np.array(sorted(list(map(int, input().split(' '))), reverse=True))
two_exp_array = np.array(sorted([2 ** i for i in range(n-1)], reverse=True))
two_exp_array = np.concatenate([two_exp_array, np.array([1])], axis=0)

cal_array = v_array * two_exp_array
result = np.sum(cal_array / (2 ** (n - 1)))
print(result)

