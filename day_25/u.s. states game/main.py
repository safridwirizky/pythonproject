from turtle import Screen, Turtle
from pathlib import Path
import pandas

screen = Screen()
turtle = Turtle()

game = str(Path(__file__).with_name("blank_states_img.gif"))
data_path = Path(__file__).with_name("50_states.csv")

screen.title("U.S. States Game")
screen.addshape(game)
turtle.shape(game)

pen = Turtle()

pen.hideturtle()
pen.penup()
pen.speed(0)

data = pandas.read_csv(data_path)

game_is_on = True
while game_is_on:
    user_input = input("Tebak state: ").title()

    if user_input in data.state.values:
        pen.goto(int(data[data["state"] == user_input].x.iloc[0]), int(data[data["state"] == user_input].y.iloc[0]))
        pen.write(user_input, font=("Arial", 12, "normal"))