from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.NORMAL_WORD = "Score: "
        self.score =0
        self.GAME_OVER = "Game Over"
        self.refresh(self.NORMAL_WORD + str(self.score))
    
    def refresh(self, word):
        self.clear()
        self.write(word, align="center", font=("Arial", 24, "normal"))
    
    def game_over(self):
        self.refresh(self.GAME_OVER)