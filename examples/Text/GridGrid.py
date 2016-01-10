import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Draw a grid of grids.

# Use corner transformations to rotate objects from the top-left corner,
# instead of from the center of an object (which is the default).

def draw(canvas):
    canvas.clear()
    transform(CORNER)

    font('Gill Sans', 72)

    for i in range(600):
        # At the beginning of the loop, push the current transformation.
        # This means that each loop begins with a "clean slate".
        push()
        # Fills aren't remembered using push/pop, only transformations.
        fill(random(),0,0,0.5)
        # Use this way of translation to put objects on a grid.
        # NodeBox also has a grid function: see the examples in Examples/Grid
        translate(random(1,10)*50, random(1,10)*50)
        rotate(random(360))
        scale(random(1.8))
        # Change this text for other interesting results.
        text('#', 0, 0)
        pop()

canvas.size = 500,500
canvas.run(draw)