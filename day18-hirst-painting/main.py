import random
import colorgram
import turtle

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)


def draw_dotline(canvas_x, canvas_y, offset) -> None:
    for x in range(0, canvas_x, offset):
        for y in range(0, canvas_y, offset):
            tim.setpos(y, x)
            tim.pencolor(random.choice(rgb_colors))
            tim.dot()


screen = turtle.Screen()
screen.setworldcoordinates(
    -25, -25, screen.window_width() - 1, screen.window_height() - 1
)
screen.colormode(255)

tim = turtle.Turtle()
tim.shape('turtle')
tim.speed('fastest')
tim.penup()
tim.pensize(15)

spacing = 50
dot_size = 20
canvas_x = (spacing + dot_size) * 10
canvas_y = (spacing + dot_size) * 10

draw_dotline(canvas_x, canvas_y, spacing + dot_size)

# tim.hideturtle()
screen.exitonclick()
