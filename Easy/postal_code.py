a, b = tuple(map(int, input().split()))
S = input()

if S[a] == '-':
    not_a_S = S[0:a] + S[a+1:len(S)+1]
    if '-' not in not_a_S:
        print('Yes')
    else:
        print('No')
else:
    print('No')