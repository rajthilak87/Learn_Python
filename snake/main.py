from turtle import Screen
from snake import Snake
from ball import Food
from scoreboard import Scoreboard
import time 


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("green")
screen.title("!!!!!!!!***********My_Snake_Game*********!!!!!!!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreb = Scoreboard()
game_on = True

screen.listen()
screen.onkey(snake.go_up,"Up")
screen.onkey(snake.go_down,"Down")
screen.onkey(snake.go_left,"Left")
screen.onkey(snake.go_right,"Right")

while game_on:
    screen.update()
    time.sleep(.3)
    snake.move_snake()
    
    if snake.head.distance(food) < 15:
        scoreb.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290  :
        scoreb.reset() 
        snake.reset()  

    for seg in snake.segment:
        if snake.head == seg:
            pass
        elif snake.head.distance(seg) < 10:
            scoreb.reset()
            snake.reset() 
               
screen.exitonclick()


