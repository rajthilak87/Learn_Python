from turtle import Turtle, Screen
import random 

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race ? ")
colors = ["red","blue","green","orange","cyan"]
y_pos = [0,30,60,90,120]
tur_num = []

for n in range(0,5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_pos[n])
    tur_num.append(new_turtle)

if user_bet:
    race_on = True

while race_on:    
    for n in tur_num:        
        if n.xcor() > 230:
            race_on = False
            winning_color = n.pencolor()
            if winning_color == user_bet:
                print(f"Your won the race!!!. The {winning_color} color turtle is the winner ! ! !")
            else:
                print(f"Your lost the race!!!. The {winning_color} color turtle is the winner ! ! !")
        rand_dist = random.randint(0,10)
        n.forward(rand_dist)
screen.exitonclick()