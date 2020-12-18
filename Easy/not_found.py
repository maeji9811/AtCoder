import string
S = input()
a_z = string.ascii_lowercase

for i in a_z:
    if i not in S:
        print(i)
        break
else:
    print(None)