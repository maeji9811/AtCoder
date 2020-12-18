S = input()

for i, s in enumerate(S):
    for i_c, s_c in enumerate(S):
        if i != i_c:
            if s == s_c:
                print('no')
                break
    else:
        continue
    break
else:
    print('yes')
