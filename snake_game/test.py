from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("green")
screen.title("My Snake Game")

starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []
screen.tracer(0)

for position in starting_positions:
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.setpos(position)
    segments.append(new_turtle)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].setpos(new_x,new_y)
    
    segments[0].forward(20)

screen.exitonclick()