from turtle import Turtle, Screen
import random

tinyTurtle = Turtle()
screen = Screen()

# Sets the speed to fastest mode
tinyTurtle.speed("fastest")
tinyTurtle.pensize(10)

# Random change in direction
angle = [0, 90, 180, 270]

for moves in range(300):
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    screen.colormode(255)
    
    # Because pencolor accepts data in form of the tuple.
    rgbTuple = (r, g, b)

    tinyTurtle.pencolor(rgbTuple)
    randomTilt = random.choice(angle)
    tinyTurtle.forward(20)

    # Sets the orientation of the turtle to certain angle.
    tinyTurtle.setheading(randomTilt)


# If you want the screen to collapse after the program, comment the below line.
screen.exitonclick()
