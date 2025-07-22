import turtle
import math
import random

executed = False

ran = random.randint(0, 1)
move = random.randint(100, 200)


def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def utun(x1, x2, y1, y2):
    t.forward(350)
    if ran == 0:
        t.lt(90);
        t.forward(move);
        t.rt(90)
        t.forward(move)
        t.rt(90)
        t.forward(move)
        t.lt(90)
    if ran == 1:
        t.rt(90);
        t.forward(move);
        t.lt(90)
        t.forward(move)
        t.lt(90)
        t.forward(move)
        t.rt(90)

    return 0


def crash_sensor(x1, x2, y1, y2):
    if x1 >= x2 and y1 >= y2:
        print("crash")

        return 10


t = turtle.Turtle()
t.shape("turtle")
s = t.clone()
s.hideturtle()

test_t = t.clone()

# 초기 위치 설정
# t.speed(1)
t.rt(135)
t.penup()
t.goto(-300, -300)
t.pendown()

# 본격 경로 이동
t.rt(180)
t.penup()
t.goto(300, 300)
t.rt(180)
t.pendown()

# 장애물 선
s.pensize(5)
s.penup()
s.goto(50, -50)
obstacle_x1, obstacle_y1 = s.pos()
s.pendown()
s.goto(-50, 50)
obstacle_x2, obstacle_y2 = s.pos()

print(obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2)

# 거리 추적용 변수
x_prev, y_prev = t.pos()
total_distance = 0

while True:

    t.penup()
    t.forward(5)
    x_curr, y_curr = t.pos()

    # 누적 거리 계산
    step_dist = distance(x_prev, x_curr, y_prev, y_curr)
    total_distance += step_dist
    x_prev, y_prev = x_curr, y_curr

    print(x_curr, y_curr)
    if not executed:
        utun(10, x_curr, 10, y_curr)
        executed = True

    if x_curr <= -260 and y_curr <= -260:
        break
    t.pendown()

# 결과 출력
print(f"총 이동 거리: {total_distance:.2f}픽셀")
test_t.lt(45)
test_t.penup()
test_t.goto(-200, -200)
test_t.pendown()
while (1):
    test_t.penup()
    test_t.forward(5)
    x, y = test_t.pos()
    print(x, y)
    if crash_sensor(x, 0, y, 0) == 10:
        break
    test_t.pendown()

turtle.done()
