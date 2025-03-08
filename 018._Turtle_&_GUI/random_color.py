import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def rand_color():
    tim = t.Turtle()
    t.colormode(255)
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    tim.speed('fastest')

    for _ in range(200):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(30)