from turtle import Turtle
from constant_variables import SCREEN_HEIGHT, SCREEN_WIDTH

TOP_LEFT = SCREEN_WIDTH/-2 +10, SCREEN_HEIGHT/2 -40

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 5
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(TOP_LEFT)
        self.error_message = ""


    def update_score(self):
        game_status_message = f"Lives: {self.lives} "+self.error_message
        self.clear()
        self.write(game_status_message, align="left", font=("Courier", 20, "normal"))

    def reduce_life(self):
        self.lives -= 1

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Courier", 32, "normal"))
        self.goto(0, -40)
        self.write(f"You are out of lives", align="center", font=("Courier", 24, "normal"))
