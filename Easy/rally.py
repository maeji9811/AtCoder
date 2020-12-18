n = int(input())
x_input = input().split(' ')
x = list(map(int, x_input))
x.sort()
x_range = range(x[0], x[-1] + 1)

sum_list = []
for p in x_range:
    power = 0
    for i, x_i in enumerate(x):
        amount = (x_i - p) ** 2
        power += amount
        if i == len(x) - 1:
            sum_list.append(power)

print(min(sum_list))
