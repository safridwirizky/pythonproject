import colorgram
import turtle as t

def painting():
    tim = t.Turtle()
    tim.penup()
    t.colormode(255)
    tim.pensize(20)

    colors = []

    extracted = colorgram.extract('Nopaline.jpg', 16)

    for i in extracted:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        colors.append((r, g, b))

    x = -100
    y = -100
    for i, v in enumerate(colors):
        tim.color(v)
        tim.goto(x, y)
        tim.pendown()
        tim.forward(1)
        tim.penup()

        if (i + 1) % 4 == 0:
            y += 50
            x -= 150
        else:
            x += 50