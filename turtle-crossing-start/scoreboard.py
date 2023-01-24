from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200,250)
        self.score()

    def score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font = FONT) 

    
    def update_score(self):
        self.level += 1
        self.score()


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over !!!", align="center", font = FONT)
    
