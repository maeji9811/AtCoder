s = int(input())

f_array = [s]
counter = 1
while True:
    counter += 1
    if f_array[counter-2] % 2 != 0:
        f = f_array[counter-2] * 3 + 1
        if f in f_array:
            print(counter)
            break
        else:
            f_array.append(f)
    else:
        f = f_array[counter-2] / 2
        if f in f_array:
            print(counter)
            break
        else:
            f_array.append(f)
