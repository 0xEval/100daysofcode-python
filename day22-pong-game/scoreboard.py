from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(-200, 200)
        self.write(
            f'{self.l_score}',
            align='center',
            font=('Courier', 50, 'normal'),
        )

        self.goto(200, 200)
        self.write(
            f'{self.r_score}',
            align='center',
            font=('Courier', 50, 'normal'),
        )

    def l_point(self) -> None:
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self) -> None:
        self.r_score += 1
        self.update_scoreboard()
