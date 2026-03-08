from tkinter import *
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("POMODORO")
window.minsize(width=500, height=500)

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


# Capture image
imgpath = Path(__file__).parent / "tomato.png"
img = PhotoImage(file=imgpath)

# Create Canvas
canvas = Canvas(width=200, height=300, highlightthickness=0)
canvas.create_image(100, 100, image=img)
timer_text = canvas.create_text(
    100,
    122,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 40, "bold"),
)
canvas.pack()

# Fungsi countdown
def start_timer(count=WORK_MIN*60):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        window.after(1000, start_timer, count - 1)
    else:
        canvas.itemconfig(timer_text, text="Times Up!")


# Button start timer
button_start = Button(text="Start", command=start_timer)
button_start.pack()

window.mainloop()