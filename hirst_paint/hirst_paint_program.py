import turtle as t   
from extract_color import color_list
import random
 
tim = t.Turtle()
screen = t.Screen()
tim.penup()
tim.hideturtle()
tim.shape("arrow")
t.colormode(255)
tim.speed("fastest")
number_of_dots = 100
tim.goto(0, -250)

def dot_list():  
    tim.color(random.choice(color_list)) 
    tim.dot(20)
    tim.penup()
    tim.fd(50)

def print_dot():
    for n in range(1, number_of_dots):
        dot_list()   
        if n % 10 == 0:
            tim.setheading(90)
            tim.fd(50)
            tim.left(90)        
            tim.fd(500)
            tim.setheading(0) 


    
print_dot()



screen.exitonclick()