from tkinter import *
from tkinter import messagebox
from pathlib import Path

THEME_COLOR = "#375362"

image_true_path = Path(__file__).parent / "images" / "true.png"
image_false_path = Path(__file__).parent / "images" / "false.png"

class QuizInterface():
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

        self.current_question = self.question_list[self.question_number]

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.resizable(False, False)
        self.window.config(bg=THEME_COLOR)

        self.label_score = Label(text=f"Score: {self.score}", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR)
        self.label_score.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.id_text = self.canvas.create_text(
            150, 125, 
            text=self.current_question.text, 
            font=("Arial", 20, "italic"),
            fill="black",
            width=280
            )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        
        self.image_true = PhotoImage(file=image_true_path)
        self.button_true = Button(image=self.image_true, command=self.button_true)
        self.button_true.grid(row=2, column=0, padx=20, pady=20)

        self.image_false = PhotoImage(file=image_false_path)
        self.button_false = Button(image=self.image_false, command=self.button_false)
        self.button_false.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()

    def button_true(self):
        answer = "True"
        self.check_answer(answer)

    def button_false(self):
        answer = "False"
        self.check_answer(answer)
    
    def next_question(self):
        self.canvas.config(bg="white")

        if self.question_number < len(self.question_list):
            self.current_question = self.question_list[self.question_number]
            self.canvas.itemconfig(
                self.id_text,
                text=self.current_question.text
            )
        else:
            messagebox.showinfo("Game Over", f"List of question is over. You get {self.score} score of 10 questions.")
            exit()

    def check_answer(self, answer):
        if self.current_question.answer == answer:
            self.canvas.config(bg="green")
            
            self.score += 1
            self.label_score.config(text=f"Score: {self.score}")
            
        else:
            self.canvas.config(bg="red")

        self.question_number += 1

        self.window.after(1000, self.next_question)