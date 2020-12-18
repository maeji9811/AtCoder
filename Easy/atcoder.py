S = input()

length = 0
length_list = [0]
for i, s in enumerate(S):
    if s == 'A' or s == 'C' or s == 'G' or s == 'T':
        length += 1
        if i == (len(S)-1):
            length_list.append(length)
    else:
        if length != 0:
            length_list.append(length)
        length = 0

print(max(length_list))


