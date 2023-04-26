ABSOLUTE_ROTATIONS = 360

from turtle import Turtle, Screen
import random

def setRandomColor():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rgb = (r, g, b)
    return rgb


def drawSpirograph(angle):
    rotations = int(ABSOLUTE_ROTATIONS / angle)
    for _ in range(rotations):
        tinyTurtle.pencolor(setRandomColor())
        
        # Draws a circle of radius 100 units.
        tinyTurtle.circle(100)

        """ heading() will yield the current angle the cursor is pointing at, then wechange it so cursor points to diffent angle there by starting a new circle from             that new angle.
        """
        tinyTurtle.setheading(tinyTurtle.heading() + angle)


tinyTurtle = Turtle()
screen = Screen()

screen.colormode(255)
tinyTurtle.speed(0)

drawSpirograph(5)

screen.exitonclick()
