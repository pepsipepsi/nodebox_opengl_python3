import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Demonstrates some uses of the image command.

# There are several ways to scale an image, 
# but by far the easiest is to provide a width
# parameter, such as here.

def draw(canvas):
    canvas.clear()

    for x, y in grid(8, 8, 50, 50):
        image("nodeboxicon.png", x, y, width=50)

    # Overlay the grid of images with an alpha-transparent
    # rectangle.
    fill(0.1, 0.1, 0.75, 0.8)
    rect(0, 0, 500, 500)

    # Show the main image.
    image("nodeboxicon.png", 100, 100)

    # Show the text below the image
    font("Georgia Bold", 39)
    fill(1, 1, 1)
    # We use center-alignment so we can change the
    # text without impacting its placement.
    # Note that for this to work, we need to give
    # a width as parameter for the text command.
    align(CENTER)
    text("NodeBox", 0, 345, width=400)

canvas.size = 500,500
canvas.run(draw)