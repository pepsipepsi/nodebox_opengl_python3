import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Fun with stars! 

# Use the HSB color model to generate matching random colors.
#colormode(HSB)

def draw(canvas):
    canvas.clear()
    # This loop has no push and pop, meaning that every transformation
    # is appended to the previous ones.
    for y in range(100):
        fill(random(0.8,1),random(),random(0.2,0.6),random())
        rotate(random(-3,3))
        translate(random(-100,100), random(-100,100))
        star(300,300,random(1,100), random(1,5), random(1,500))

canvas.size = 500,500
canvas.run(draw)