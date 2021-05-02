from turtle import Turtle
from random import randint, choice

AXIS_DISPLACEMENT = randint(8, 10)
INITIAL_MOVE_SPEED = AXIS_DISPLACEMENT/100
DIRECTION = [-1, 1]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fast")
        self.x_move = AXIS_DISPLACEMENT * choice(DIRECTION)
        self.y_move = AXIS_DISPLACEMENT
        self.move_speed = INITIAL_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = INITIAL_MOVE_SPEED
        self.x_move *= -1
