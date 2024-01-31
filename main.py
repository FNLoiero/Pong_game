from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

l_player = Paddle(-350)
r_player = Paddle(350)
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(l_player.up, "Up")
screen.onkey(l_player.down, "Down")
screen.onkey(r_player.up, "w")
screen.onkey(r_player.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(r_player) < 50) or (ball.distance(l_player) < 50 and ball.xcor() < -320) :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_score()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_score()

screen.exitonclick()