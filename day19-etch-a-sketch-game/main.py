from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def tilt_right():
    tim.setheading(tim.heading() - 5.0)


def tilt_left():
    tim.setheading(tim.heading() + 5.0)


def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=tilt_left)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=tilt_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
