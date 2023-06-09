from turtle import Turtle, Screen
import random


def turtle_initialization(turtles, colors, y_coordinate):
    """
    The following function places the instances of the turtles in their respective positions before starting
    the race.
    :param turtles: This is the list consisting of the turtles instances passed.
    :param colors: This is the list consisting of the colors instances passed.
    :param y_coordinate: Integer y_coordinate which separates turtles from each other in the plane.
    :return: None
    """

    for i, color in enumerate(colors):
        turtles[i].penup()
        turtles[i].color(colors[i])
        turtles[i].goto(x_index, y_coordinate)
        y_coordinate += 60


def turtles_run(turtle_list, user_input):
    """
    This function makes the turtles run by random steps.
    :param turtle_list: List of the turtle instances passed.
    :param user_input: User's choice of the color.
    :return: None
    """
    race_on = True
    while race_on:
        for turtle in turtle_list:
            if turtle.xcor() >= 220:
                race_on = False
                winning_color = turtle.pencolor()
                if user_input == winning_color:
                    print(f"Your {winning_color} turtle won! You now win $100.")
                else:
                    print(f"The winner is {winning_color} turtle!")
                    print(f"The {user_input} turtle you bet on lost :/")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


list_of_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list_of_turtles = []
x_index = -230
y_index = -140

screen = Screen()
screen.bgcolor("black")

# Setting up the aspect ratio of the screen.
screen.setup(width=500, height=400)

for index in range(0, 6):
    list_of_turtles.append(Turtle(shape="turtle"))

screen.textinput(title="List of Available Colors", prompt="Available Colors: Red, Orange, Yellow, Green, Blue and Purple. Click 'Ok' to continue")

# Converts the input in lower case for ease of comparing.
user_bet = screen.textinput(title="Make your bet now!", prompt="Enter the color of the turtle which would win: ").lower()

is_valid_input = True

if user_bet not in list_of_colors:
    is_valid_input = False
    print("Invalid color entered. Please try again.")
    screen.bye()

if is_valid_input:
    turtle_initialization(list_of_turtles, list_of_colors, y_index)
    turtles_run(list_of_turtles, user_bet)
    screen.exitonclick()
