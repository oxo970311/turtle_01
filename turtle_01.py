import turtle
import math


def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


t = turtle.Turtle()
t.shape("turtle")
s = t.clone()
s.hideturtle()

# 초기 위치 설정
t.speed(1)
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
s.pendown()
s.goto(-50, 50)

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

    # 장애물 감지
    if -50 <= x_curr <= 50 and -50 <= y_curr <= 50:
        t.rt(90)
        t.forward(100)
        t.lt(90)
        t.forward(100)
        t.lt(90)
        t.forward(100)
        t.right(90)
        t.forward(350)
        break

    t.pendown()

# 결과 출력
print(f"총 이동 거리: {total_distance:.2f}픽셀")

check_x, check_y = t.pos()

if check_x < -260 and check_y < -260:
    print("목적지 도착")

turtle.done()
