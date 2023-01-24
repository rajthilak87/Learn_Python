from turtle import Turtle

POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def create_snake(self):
        for n in POSITION:
            self.add_segment(n)

    def add_segment(self,n):
        square = Turtle()
        square.shape("square")
        square.color("white")
        square.penup()
        square.goto(n)
        self.segment.append(square)

    def move_snake(self):
        for k in range(len(self.segment) -1, 0, -1):
            new_x = self.segment[k-1].xcor()
            new_y = self.segment[k-1].ycor()
            self.segment[k].setpos(new_x,new_y)
        self.head.forward(20)
    
    def extend(self):        
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def go_up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def go_left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def go_down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)