from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coords: tuple) -> None:
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5)
        self.shapesize(stretch_len=1)
        self.set_position(coords[0], coords[1])

    def set_position(self, x, y) -> None:
        self.setx(x)
        self.sety(y)

    def move_up(self):
        new_position = (self.xcor(), self.ycor() + 20)
        self.goto(new_position)

    def move_down(self):
        new_position = (self.xcor(), self.ycor() - 20)
        self.goto(new_position)
