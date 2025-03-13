from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=600, height=600)

snake = Snake()

def move_up():
    if snake.segments[0].heading() != 270:
        if snake.segments[0].heading() != 90:
            snake.segments[0].setheading(90)

def move_left():
    if snake.segments[0].heading() != 0:
        if snake.segments[0].heading() != 180:
            snake.segments[0].setheading(180)

def move_down():
    if snake.segments[0].heading() != 90:
        if snake.segments[0].heading() != 270:
            snake.segments[0].setheading(270)

def move_right():
    if snake.segments[0].heading() != 180:
        if snake.segments[0].heading() != 0:
            snake.segments[0].setheading(0)

screen.onkey(fun=move_up, key='w')
screen.onkey(fun=move_left, key='a')
screen.onkey(fun=move_down, key='s')
screen.onkey(fun=move_right, key='d')

screen.update()

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    snake.move()

screen.exitonclick()