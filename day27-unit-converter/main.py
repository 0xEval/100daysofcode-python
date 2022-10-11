import tkinter as tk


def btn_calculate() -> None:
    miles = float(miles_entry.get())
    kms = miles * 1.609
    dist_label.config(text=f'{kms}')


window = tk.Tk()
window.title('Tkinter GUI')
window.config(padx=50, pady=50)

# Row 0
miles_entry = tk.Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = tk.Label(text='Miles', font=('Arial', 24, 'normal'))
miles_label.grid(column=2, row=0)

# Row 1
eq_label = tk.Label(text='is equal to', font=('Arial', 24, 'normal'))
eq_label.grid(column=0, row=1)

dist_label = tk.Label(text='0', font=('Arial', 24, 'normal'))
dist_label.grid(column=1, row=1)


km_label = tk.Label(text='Km', font=('Arial', 24, 'normal'))
km_label.grid(column=2, row=1)

# Row 2
button = tk.Button(text='Calculate', command=btn_calculate)
button.grid(column=1, row=2)

window.mainloop()   # Needs to be at the end of the program
