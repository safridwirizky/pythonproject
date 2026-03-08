from tkinter import messagebox
import tkinter as tk
from pathlib import Path
import json
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def search():
    file_path = Path(__file__).parent / "password.json"
    data = {}
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        for website in data:
            if website == entry1.get():
                messagebox.showinfo(f"{website}", f"email: {data[website]['username']}\npassword: {data[website]['password']}")
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write("{}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password(length = 12):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    all_char = letters + digits + punctuation

    password = "".join(random.choice(all_char) for _ in range(length))
    entry3.delete(0, tk.END)
    entry3.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_akun():
    file_path = Path(__file__).parent / "password.json"

    data = {}

    with open(file_path, "r") as file:
        data = json.load(file)

    data[entry1.get()] = {
                "username" : entry2.get(),
                "password" : entry3.get(),
            }
    
    with open(file_path, "w") as file:
        file.write(json.dump(data, file, indent=4))

# ---------------------------- UI SETUP ------------------------------- #

image_path = Path(__file__).parent / "logo.png"

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=450, height=400)
window.resizable(False, False)

image = tk.PhotoImage(file=image_path)

canvas = tk.Canvas(width=300, height=200)
canvas.create_image(150, 100, image=image)
canvas.grid(row=0, column=1)

label1 = tk.Label(text="Website:")
label1.grid(row=1, column=0)
label2 = tk.Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = tk.Label(text="Password:")
label3.grid(row=3, column=0)

entry1 = tk.Entry()
entry1.grid(row=1, column=1, sticky="EW")
entry2 = tk.Entry()
entry2.grid(row=2, column=1, columnspan=2, sticky="EW")
entry3 = tk.Entry()
entry3.grid(row=3, column=1, sticky="EW")

button_search = tk.Button(text="Search", command=search)
button_search.grid(row=1, column=2, sticky="EW")
button_generate_pass = tk.Button(text="Generate", command=generate_password)
button_generate_pass.grid(row=3, column=2, sticky="EW")
button_add = tk.Button(text="Add", command=add_akun)
button_add.grid(row=4, column=1, columnspan=3, sticky="EW")

window.mainloop()