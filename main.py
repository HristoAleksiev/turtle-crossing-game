from turtle import Turtle, Screen
from player import Player
from score import ScoreBoard
import time as t

s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
s.listen()

score = ScoreBoard()

player = Player()

game_over = False


def exit_game():
    global game_over
    game_over = True


while not game_over:
    s.update()
    s.onkeypress(exit_game, "e")
    s.onkeypress(player.move, "w")

s.bye()