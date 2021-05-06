from turtle import Screen
from player import Player
from score import ScoreBoard
from cars_spawner import CarSpawner
import time as t

s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
s.listen()

score = ScoreBoard()
player = Player()
car = CarSpawner()

game_over = False


def exit_game():
    global game_over
    game_over = True


while not game_over:
    s.update()

    s.onkeypress(exit_game, "e")
    s.onkeypress(player.move, "w")

    car.create_car()
    car.move_cars()

    if player.check_collision(car.cars_collection) == "Crashed":
        exit_game()
    elif player.check_collision(car.cars_collection) == "Level":
        score.level_up()
        player.reset_position()
        car.increase_speed()

    t.sleep(0.1)

s.bye()
