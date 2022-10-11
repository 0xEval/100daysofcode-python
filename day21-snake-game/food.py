import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # 10x10 circle
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self) -> None:
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
