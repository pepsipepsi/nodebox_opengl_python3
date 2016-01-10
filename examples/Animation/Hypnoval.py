import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# A simple animation example.
# The hypnotating ovals use a little bit of math to
# make smooth animations, notably sinus and cosinus functions.
# NodeBox knows a script is an animation when it calls the "speed" method.
# Animation scripts always contain:
#  - a setup method that is run once, at the start of the animation
#  - a draw method that is run for every frame.
# Variables that you want to use in your script should be declared global.

# The setup method is called once, at the start of the animation.
# Here, it initializes the counter.

global cnt
cnt = 0.0

# The draw method is called for every frame.
# Here, it draws the oval grid.
def draw(canvas):
    canvas.clear()

    global cnt
    # We use an internal counter that modifies each
    # oval slightly
    s = 0.0
    # Move the canvas a bit.
    translate(130,80)
    # Draw a grid of 5 by 5.
    for x, y in grid(5,5,90,90):
        # Oscillate the fill color.
        fill(0, 0, sin(cnt+s*5.0)/2.0)
        # Draw the oval.
        oval(x + sin(cnt+s)*10.0, y + cos(cnt+s)*-6.0, 70.0, 60.0)
        # Increase the counter so that every oval looks a bit different.
        s += 0.05
    # Increase the global counter.
    cnt += 0.19

canvas.size = 500, 500
canvas.run(draw)