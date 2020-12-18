n = int(input())
a_list = [int(input()) for _ in range(n)]
i_list = list(range(1, n + 1))

lighting_a = a_list[0]
lighting_i = i_list[0]
push = 0

while True:
    now_lighting_a = lighting_a
    now_lighting_i = lighting_i
    lighting_a = a_list[now_lighting_a - 1]
    lighting_i = i_list[now_lighting_a - 1]
    push += 1
    if lighting_a == now_lighting_i:
        print(-1)
        break
    elif lighting_i == 2:
        print(push)
        break

# n = int(input())
# a_list = []
# i_list = []
# for i in range(n):
#     i_list.append(i + 1)
#     a_list.append(int(input()))
#
# lighting_a = a_list[0]
# lighting_i = i_list[0]
#
# push = 0
#
# while True:
#     now_lighting_a = lighting_a
#     now_lighting_i = lighting_i
#     lighting_a = a_list[now_lighting_a - 1]
#     lighting_i = i_list[now_lighting_a - 1]
#     push += 1
#     if lighting_a == now_lighting_i:
#         print(-1)
#         break
#     elif lighting_i == 2:
#         print(push)
#         break

