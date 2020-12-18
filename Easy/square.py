x_1, y_1, x_2, y_2 = tuple(map(int, input().split()))

x_dis = x_2 - x_1
y_dis = y_2 - y_1

x_3 = x_2 - y_dis
y_3 = y_2 + x_dis
x_4 = x_1 - y_dis
y_4 = y_1 + x_dis

print(x_3, y_3, x_4, y_4)