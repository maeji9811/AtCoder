import numpy as np

k, n = tuple(map(int, input().split(' ')))
a_array = np.array(list(map(int, input().split(' '))))
first_array = a_array
last_array = np.append(first_array[:-1] + k, first_array[-1])
last_array = np.sort(last_array)
distance = last_array - first_array
print(int(np.min(distance)))
