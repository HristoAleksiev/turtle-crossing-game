from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INITIAL_SPEED = 35
SPEED_INCREMENT = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()

        self.car_speed = INITIAL_SPEED
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(COLORS[r.randint(0, len(COLORS) - 1)])

    def move(self):
        self.forward(self.car_speed)

    def get_speed(self):
        return self.car_speed

    def accelerate(self):
        self.car_speed += SPEED_INCREMENT
