from turtle import Screen, Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    
    def create_snake(self):
        for n in STARTING_POSITION:
            self.add_segment(n)

    def add_segment(self, n):
        square = Turtle()
        square.color("white")
        square.shape("square")
        square.penup()
        square.goto(n)
        self.segment.append(square)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move_snake(self):
        for k in range(len(self.segment)-1,0,-1):
            new_x = self.segment[k-1].xcor()
            new_y = self.segment[k-1].ycor()
            self.segment[k].setpos(new_x, new_y)
        self.head.forward(20)
 

    def move_up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)




