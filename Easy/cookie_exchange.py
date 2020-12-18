import numpy as np

# a b c
# (b+c)/2       (a+c)/2       (a+b)/2
# (2a+b+c)/4    (a+2b+c)/4    (a+b+2c)/4
# (2a+3b+3c)/8  (3a+2b+3c)/8  (3a+3b+2c)/8
# (6a+5b+5c)/16 (5a+6b+5c)/16  (5a+5b+6c)/16
# (10a+11b+11c)/32 (11a+10b+11c)/32 (11a+11b+10c)/32


abc = list(map(int, input().split(' ')))
o = 0
while True:
    if abc[0] != 1 and abc[0] == abc[1] == abc[2]:
        print(-1)
        break
    for i in abc:
        if i % 2 != 0:
            print(o)
            break
    else:
        abc = [(abc[1]+abc[2])/2, (abc[0]+abc[2])/2, (abc[0]+abc[1])/2]
        o += 1
        continue
    break

