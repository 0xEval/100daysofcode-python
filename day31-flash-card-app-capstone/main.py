import tkinter as tk
import pandas as pd
import random

# ------------------------------ Const ---------------------------------------

BACKGROUND_COLOR = '#B1DDC6'
CARD_WIDTH = 800
CARD_HEIGHT = 526
PADDING_U = 50

current_card = {}
to_learn = {}
flip_timer = ''   # Useless - just to shut up Pylint


# ----------------------------- Data Handling ---------------------------------

try:
    # Game has been played before
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    orig_df = pd.read_csv('data/french_words.csv')
    to_learn = orig_df.to_dict(orient='records')
    print(to_learn)
else:
    to_learn = df.to_dict(orient='records')
    print(to_learn)

# --------------------------- Callback Functions ------------------------------


def next_card() -> None:
    """
    Draw a new card and display it on the game Canvas, then
    start a timer to let the player guess
    """
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    card_canvas.itemconfigure(card_image, image=front_card_img)
    card_canvas.itemconfigure(
        card_title, text='French', fill='black', font=('Arial', 40, 'italic')
    )
    card_canvas.itemconfigure(
        card_word, text=current_card['French'], fill='black'
    )
    flip_timer = window.after(5000, func=flip_card)


def remove_card() -> None:
    """
    Removes the current card from output `.csv` to prevent drawing again,
    then draw a new card
    """
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


def flip_card() -> None:
    """
    Update the game Canvas to show the `English` translation of the current card
    """
    card_canvas.itemconfigure(card_image, image=card_back_img)
    card_canvas.itemconfigure(card_title, text='English', fill='white')
    card_canvas.itemconfigure(
        card_word, text=current_card['English'], fill='white'
    )


# ------------------------------ TKInter GUI ----------------------------------

window = tk.Tk()
window.title('Flashy')
window.minsize(
    width=CARD_WIDTH + PADDING_U, height=CARD_HEIGHT + 3 * PADDING_U
)
window.config(background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Card Widget

card_back_img = tk.PhotoImage(file='./images/card_back.png')
front_card_img = tk.PhotoImage(file='./images/card_front.png')
wrong_img = tk.PhotoImage(file='./images/wrong.png')
right_img = tk.PhotoImage(file='./images/right.png')

card_canvas = tk.Canvas(
    width=CARD_WIDTH + PADDING_U,
    height=CARD_HEIGHT + PADDING_U,
    bg=BACKGROUND_COLOR,
    highlightbackground=BACKGROUND_COLOR,
)
card_image = card_canvas.create_image(
    (CARD_WIDTH + PADDING_U) / 2,
    (CARD_HEIGHT + PADDING_U) / 2,
    image=front_card_img,
)
card_title = card_canvas.create_text(
    CARD_WIDTH / 2, 150, text='Title', font=('Arial', 40, 'italic')
)
card_word = card_canvas.create_text(
    CARD_WIDTH / 2, 263, text='Word', font=('Arial', 60, 'bold')
)

wrong_canvas = tk.Canvas(
    height=150,
    width=400,
    bg=BACKGROUND_COLOR,
    highlightbackground=BACKGROUND_COLOR,
)
wrong_btn = wrong_canvas.create_image(250, 50, image=wrong_img)
wrong_canvas.tag_bind(wrong_btn, '<Button-1>', lambda x: next_card())

right_canvas = tk.Canvas(
    height=150,
    width=400,
    bg=BACKGROUND_COLOR,
    highlightbackground=BACKGROUND_COLOR,
)
right_btn = right_canvas.create_image(130, 50, image=right_img)
right_canvas.tag_bind(right_btn, '<Button-1>', lambda x: remove_card())

# ---- Geometry -----

card_canvas.grid(row=0, column=0, columnspan=2)
wrong_canvas.grid(column=0, row=1)
right_canvas.grid(column=1, row=1)

next_card()   # Load the first card

window.mainloop()

# ------------------------------------------------------------------------------
