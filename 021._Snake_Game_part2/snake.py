from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.body_snake()

    def body_snake(self):
        for i in range(3, 0, -1):
            seg = Turtle()
            seg.penup()
            seg.shape('square')
            seg.color('white')
            seg.shapesize(1)
            seg.goto(x=((i-2) * 20), y=0)

            self.segments.append(seg)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)


















