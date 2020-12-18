n = int(input())
S = input()
x = 0
x_list = [0]
for s in S:
    if s == 'I':
        x += 1
        x_list.append(x)
    elif s == 'D':
        x -= 1
        x_list.append((x))
print(max(x_list))