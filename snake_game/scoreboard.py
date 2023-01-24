from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=260)
        self.scoreb()
        self.hideturtle()

    def scoreb(self):
        self.write(f"Score: {self.score}",align="center",font=("Courier",24,"normal"))
    
    def game_over(self):
       self.goto(x=0,y=100)
       self.write(f"GAME OVER !!!",align="center",font=("Courier",24,"normal")) 
       