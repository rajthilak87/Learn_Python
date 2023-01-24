from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-150,260) 
        self.high_score = 0
        self.score = 0
        with open("c:/Users/dell/Desktop/my_result.txt", mode="r",) as j:
            # self.high_score = j.readlines()
            for line in j.readlines():
                self.high_score = int(line)

    def update_score(self):
        self.clear()        
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="left", font=("Arial", 25, "italic"))
        with open("c:/Users/dell/Desktop/my_result.txt", mode="w",) as f:
            f.write(str(self.high_score))


    def increase_score(self):
        self.score += 1
        self.update_score()


    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score     
        self.score = 0
        self.update_score()
        


