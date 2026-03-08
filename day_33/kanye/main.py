from tkinter import *
from pathlib import Path
import requests


def get_quote():
    global canvas, quote_text

    url = "https://api.kanye.rest/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        canvas.itemconfig(quote_text, text=data["quote"])
    else:
        canvas.itemconfig(quote_text, text=f"Error: {response.status_code}")

bg_path = Path(__file__).parent / "background.png"
btn_path = Path(__file__).parent / "kanye.png"

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=str(bg_path))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=str(btn_path))
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()