import numpy as np

h, w = tuple(list(map(int, input().split(' '))))

if h == 1 or w == 1:
    print(1)
else:
    w_first = int(np.ceil(w / 2))
    w_second = w - w_first
    if h % 2 == 0:
        h_first = int(h / 2)
    else:
        h_first = int(np.ceil(h / 2))

    h_second = h - h_first

    print(h_first * w_first + h_second * w_second)

