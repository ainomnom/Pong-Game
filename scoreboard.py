from turtle import Turtle

ALIGNMENT = "center"
FONT_1 = ("Courier", 60, "normal")
FONT_2 = ("Courier", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self, red_player, blue_player):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.red_player = red_player
        self.blue_player = blue_player
        self.red_score = 0
        self.blue_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.blue_score, align=ALIGNMENT, font=FONT_1)
        self.goto(100, 200)
        self.write(self.red_score, align=ALIGNMENT, font=FONT_1)

    def red_point(self):
        self.red_score += 1
        self.update_scoreboard()

    def blue_point(self):
        self.blue_score += 1
        self.update_scoreboard()

    def announce_winner(self):
        self.goto(0, 0)
        if self.red_score > self.blue_score:
            x_pos = 180
            winner = self.red_player
        else:
            x_pos = -180
            winner = self.blue_player
        self.setx(x_pos)
        self.write(f"{winner} wins!", align=ALIGNMENT, font=FONT_2)
