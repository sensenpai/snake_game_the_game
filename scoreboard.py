from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.pendown()
        self.write(arg=f"Score: {self.score}",align="center", font=("arial", 20, "normal"))

    def game_over(self):
        self.color("green")
        self.hideturtle()
        self.penup()
        self.setposition(0,0)
        self.pendown()
        self.write(arg="GAME OVER", align="center", font=("arial", 40, "normal"))

    def increase_score(self):
        self.score += 1
        self.write_score()
