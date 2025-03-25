from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(.5)
        self.color("red")
        self.refresh()
    
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))