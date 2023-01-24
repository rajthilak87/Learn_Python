import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(turtle_player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()
    
    for car in cars.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False    
            score.game_over()           
        
    if turtle_player.complete_level():         
        turtle_player.restart()
        score.update_score()  
        cars.level_up()  

screen.exitonclick()
  

            

