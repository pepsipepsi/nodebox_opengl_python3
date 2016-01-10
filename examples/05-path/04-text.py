import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# The classic NodeBox for Mac OS X has an interesting textpath() function
# that transforms a string into a BezierPath.
# This function is partly emulated in NodeBox for OpenGL, as long as
# you stick with the default fonts (Droid Sans, Droid Sans Mono, Droid Serif).
# Note: there is a way to make more fonts available - see nodebox/font/glyph.py,
# relying on the classic NodeBox to do the calculations.
myPath = textpath("GROW", x=40, y=200, fontname="Arial", fontsize=100, bold=True)
myPath2 = textpath("GROW", x=40, y=200, fontname="Arial", fontsize=100, bold=True)

# in python 2 it's necessary to convert this set to a list in order to iterate over it, not in python 3. You can just iterate over the set

# Now that we have a BezierPath from the text we can use all sorts of math on it.
# Calculate a list of points (PathElement objects), evenly distributed along the path:

def draw(canvas):
    #canvas.clear()
    fill(0.2, 0.5, 0, 1)
    drawpath(myPath2)

    for pt in myPath:
        ellipse(pt.x, pt.y, 2, 2)
        # Each frame, adjust the position of the point a little bit.
        # Since we are not clearing the background,
        # it will appear as if something is growing from the text.

        pt.x += random(-1.0, 1.0)
        pt.y += random(-1.0, 1.0)

canvas.fps  = 20
canvas.size = 500, 500
canvas.run(draw)