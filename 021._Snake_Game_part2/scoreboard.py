from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 600)
        self.color("white")
        self.score =0
        self.NORMAL_WORD = f"Score: {self.score}"
        self.GAME_OVER = "Game Over"
        self.refresh(self.NORMAL_WORD)
    
    def refresh(self, word):
        self.score += 1
        self.clear()
        self.write(word, align="center", font=("Arial", 24, "normal"))
    
    def game_over(self):
        self.refresh(self.GAME_OVER)