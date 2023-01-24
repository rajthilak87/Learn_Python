from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

colors  = ['black', 'gold', 'yellow', 'orange', 'red', 'blue', 'purple','cyan','turquoise','olive','navy']
timmy_the_turtle.width("5") 
timmy_the_turtle.shape("turtle") 


def run():
    
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(an)     

no_of_sides = 11
for i in range(3, no_of_sides):
    an = 360 / i
    print(an)        
    timmy_the_turtle.color(random.choice(colors))
    
    
     # Make a list of colors to picvk from

    for n in range(0,i):    
        
        run()        
screen = Screen()
screen.exitonclick()
