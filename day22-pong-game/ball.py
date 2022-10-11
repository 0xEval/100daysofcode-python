import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_speed = 0.025
        self.x_move = 5
        self.y_move = 5
        self.random_start()

    def random_start(self) -> None:
        f = random.choice([self.bounce_y, self.bounce_x, None])
        if f != None:
            f()

    def increase_speed(self) -> None:
        self.move_speed *= 0.8

    def reset_position(self) -> None:
        self.goto(0, 0)
        self.move_speed = 0.025
        self.bounce_x()

    def move(self) -> None:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self) -> None:
        self.x_move = self.x_move * -1

    def bounce_y(self) -> None:
        self.y_move = self.y_move * -1
