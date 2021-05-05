import math
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.game_level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.sety(265)
        self.setx(-285)

        self.write(arg=f"Level:  {self.game_level}", font=("Arial", 20, "normal"))

        # Draws a finish line in the weirdest wy I could think of:
        self.setx(-300)
        self.sety(260)
        self.setheading(0)
        self.pensize(4)
        self.pendown()
        ycoord = self.ycor()

        for i in range(16, 1, -3):
            ycoord -= 4
            self.setx(-300 + (math.ceil(i % 2 * 5)))
            self.sety(ycoord)
            for _ in range(0, 120, 2):
                self.pendown()
                self.forward(5)
                self.penup()
                self.forward(5)

    def level_up(self):
        self.game_level += 1
