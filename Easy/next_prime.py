import numpy as np

x = int(input())


while True:
    if x == 2:
        print(x)
        break
    else:
        n_array = np.arange(2, x)
        n_array = x % n_array
        if 0 not in n_array:
            print(x)
            break
        else:
            x += 1
