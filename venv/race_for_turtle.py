from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
user_bet = screen.textinput(title="Who will WIN the race", prompt="Please enter a color : ")
colors = ["orange","green","red","blue","cyan"]
y_posi = [0,30,60,90,120]
all_turtles = []

for n in range(0,5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x= -230, y = y_posi[n])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You WON the RACE. The {winning_color} turtle won the race")
            else:
                print(f"You LOST the RACE. The {winning_color} turtle won the race")

screen.exitonclick()
