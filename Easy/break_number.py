import numpy as np

n = int(input())

two_power = np.array(sorted([2 ** i for i in range(7)], reverse=True))
for i in sorted(range(n + 1), reverse=True):
    for t in two_power:
        if i == t:
            print(i)
            break
    else:
        continue
    break
