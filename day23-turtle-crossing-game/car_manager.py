import random
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Cars:
# 1) Render one car on screen
# 2) Handle y-axis car movement
# 3) Randomize car position on screen
# 4) Randomize car colour
# 5) Create random car function
# 6) Handle car collision with player


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self) -> None:
        random_chance = random.randint(1, 10)
        if random_chance == 5:
            self.cars.append(Car())

    def move_cars(self) -> None:
        for car in self.cars:
            car.move(self.car_speed)

    def increase_speed(self) -> None:
        self.car_speed += MOVE_INCREMENT
        self.move_cars()


class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.move_speed = STARTING_MOVE_DISTANCE
        self.starting_pos()

    def starting_pos(self) -> None:
        new_y = random.randint(-250, 250)
        self.goto(x=300, y=new_y)
        self.setheading(180)

    def increase_speed(self) -> None:
        self.move_speed += MOVE_INCREMENT

    def move(self, speed) -> None:
        self.fd(speed)
