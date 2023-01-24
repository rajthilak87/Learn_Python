import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("arrow")
tim.pensize(5)
tim.speed("normal")

directions = [0,90,180,270]
colors = ["red","blue","orange","pink"]

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand = (r,g,b)
    return rand

screen = t.Screen() 

def wander():
    tim.setheading(random.choice(directions))
    tim.color(random_colors())
    tim.forward(20)



for _ in range(0,200):
    wander()

screen.exitonclick()






