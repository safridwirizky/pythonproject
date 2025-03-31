from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.STARTING_POSITION = [
            (20, 0),
            (0, 0),
            (-20, 0),
        ]
        self.body_snake()

    def body_snake(self):
        for seg in self.STARTING_POSITION:
            self.add_segment(seg)
    
    def add_segment(self, position):
        seg = Turtle()
        seg.penup()
        seg.shape('square')
        seg.color('white')
        seg.shapesize(1)
        seg.speed('fastest')
        seg.goto(position)

        self.segments.append(seg)
    
    def extend():
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)