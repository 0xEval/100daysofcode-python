from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Player:
# 1) Create class Player which is a Turtle
# 2) Handle player movements
# 3) Detect collision with top edge of screen
# 4) Reset position


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.speed('slow')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move_up(self) -> None:
        self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)

    def reset_position(self) -> None:
        self.goto(STARTING_POSITION)

    def has_reached_finishline(self) -> bool:
        return self.ycor() >= 280
