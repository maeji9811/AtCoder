import numpy as np

n, m, c = tuple(input().split(' '))
n, m, c = int(n), int(m), int(c)
b_array = np.array(list(map(int, input().split(' '))))
a_array = np.array([list(map(int, input().split(' '))) for _ in range(n)])

a_b_array = a_array * b_array
sum_array = a_b_array.sum(1)
sum_c_array = sum_array + c
sign_array = np.sign(sum_c_array)
result = sign_array[sign_array > 0].sum()
print(result)



