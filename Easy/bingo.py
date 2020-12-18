import numpy as np

bingo = np.array([list(map(int, input().split(' '))) for _ in range(3)])
n = int(input())
b_list = [int(input()) for _ in range(n)]

for b in b_list:
    np.place(bingo, bingo == b, 0)

flip_bingo = np.fliplr(bingo)
dia_right_sum = np.diag(bingo).sum()
dia_left_sum = np.diag(flip_bingo).sum()
if dia_right_sum == 0 or dia_left_sum == 0:
    print('Yes')
else:
    array_sum_axis_0 = np.sum(bingo, 0)
    array_sum_axis_1 = np.sum(bingo, 1)
    if 0 in array_sum_axis_0 or 0 in array_sum_axis_1:
        print('Yes')
    else:
        print('No')



