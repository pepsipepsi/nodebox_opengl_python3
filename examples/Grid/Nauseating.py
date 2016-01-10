import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Nauseating grid of circles.
# Each circle is randomly enlarged or shrinked a little bit,
# so it looks like a really blown up raster image.
# "What do you see?"

def draw(canvas):
    canvas.clear()
    # Create a grid of 20 by 20. Each row and column is 30 points.
    for x, y in grid(20,20,35,25):
        push()
        # Scale every element from 20% to 120% of its original size.
        scale(random(0.0,5.0))
        # Draw an oval that is a little bit smaller than the row and
        # column width.
        oval(x,y,30,30)
        pop()

canvas.size = 500,500
canvas.run(draw)