import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Create organic balls using text.

def draw(canvas):
    canvas.clear()
    font('Zapfino')
    fontsize(72)

    # Draw a black background. Setting the background to None
    # gives an empty background.
    background(0)

    # Move to the center of the composition. Note that, because
    # we use Zapfino, the ball will end up off-center.
    translate(500/2,500/2)
    for i in range(100):
        # The trick is skewing, rotating and scaling without
        # moving so all elements share the same centerpoint.
        push()
        # Select a value between (0,0,0) (black) and (1,0,0) (red).
        fill(random(),0,0)
        rotate(random(0,800))
        scale(random()*2)
        #skew(random(200),random(200))
        text('(',0,0)
        pop()

canvas.size = 500,500
canvas.run(draw)