import random
import string
import json
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


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password() -> None:
    website = website_entry.get()
    try:
        with open('data.json', 'r') as read_f:
            data = json.load(read_f)
    except FileNotFoundError:
        tk.messagebox.showinfo(message='No data file found :(')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            tk.messagebox.showinfo(
                message=f'Website: {website}\nEmail: {email}\nPassword: {password}',
            )
        else:
            tk.messagebox.showinfo(message='No details found :(')


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data() -> None:

    website = website_entry.get()
    email = identity_entry.get()
    password = password_entry.get()

    new_data = {website: {'email': email, 'password': password}}

    if len(email) == 0 or len(password) == 0:
        tk.messagebox.showwarning(
            title=website, message='Email/Password cannot be empty!'
        )

    else:
        try:
            with open('data.json', 'r') as read_f:
                # Read existing credentials in JSON file, save to Python Dict
                data = json.load(read_f)
                # print(type(data))
        except FileNotFoundError:
            # JSON File does not exist, create it and write credentials
            with open('data.json', 'w') as write_f:
                json.dump(new_data, write_f, indent=4)
        else:
            # JSON File already exists, get deserialized JSON to data, update and write back
            data.update(new_data)
            with open('data.json', 'w') as write_f:
                json.dump(data, write_f, indent=4)
        finally:
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

website_entry = tk.Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()

identity_entry = tk.Entry(width=38)
identity_entry.grid(row=2, column=1, columnspan=2)
identity_entry.insert(0, 'llomiecorp@llc.com')

password_entry = tk.Entry(width=20)
password_entry.grid(row=3, column=1)


# Buttons

search_button = tk.Button(text='Search', width=13, command=find_password)
search_button.grid(row=1, column=2)

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
