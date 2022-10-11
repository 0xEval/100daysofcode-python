import time
from turtle import Turtle

COORDINATES = {'UP': 90, 'RIGHT': 0, 'LEFT': 180, 'DOWN': 270}
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]


class Snake:
    def __init__(self) -> None:
        self.body = []
        self.__create_snake()
        self.head = self.body[0]

    def __create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            self.__add_segment(position)

    def move(self, distance) -> None:
        """Moves the snake by `distance` amount of units"""
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.head.fd(distance)   # Head

    def __add_segment(self, position) -> None:
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.setpos(position)
        self.body.append(segment)

    def extend(self) -> None:
        self.__add_segment(self.body[-1].position())

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
