from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color("black")
        self.shape("turtle")
        self.shapesize(0.8)
        self.setheading(90)
        self.sety(-285)

    def move(self):
        self.forward(20)

    def check_collision(self, cars):
        for car in cars:
            if round(self.ycor() + 10 == car.ycor()) and round(self.xcor() + 10 == car.xcor() - 15):
                return True
