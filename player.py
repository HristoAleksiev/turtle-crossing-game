from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color("black")
        self.shape("turtle")
        self.shapesize(0.8)
        self.setheading(90)
        self.sety(-281)

    def move(self):
        self.forward(20)

    def check_collision(self, cars):
        for car in cars:
            print(self.position())
            print(car.position())

            if self.distance(car) < 19:
                return True
