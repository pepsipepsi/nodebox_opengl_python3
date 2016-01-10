import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Create interesting effects by using 
# appending transformations.

# All transformations in NodeBox are remembered.
# Every transformation you do is appended to the 
# previous ones. Here, the scale and rotation are 
# only changed a little bit, but by doing this multiple
# times, you will get full transformations.
# Also note that the actual position of the text is never
# changed: instead, it is modified by the transformations.

def draw(canvas):
    canvas.clear()

    # The first thing we do is move to the center of the screen.
    translate(300,300)
    for i in range(60):
        # The fill color is changed. Try using alpha transparency.
        fill((75-i)*0.01)
        # The imaged is scaled up. A random range from 1.0
        # (no scale) to 1.2 (20%  larger) is selected
        scale(random(1.0,1.2))
        # Rotate by a random value, from 0 to 10.
        rotate(random(10))
        # Use the loop counter as a text string. The loop will
        # go from 0 to 99. Try changing this in a fixed text
        # to see some interesting effects.
        text(str(i),0,0)

canvas.size = 500,500
canvas.run(draw)