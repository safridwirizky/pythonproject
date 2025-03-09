from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Guess the turtle that will win? Type turtle's color: ")
print(user_bet)

all_turtles = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

x, y = -380, -245

for color in colors:
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.teleport(x=x, y=y)
    all_turtles.append(new_turtle)
    y += 100

speed = [10, 20, 30]

if user_bet:
    go = True
while go:
    for i, turtle in enumerate(all_turtles):
        if turtle.xcor() > 380:
            go = False

            if turtle.pencolor() == user_bet:
                print(f'You won. Your bet is right')
            else:
                print(f'You lost. The winning turtle is {turtle.pencolor()}')

            break

        turtle.forward(random.choice(speed))

screen.exitonclick()