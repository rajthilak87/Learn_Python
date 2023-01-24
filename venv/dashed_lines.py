from turtle import Turtle, Screen

 
        
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle") 
timmy_the_turtle.color("Coral")

def dashed_lines():
    timmy_the_turtle.pendown() 
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)

for _ in range(0,20):
    dashed_lines()
