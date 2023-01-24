from turtle import Turtle, Screen

 
        
timmy_the_turtle = Turtle()

def run():
    timmy_the_turtle.color("black") 
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90) 

     
timmy_the_turtle.shape("turtle") 
timmy_the_turtle.color("Coral")
for n in range(0,2):    
    timmy_the_turtle.color("Grey16")
    run()
    timmy_the_turtle.color("Red")
    run()







screen = Screen()
screen.exitonclick()