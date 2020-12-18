n = int(input())
d = list(map(int, input().split(' ')))

d_sort = sorted(d)

half_point_small = d_sort[int((n/2)-1)]
half_point_big = d_sort[int(n/2)]
print(half_point_big - half_point_small)

