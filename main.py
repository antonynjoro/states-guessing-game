import pandas
from turtle import Turtle, Screen

with open("50_states.csv") as states_file:
    states_data = pandas.read_csv(states_file)

from score_board import Scoreboard

from constant_variables import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_SPECIFICATIONS = ("Courier", 12, "normal")

scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgpic("./blank_states_img.gif")

pen = Turtle()
pen.penup()
pen.hideturtle()
pen.color("black")

screen.title("States Game")

guessed_states_list = []

game_is_on = True

while game_is_on:
    scoreboard.update_score()
    guess = screen.textinput("Guess a state", "Guess a state").title()

    # print(states_data.state[states_data.state == "Alabama"])

    state_object = states_data[states_data.state == guess]
    # print(state_object)

    if guess == "Exit":
        game_is_on = False

    if not state_object.empty:
        pen.goto(int(state_object.x), int(state_object.y))
        pen.write(state_object.state.item())
        scoreboard.error_message = ""
        scoreboard.update_score()
        guessed_states_list.append(guess)




    else:
        scoreboard.reduce_life()
        scoreboard.error_message = f"{guess} is not a state. You lose a life"

    if scoreboard.lives < 1:
        scoreboard.game_over()
        game_is_on = False

unguessed_states = [state for state in states_data.state.to_list() if state not in guessed_states_list]


unguessed_states = pandas.DataFrame(unguessed_states)

unguessed_states.to_csv("states_to_learn.csv")

