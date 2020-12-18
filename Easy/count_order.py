import itertools

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

sort_p_q = list(itertools.permutations(sorted(p)))
p_i = 0
q_i = 0
for i, l in enumerate(sort_p_q):
    if l == tuple(p):
        p_i = i + 1
    elif l == tuple(q):
        q_i = i + 1

if p == q:
    print(0)
else:
    print(abs(p_i - q_i))
