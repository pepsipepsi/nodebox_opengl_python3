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
myPath = textpath("VAPORIZE", x=40, y=200, fontname="Arial", fontsize=80, bold=True)

# Now that we have a BezierPath from the text we can use all sorts of math on it.
# Calculate a list of points (PathElement objects), evenly distributed along the path:

myPoints = list(myPath.points(1000))
n = 0

def draw(canvas):
    canvas.clear()
    fill(0.8, 0.0, 0.8, 1)

    for pt in myPoints:
        ellipse(pt.x, pt.y, 3, 3)
        # Each frame, adjust the position of the point a little bit.
        # Since we are not clearing the background,
        # it will appear as if something is growing from the text.

        # changed it to vaporize because not clearing the canvas makes it flash

        pt.x += random(-2.0, 2.0)
        pt.y += random(-2.0, 2.0)

canvas.fps  = 20
canvas.size = 500, 500
canvas.run(draw)