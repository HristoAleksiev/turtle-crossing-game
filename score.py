import math
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.game_level = 1
        self.penup()
        self.hideturtle()
        self.color("black")

        self.display_level()
        self.draw_finish_line()

    def display_level(self):
        self.sety(265)
        self.setx(-285)

        self.write(arg=f"Level:  {self.game_level}", font=("Arial", 20, "normal"))

    def draw_finish_line(self):
        # Draws a finish line in the weirdest way I could think of:
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
        self.clear()
        self.display_level()
        self.draw_finish_line()

    def game_over(self):
        self.clear()
        self.sety(0)
        self.setx(0)

        self.write(arg="Game Over!", align="center", font=("Arial", 20, "normal"))

        self.sety(-20)
        self.write(arg=f"You have reached level: {self.game_level}", align="center",
                   font=("Arial", 20, "normal"))
        return
