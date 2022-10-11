from turtle import Turtle


ALIGNMENT = 'center'
STYLE = ('Inconsolata', 16, 'bold')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.hideturtle()
        self.update()

    def update(self) -> None:
        self.write(f'Score = {self.score}', False, ALIGNMENT, STYLE)

    def game_over(self) -> None:
        self.clear()
        self.write('GAME OVER!', False, ALIGNMENT, STYLE)

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.update()
