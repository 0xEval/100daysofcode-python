import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Game Requirements
# --------------------------------------------------------------------------------
# A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
#
# 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
#
#
# 3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
#
# 4. When the turtle collides with a car, it's game over and everything stops.

# TO-DOs
# --------------------------------------------------------------------------------
# Player [DONE]:
# 1) Create class Player which is a Turtle
# 2) Handle player movements
# 3) Detect collision with top edge of screen
# 4) Reset position

# Cars:
# 1) Render one car on screen
# 2) Handle y-axis car movement
# 3) Randomize car position on screen
# 4) Randomize car colour
# 5) Create random car function
# 6) Handle car collision with player
#
# Scoreboard:
# 1) Print score top-left of board
# 2) Increase score when player wins
# 3) Game over when car collides in player


screen = Screen()
screen.title('Turtle Crossing Game')
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkey(key='Up', fun=player.move_up)

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) <= 30:
            scoreboard.game_over()
            player.reset_position()

    if player.has_reached_finishline():
        player.reset_position()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
