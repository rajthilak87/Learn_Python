from turtle import Turtle, Screen
import random

screen = Screen()
user_bet = screen.textinput(title = "Who will the Race" , prompt = "Please enter the color tutor you bet ? " )
colors = ["blue","cyan","green","red","orange"]
y_pos = [0,30,60,90,120]

race_on = False
all_turtles = []

for n in range(0,5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[n])
    new_turtle.goto(x= -250, y = y_pos[n])
    all_turtles.append(new_turtle)

race_on = True

while race_on:
    for each in all_turtles:
        if each.xcor() > 250:
            winning_color = each.pencolor()
            race_on = False
            if winning_color == user_bet:
                print(f"You WON the RACE. The {winning_color} Color Turtle is the WINNER !!!")            
            else:
                print(f"You LOST the RACE. The {winning_color} Color Turtle is the WINNER !!!")
        random_dist = random.randint(1,10)
        each.forward(random_dist)
        

screen.exitonclick()
