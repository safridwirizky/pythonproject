from tkinter import *

screen = Tk()
# screen.minsize(width=500, height=300)
screen.title("Mile to Km Converter")

label = Label(text="0")
label.grid(row=1, column=1)

entry1 = Entry()
entry1.grid(row=0, column=1)

label1 = Label(text="Mile")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

def change_label():
    n = float(entry1.get())
    n = n * 1.60934
    label.config(text=f"{n}")

button = Button(text="Click me", command=change_label)
button.grid(row=2, column=1)


screen.mainloop()