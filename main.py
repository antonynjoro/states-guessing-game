import pandas
from turtle import Turtle, Screen

# Open the CSV file containing the states data
with open("50_states.csv") as states_file:
    states_data = pandas.read_csv(states_file)

# Import the Scoreboard class
from score_board import Scoreboard

# Import the screen dimensions
from constant_variables import SCREEN_HEIGHT, SCREEN_WIDTH

# Set font specifications for scoreboard
FONT_SPECIFICATIONS = ("Courier", 12, "normal")

# Create an instance of the Scoreboard class
scoreboard = Scoreboard()

# Create a turtle screen
screen = Screen()
# Set the screen dimensions
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# Set the background image
screen.bgpic("./blank_states_img.gif")

# Create a turtle object
pen = Turtle()
# Lift the turtle's pen so it doesn't draw
pen.penup()
# Hide the turtle
pen.hideturtle()
# Set the turtle's color to black
pen.color("black")

# Set the title of the screen
screen.title("States Game")

# Create an empty list to store the guessed states
guessed_states_list = []

# Set the game state to on
game_is_on = True

# Start the game loop
while game_is_on:
    # Update the scoreboard
    scoreboard.update_score()
    # Ask the user for a guess
    guess = screen.textinput("Guess a state", "Guess a state").title()

    # Check if the guess is "Exit"
    if guess == "Exit":
        game_is_on = False

    # Check if the guess is a valid state
    state_object = states_data[states_data.state == guess]
    if not state_object.empty:
        # If the guess is valid, move the turtle to the state's coordinates and write the state's name
        pen.goto(int(state_object.x), int(state_object.y))
        pen.write(state_object.state.item())
        # Clear the error message and update the scoreboard
        scoreboard.error_message = ""
        scoreboard.update_score()
        # Add the state to the list of guessed states
        guessed_states_list.append(guess)
    else:
        # If the guess is not a valid state, reduce the player's lives and display an error message
        scoreboard.reduce_life()
        scoreboard.error_message = f"{guess} is not a state. You lose a life"

    # Check if the player has run out of lives
    if scoreboard.lives < 1:
        # If the player has run out of lives, end the game
        scoreboard.game_over()
        game_is_on = False

# Create a list of states that were not guessed
unguessed_states = [state for state in states_data.state.to_list() if state not in guessed_states_list]

# Convert the list of unguessed states to a DataFrame
unguessed_states = pandas.DataFrame(unguessed_states)

# Save the unguessed states to a CSV file
unguessed_states.to_csv("states_to_learn.csv")
