import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def spirograph():
    t.colormode(255)
    tim = t.Turtle()
    tim.speed('fastest')

    for i in range(36):
        tim.color(random_color())
        tim.setheading(i * 10)
        tim.circle(100)