from turtle import Turtle, Screen
from car import Car
import random as r

MIN_LANES = 1
MAX_LANES = 24


class CarSpawner:
    def __init__(self):
        self.cars_collection = []
        self.s = Screen()

    def create_car(self):
        if r.randint(1, 6) == 1:
            car = Car()

            car.setx(300)
            car.sety(-260 + (20 * r.randint(MIN_LANES, MAX_LANES)))
            car.setheading(180)

            self.cars_collection.append(car)
            self.destroy_cars()

    def move_cars(self):
        for car in self.cars_collection:
            car.move()

    def destroy_cars(self):
        for car in self.cars_collection:
            if car.xcor() < -300:
                car.hideturtle()
                self.cars_collection.remove(car)

    def increase_speed(self):
        for car in self.cars_collection:
            car.accelerate()
