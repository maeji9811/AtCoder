import math

n = int(input())

x_int = int(n / 1.08)
x_ceil = math.ceil(n / 1.08)

if n == int(x_int * 1.08):
    print(x_int)
elif n == int(x_ceil * 1.08):
    print(x_ceil)
else:
    print(':(')

