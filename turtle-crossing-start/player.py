from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE) 
    
    def restart(self):                    
        self.goto(STARTING_POSITION)
  
    def complete_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True 
        else: 
            return False
    

