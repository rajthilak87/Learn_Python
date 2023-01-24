import turtle as t   
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    select_color = (r,g,b)
    return select_color
    
def cont_cir():
    tim.color(rand_color())
    tim.circle(50)
    tim.left(5)
    
  
    
for _ in range(0,80):
    cont_cir()

screen = t.Screen()
screen.exitonclick()
