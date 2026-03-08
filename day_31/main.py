from pathlib import Path
from tkinter import messagebox
import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


#------------------------- Organize Data ------------------------#

data_path = Path(__file__).parent / "data" / "arabic.csv"
df = pd.read_csv(data_path)

is_right = 0
random_row = df.sample(n=1)
def flash_card():
    global is_right, random_row, text_id, delay_3detik

    canvas.config(bg="white")
    canvas.itemconfig(text_id, text=random_row.iloc[0, 0])
    is_right = random.randint(0, 1)
    print(is_right)
    random_row = df.sample(n=1)
    window.after(3000, delay_3detik)

#----------------------- Button Function ------------------------#

def button_ok_func():
    global is_right, random_row
    
    if is_right == 1:
        messagebox.showinfo("", "Anda Benar")
    else:
        messagebox.showinfo("", f"Anda Salah\n\nYang benar = {random_row.iloc[0, 1]}")
    
    flash_card()

def button_false_func():
    global is_right

    if is_right == 0:
        messagebox.showinfo("", "Anda Benar")
    else:
        messagebox.showinfo("", "Anda Salah")

    flash_card()

#------------------------------ UI ------------------------------#

window = tk.Tk()
window.title("Flash Card")
window.minsize(width=600, height=500)
window.resizable(False, False)

canvas = tk.Canvas(width=300, height=300)
canvas.pack()

text_id = canvas.create_text(
    100,
    100,
    text=random_row.iloc[0, 0],
    font=("Arial", 26, "normal"),
    fill="black"
)

button_ok_path = Path(__file__).parent / "images" / "right.png"
button_false_path = Path(__file__).parent / "images" / "wrong.png"

image_ok = tk.PhotoImage(file=str(button_ok_path))
image_false = tk.PhotoImage(file=str(button_false_path))

button_ok = tk.Button(image=image_ok, highlightthickness=0, command=button_ok_func)
button_ok.pack()
button_false = tk.Button(image=image_false, highlightthickness=0, command=button_false_func)
button_false.pack()

def delay_3detik():
    global random_row
    canvas.config(bg=BACKGROUND_COLOR)
    if is_right == 0:
        rand_row = df.sample(n=1)
        canvas.itemconfig(text_id, text=rand_row.iloc[0, 1])
    else:    
        canvas.itemconfig(text_id, text=random_row.iloc[0, 1])

flash_card()

window.mainloop()