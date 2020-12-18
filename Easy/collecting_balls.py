n = int(input())
k = int(input())
X = list(map(int, input().split(' ')))

ball_xy = [[x, i + 1] for i, x in enumerate(X)]
type_a = [[0, i + 1] for i in range(n)]
type_b = [[k, i + 1] for i in range(n)]

min_dis = 0
for ball, a, b in zip(ball_xy, type_a, type_b):
    a_to_ball = abs(ball[0] - a[0]) * 2
    b_to_ball = abs(ball[0] - b[0]) * 2
    if a_to_ball >= b_to_ball:
        min_dis += b_to_ball
    elif a_to_ball < b_to_ball:
        min_dis += a_to_ball

print(min_dis)




# print(ball_xy)
# print(type_a)
# print(type_b)