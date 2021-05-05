from turtle import Turtle, Screen
import random as r

MIN_LANES = 1
MAX_LANES = 24
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INITIAL_SPEED = 15
SPEED_INCREMENT = 10


class CarSpawner:
    def __init__(self):
        self.cars_collection = []
        self.s = Screen()

    def create_car(self):
        if r.randint(1, 6) == 5:
            car = Turtle()

            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.color(COLORS[r.randint(0, len(COLORS) - 1)])

            car.setx(300)
            car.sety(-260 + (20 * r.randint(MIN_LANES, MAX_LANES)))
            car.setheading(180)

            self.cars_collection.append(car)
            self.destroy_cars()

    def move_cars(self):
        for car in self.cars_collection:
            car.forward(INITIAL_SPEED)

    def destroy_cars(self):
        for car in self.cars_collection:
            if car.xcor() < -300:
                car.hideturtle()
                self.cars_collection.remove(car)
