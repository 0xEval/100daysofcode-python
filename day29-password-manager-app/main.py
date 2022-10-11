import random
import string
import tkinter as tk
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password() -> None:
    # Password Generator Project
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [
        random.choice(letters) for char in range(random.randint(8, 10))
    ]
    password_list += [
        random.choice(symbols) for char in range(random.randint(2, 4))
    ]
    password_list += [
        random.choice(numbers) for char in range(random.randint(2, 4))
    ]

    random.shuffle(password_list)

    password = ''.join(password_list)
    print(f'Your password is: {password}')

    # Paste password to Entry
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data() -> None:

    website = website_entry.get()
    email = identity_entry.get()
    password = password_entry.get()

    if len(email) == 0 or len(password) == 0:
        tk.messagebox.showwarning(
            title=website, message='Email/Password cannot be empty!'
        )

    else:

        consent = tk.messagebox.askokcancel(
            title=website,
            message=f'Details Entered \nEmail:\t{email}\nPassword:\t{password}',
        )

        if consent:
            with open('data.txt', 'a') as write_f:
                write_f.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Labels

website_label = tk.Label(text='Website:')
website_label.grid(row=1, column=0)

identity_label = tk.Label(text='Email/Username:')
identity_label.grid(row=2, column=0)

password_label = tk.Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries

website_entry = tk.Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

identity_entry = tk.Entry(width=38)
identity_entry.grid(row=2, column=1, columnspan=2)
identity_entry.insert(0, 'llomiecorp@llc.com')

password_entry = tk.Entry(width=20)
password_entry.grid(row=3, column=1)


# Buttons

generate_button = tk.Button(
    text='Generate Password', command=generate_password
)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text='Add', width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


img = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, columnspan=3)

window.mainloop()
