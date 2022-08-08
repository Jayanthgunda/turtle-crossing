from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_end(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
