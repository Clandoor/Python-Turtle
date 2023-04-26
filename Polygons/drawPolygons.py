ABSOLUTE_DEGREE = 360

from turtle import Turtle, Screen
import random

tinyTurtle = Turtle()
screen = Screen()

tinyTurtle.shape("turtle")
tinyTurtle.color("green")

# Edge outlines are set to black
tinyTurtle.pencolor("black")

"""
In order to pass the values in (r, g, b) format, a screen object must be created. And then, the color mode must be set. Thus, making it possible for the turtle pen to accept a tuple class object which contains a number ranging from 0 - 255.
Because there is more than one way of setting the color mode.
.pencolor() function accepts r, g and b values in a tuple format or string format.
"""

# Range is the starting polygon side to ending polygon size
for sides in range(3, 11):
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    screen.colormode(255)
    rgbTuple = (r, g, b)

    """Another approach would be store specific names inside a list and selecting a random value from that list, but at some point, we'll reach a limit, whereas in this methos, we have a wide spectrum of coming up with almost all possible colors.
    """
    tinyTurtle.pencolor(rgbTuple)
    for shape in range(sides):
        tinyTurtle.forward(75)
        turnAngle = ABSOLUTE_DEGREE / sides
        tinyTurtle.right(turnAngle)
