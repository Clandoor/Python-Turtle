"""
Below code is the example of how to get the colors based on their most occurring frequency of them in an image. Make sure that image is stored in the same location with the same name.
1. Make sure PIP version is updated.
2. Install colorgram module 'pip install colorgram.py'.
3. Import it.
"""

"""
import colorgram

rgb_colors = []

# Extracts 30 colors from the image we provided as the argument and returns a list
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    newColor = (r, g, b)
    rgb_colors.append(newColor)

print(rgb_colors)
"""


"""
Copying the color list printed on the output and storing it manually as other list.
"""




"""
Code Specifications: 
1. 10 dots on each row and column.
2. Dot size should be 20 units each only.
3. Dots should be separated by 50 units each. 
"""



import random
from turtle import Turtle, Screen

ROWS = 10
COLUMNS = 10


def paintHirthPainting():
    # Manually setting the coordinates first so it fits my screen appropriately.
    x = -230.00
    y = -250.00

    """ Pen up because we don't want a straight line when the position of cursor instantly changes from the initial position to given values of the coordinates.
    """
    tinyTurtle.penup()

    for row in range(ROWS):
        """Setting the position manually so cursor moves directly to the desired location for better visibility for me. Morever, we need the cursor on the top previously created row to start the new row, so our x coordinate will remain unchanged while we will increment the y coordinate value by 50 units so it can start a new row from there. 
        """
        tinyTurtle.setposition(x, y)
        for column in range(COLUMNS):
            tinyTurtle.color(random.choice(colorList))
            tinyTurtle.dot(20)
            tinyTurtle.forward(50)

        # Incrementing the value of y coordinate by 50 units so cursor can start a new row.
        y += 50


colorList = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tinyTurtle = Turtle()

# Hiding the Cursor for the better.
tinyTurtle.hideturtle()
screen = Screen()

# So we can use rgb color codes without any issues.
screen.colormode(255)

tinyTurtle.speed("fastest")

paintHirthPainting()
screen.exitonclick()






"""
Another Approach:
tinyTurtle.penup()
Inside the Nested For Loop, just add the following statements
    
    tinyTurtle.color(random.choice(colorList))

    # Since pen was up, we need it back down so circles are visible.
    tinyTurtle.pendown()
    
    # Starts to fill the color.
    tinyTurtle.begin_fill()
    
    # Draw the Circle with the radius of 10.
    tinyTurtle.circle(10)
    
    # Pen back up as we are done drawing the circle
    tinyTurtle.penup()
    
    # Now we can end the fill safely and as a result, the shape will be filled with color.
    tinyTurtle.end_fill()
    tinyTurtle.forward(50)
"""
