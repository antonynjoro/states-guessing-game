from turtle import Turtle
from constant_variables import SCREEN_HEIGHT, SCREEN_WIDTH

# Set the top-left coordinates of the scoreboard
TOP_LEFT = SCREEN_WIDTH/-2 +10, SCREEN_HEIGHT/2 -40

class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the parent class (Turtle)
        super().__init__()
        # Set the initial number of lives to 5
        self.lives = 5
        # Set the turtle's color to black
        self.color('black')
        # Lift the turtle's pen so it doesn't draw
        self.penup()
        # Hide the turtle
        self.hideturtle()
        # Move the turtle to the top-left corner of the screen
        self.goto(TOP_LEFT)
        # Initialize the error message to an empty string
        self.error_message = ""

    def update_score(self):
        # Create the message to display on the scoreboard
        game_status_message = f"Lives: {self.lives} "+self.error_message
        # Clear any previous message
        self.clear()
        # Write the new message on the scoreboard
        self.write(game_status_message, align="left", font=("Courier", 20, "normal"))

    def reduce_life(self):
        # Reduce the number of lives by 1
        self.lives -= 1

    def game_over(self):
        # Move the turtle to the center of the screen
        self.goto(0,0)
        # Write the "Game Over" message
        self.write(f"Game Over", align="center", font=("Courier", 32, "normal"))
        # Move the turtle down and write the "You are out of lives" message
        self.goto(0, -40)
        self.write(f"You are out of lives", align="center", font=("Courier", 24, "normal"))
