import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.title('The Pong Game')
screen.bgcolor('black')
screen.setup(width=WIDTH, height=HEIGHT)
screen.listen()
screen.tracer(0)

# Setup Game Start
ball = Ball()
scoreboard = Scoreboard()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.onkey(key='Up', fun=left_paddle.move_up)
screen.onkey(key='Down', fun=left_paddle.move_down)
screen.onkey(key='w', fun=right_paddle.move_up)
screen.onkey(key='s', fun=right_paddle.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Collsion with Top/Bottom Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with Paddle
    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 60
        and ball.xcor() < -320
    ):
        ball.bounce_x()
        ball.increase_speed()

    # Ball goes out-of-bounds
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
