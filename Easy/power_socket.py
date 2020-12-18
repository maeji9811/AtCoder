ans_1 = []
ans_2 = []

def power_socket(a, b):
    if b == 1:
        ans_1.append(0)
    elif a > b:
        ans_1.append(1)
    else:
        a_sub_1 = a - 1
        b_sub = b - a
        amount = 1
        while b_sub > 0:
            b_sub -= a_sub_1
            amount += 1
        ans_1.append(amount)

for a in range(2, 21):
    for b in range(2, 21):
        power_socket(a, b)


def socket_2(a, b):
    outlet = 1
    ans = 0
    while b > outlet:
        outlet -= 1
        outlet += a
        ans += 1
    ans_2.append(ans)


for a in range(2, 21):
    for b in range(2, 21):
        socket_2(a, b)

for x, y in zip(ans_1, ans_2):
    print(x == y)


# 提出用
a, b = tuple(input().split(' '))
a, b = int(a), int(b)

if b == 1:
    print(0)
elif a > b:
    print(1)
else:
    a_next = a - 1
    b_sub = b - a
    amount = 1
    while b_sub > 0:
        b_sub -= a_next
        amount += 1
    print(amount)

# 提出２
a, b = tuple(input().split(' '))
a, b = int(a), int(b)

outlet = 1
ans = 0
while b > outlet:
    outlet -= 1
    outlet += a
    ans += 1
print(ans)