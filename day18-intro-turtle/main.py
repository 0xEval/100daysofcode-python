import random
from turtle import Turtle, Screen

DIRECTIONS = {'north': 90, 'south': 270, 'east': 0, 'west': 180}


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(turtle, radius) -> None:
    turtle.speed('fastest')
    for _ in range(int(360 / radius)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.seth(turtle.heading() + radius)


def draw_shape_sequence(turtle) -> None:
    for sides in range(3, 9):
        turtle.pencolor(random_color())
        for s in range(sides):
            turtle.forward(100)
            turtle.right(360 / sides)


def draw_dashed_line(turtle) -> None:
    """Draw a dashed line from current position"""
    for i in range(50):
        if i % 2 == 0:
            turtle.penup()
        else:
            turtle.pendown()
        turtle.forward(10)


def draw_square(turtle) -> None:
    """Draw a 100x100 square from current position"""
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def random_walk(turtle) -> None:
    """Walk randomly"""
    turtle.speed('fast')
    turtle.pensize(10)
    while True:
        angle = random.choice(list(DIRECTIONS.values()))
        turtle.seth(angle)
        turtle.pencolor(random_color())
        turtle.forward(50)


screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape('turtle')

# draw_square(timmy)
# draw_dashed_line(timmy)
# draw_shape_sequence(timmy)
# random_walk(timmy)
draw_spirograph(timmy, 5)

screen.exitonclick()
