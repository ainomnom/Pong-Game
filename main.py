from turtle import Screen
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

net = Net()
red_paddle = Paddle(350, "red")
blue_paddle = Paddle(-350, "blue")
ball = Ball()

red_player = screen.textinput(title="Red player", prompt="Input red player's name:")
blue_player = screen.textinput(title="Blue player", prompt="Input blue player's name:")
max_score = int(screen.textinput(title="Maximum score", prompt="Input the maximum score:"))

scoreboard = Scoreboard(red_player, blue_player)

screen.listen()
screen.onkey(fun=red_paddle.up, key="Up")
screen.onkey(fun=red_paddle.down, key="Down")
screen.onkey(fun=blue_paddle.up, key="w")
screen.onkey(fun=blue_paddle.down, key="s")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)  # increases speed every time a ball gets hit by paddle
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.distance(red_paddle) < 50 and ball.xcor() > 320) or (ball.distance(blue_paddle) < 50 and
                                                                  ball.xcor() < -320):
        ball.bounce_x()

    # Detect if red paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.red_point()

    # Detect if blue paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.blue_point()

    if scoreboard.red_score == max_score or scoreboard.blue_score == max_score:
        game_is_on = False
        scoreboard.announce_winner()

screen.exitonclick()
