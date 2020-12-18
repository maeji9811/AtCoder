n = int(input())
a_array = list(map(int, input().split(' ')))
numbers = range(1, n+1)

dict_a_number = {number: a for number, a in zip(numbers, a_array)}
sort_a_number = list(map(str, sorted(dict_a_number, key=dict_a_number.get)))

print(' '.join(sort_a_number))

