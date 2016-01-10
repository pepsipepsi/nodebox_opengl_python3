import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Cover generator

# The HSB color mode is the big trick here. We use it to generate
# a random hue with a fixed brightness and saturation. That way,
# we can use all kinds of different colors that automatically fit
# together.
#colormode(HSB)

def draw(canvas):
    canvas.clear()
    # Set a random background color
    fill(random(),0.5,0.5)
    rect(0,0,500,500)

    # Draw 10 rectangles on top of each other, each with a different color,
    # and a random starting position and height.
    for i in range(10):
        fill(random(),0.5,0.5)
        rect(0,random(-200,500+200),500,random(-200,500+200))

    # Draw the text.
    fill(1,0,1)
    scale(8)
    text("*",500-50,50)
    reset()
    text("NODEBOX",10,500-30)
    fontsize(13.5)
    fill(1,0,1,0.4)
    text("AUTUMN | WINTER 2007",10,500-18)

canvas.size = 500,500
canvas.run(draw)