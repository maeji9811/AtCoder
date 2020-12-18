
n, m, x = tuple(map(int, input().split()))
a_array = list(map(int, input().split()))

to_n = len([i for i in a_array if i > x])
to_zero = len([i for i in a_array if i < x])

print(min(to_n, to_zero))
