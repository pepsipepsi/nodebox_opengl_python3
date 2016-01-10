import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# A foliage generator!
# The foliage are actually green stars with random 
# inner and outer radii and a random number of points.
# They are skewed to make it look more random.

def draw(canvas):
    canvas.clear()

    translate(50,50)
    # By using HSB colormode, we can change the saturation and brightness
    # of the leaves to get more natural color variations.
    #colormode(HSB)

    # Generate a 50 x 50 grid. Each row and column is 12 points wide.
    for x, y in grid(18,14,30,30):
        push()
        fill(0.3,random(),random(0.2,0.6),0.8)
        #skew(random(-50,50),random(-50,50))
        star(x+random(2,5),y+random(2,5),random(1,10),random(1,40),15)
        pop()

canvas.size = 500,500
canvas.run(draw)