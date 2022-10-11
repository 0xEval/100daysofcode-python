import time
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

win = Screen()
win.setup(height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
win.bgcolor('black')
win.title('The Snake Game')
win.tracer(
    0
)   # Disable automatic refresh of the screen, needs update() to be called

# Step 1: create the body of the snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

win.listen()
win.onkey(fun=snake.up, key='Up')
win.onkey(fun=snake.down, key='Down')
win.onkey(fun=snake.left, key='Left')
win.onkey(fun=snake.right, key='Right')

game_is_on = True
while game_is_on:
    win.update()
    time.sleep(0.1)
    snake.move(distance=20)

    # Detect food collision
    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

    # Detect walls
    if (
        snake.head.xcor() > WINDOW_WIDTH / 2 - snake.head.pensize()
        or snake.head.xcor() < -WINDOW_WIDTH / 2 + snake.head.pensize()
        or snake.head.ycor() > WINDOW_HEIGHT / 2 - snake.head.pensize()
        or snake.head.ycor() < -WINDOW_HEIGHT / 2 - snake.head.pensize()
    ):
        scoreboard.game_over()
        game_is_on = False


win.exitonclick()
