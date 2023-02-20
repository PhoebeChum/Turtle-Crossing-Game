from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(-270, 265)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()