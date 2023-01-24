from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen() 
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("*******Snake Game******")
screen.tracer(0)

snake_game = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


while snake_game:
    screen.update()
    time.sleep(.2)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        scoreboard.clear()
        scoreboard.score += 1
        scoreboard.scoreb()
        snake.extend()
        food.refresh()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       scoreboard.game_over()
       snake_game = False
    
    for seg in snake.segment:
        if snake.head == seg:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.game_over()
            snake_game = False
        

screen.exitonclick()

