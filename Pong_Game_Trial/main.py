from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor("green")
screen.title("My_Trial_Pong_Game")
screen.tracer(0)

l_paddle = Paddle((350,0))
r_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.ball_move()

    if ball.ycor() > 280 or  ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380 or  ball.xcor() < -380:
        ball.bounce_x()
        ball.goto(0,0)

    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()