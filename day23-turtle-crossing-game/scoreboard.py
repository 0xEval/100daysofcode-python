from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(-225, 225)
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def increase_score(self) -> None:
        self.score += 1

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=FONT)
