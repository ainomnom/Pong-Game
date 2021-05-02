from turtle import Turtle


class Net(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(3)
        self.penup()
        self.sety(-300)
        self.pendown()
        self.setheading(90)
        for i in range(35):
            self.forward(15)
            self.penup()
            self.forward(5)
            self.pendown()
