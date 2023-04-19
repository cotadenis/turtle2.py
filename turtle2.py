import turtle
import random

turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()

for i in range(50):
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    size = random.randint(10, 50)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

turtle.done()
