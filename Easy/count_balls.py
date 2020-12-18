n, a, b = tuple(map(int, input().split()))
a_b_sum = a + b
x = n // a_b_sum
i = n % a_b_sum

if i <= a:
    print(x * a + i)
else:
    print(x * a + a)