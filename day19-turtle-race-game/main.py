import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

RAINBOW_COLORS = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple',
]


def has_reached_finishline(turtle) -> bool:
    (x, y) = turtle.pos()
    return x >= screen.window_width() / 2 - 25


turtle_gang = []
y_offset = 25 * (6 / 2)
for id in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(RAINBOW_COLORS[id])
    new_turtle.setpos(
        (-screen.window_width() + 25) / 2, -y_offset + (id + 1) * 25
    )
    turtle_gang.append(new_turtle)

is_race_done = False
while not is_race_done:
    for turtle in turtle_gang:
        if has_reached_finishline(turtle):
            print(f'The {turtle.pencolor()} turtle has won!')
            is_race_done = True
        turtle.fd(random.randint(1, 10))

screen.exitonclick()
