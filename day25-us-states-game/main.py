import turtle
import pandas as pd
from turtle import Turtle, Screen


def write_state(name, x, y) -> None:
    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.speed('fastest')
    writer.goto(x, y)
    writer.write(name)


window = Screen()
image = 'blank_states_img.gif'
window.addshape(image)
window.title('USA States Game')

t = Turtle()
t.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    ans = window.textinput(
        title=f'{len(guessed_states)}/50 States Correct',
        prompt="What's another state's name?",
    ).title()

    if ans == 'Exit':
        missing_states = [
            state for state in all_states if state not in guessed_states
        ]
        pd.DataFrame(missing_states).to_csv('states_to_learn.csv')
        break

    if ans in all_states:
        guessed_states.append(ans)
        state_data = data[data.state == ans]
        write_state(
            state_data.state.values[0], int(state_data.x), int(state_data.y)
        )
