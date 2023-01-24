from turtle import Turtle, Screen


screen = Screen()
colors = ["red","blue","green","cyan","magenta"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color : ")
y_pos = [0,30,60,90,120]

for n in range(0,5):
    tim = Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.color(colors[n])
    tim.goto(-250,y_pos[n])

screen.exitonclick()