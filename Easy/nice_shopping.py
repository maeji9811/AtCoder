a, b, m = tuple(map(int, input().split()))
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))
m_array = [list(map(int, input().split())) for _ in range(m)]

no_coupon_min = min(a_array) + min(b_array)

coupon_min = min([a_array[m[0]-1] + b_array[m[1]-1] - m[2] for m in m_array])
print(min(coupon_min, no_coupon_min))
