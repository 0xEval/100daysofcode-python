import time
import math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer() -> None:
    global reps
    reps = 0
    canvas.itemconfigure(timer_txt, text=f'{WORK_MIN}:00')
    timer_lbl.config(text='Timer', fg=GREEN)
    pomodoro_lbl.config(text='')
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def update_timer() -> None:
    start_time = canvas.itemcget(timer_txt, 'text')
    now = time.time()
    time_lapsed = time.strftime(now) - start_time
    canvas.itemconfigure(timer_txt, text=time_lapsed)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count) -> None:
    global timer
    mins = math.floor(count / 60)
    sec = math.floor(count % 60)
    if count > 0:
        canvas.itemconfigure(timer_txt, text=f'{mins:02}:{sec:02}')
        timer = window.after(1000, countdown, count - 1)
    else:
        start_countdown()
        marks = ''.join(['✔' for _ in range(math.floor(reps / 2))])
        pomodoro_lbl.config(text=marks)


def start_countdown() -> None:
    global reps
    reps += 1

    work_sec = 5
    short_break_sec = 2
    long_break_sec = 3

    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_lbl.config(text='RELAX', fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_lbl.config(text='BREAK', fg=PINK)
        countdown(short_break_sec)
    else:
        timer_lbl.config(text='WORK', fg=GREEN)
        countdown(work_sec)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

timer_lbl = tk.Label(
    text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold')
)
timer_lbl.grid(row=0, column=1)

pomodoro_lbl = tk.Label(fg=GREEN, bg=YELLOW)
pomodoro_lbl.grid(row=3, column=1)

start_btn = tk.Button(
    text='Start', highlightbackground=YELLOW, command=start_countdown
)
start_btn.grid(row=2, column=0)

reset_btn = tk.Button(
    text='Reset', highlightbackground=YELLOW, command=reset_timer
)
reset_btn.grid(row=2, column=3)

img = tk.PhotoImage(file='tomato.png')
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_txt = canvas.create_text(
    100, 130, text=f'{WORK_MIN}:00', fill='white', font=(FONT_NAME, 35, 'bold')
)
canvas.grid(row=1, column=1)

window.mainloop()
