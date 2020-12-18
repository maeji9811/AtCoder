from itertools import combinations

n, x = tuple(map(int, input().split()))
a_array = list(map(int, input().split()))


if sum(a_array) == x:
    print(n)
elif sum(a_array) < x:
    print(n-1)
elif all([True if i > x else False for i in a_array]) is True:
    print(0)
else:
    a_array = sorted(a_array, reverse=True)
    for i in range(n):
        sum_a = sum(a_array[i+1:])
        if sum_a <= x:
            print(len(a_array[i+1:]))
            break




    # for i in reversed(range(1, n)):
    #     iter_array = list(combinations(a_array, i))
    #     for s in iter_array:
    #         if sum(s) <= x:
    #             print(i)
    #             break
    #     else:
    #         continue
    #     break

