S = input()

dis_list = []
for i in range(len(S)-2):
    three_int = int(S[i] + S[i+1] + S[i+2])
    dis = abs(three_int - 753)
    dis_list.append(dis)

print(min(dis_list))