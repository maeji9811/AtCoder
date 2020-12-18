n, a, b = tuple(input().split(' '))
S = input()
n, a, b = int(n), int(a), int(b)

pass_preliminary = 0
b_rank = 0

for s in S:
    if s == 'c':
        print('No')
    elif s == 'a':
        if pass_preliminary < a + b:
            print('Yes')
            pass_preliminary += 1
        else:
            print('No')
    elif s == 'b':
        b_rank += 1
        if pass_preliminary < a + b and b_rank <= b:
            print('Yes')
            pass_preliminary += 1
        else:
            print('No')

