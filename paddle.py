from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(color)
        self.speed("fast")
        self.setx(x_pos)

    def up(self):
        if self.ycor() <= 225:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def down(self):
        if self.ycor() >= -217:
            new_y = self.ycor() - 20
            self.sety(new_y)
