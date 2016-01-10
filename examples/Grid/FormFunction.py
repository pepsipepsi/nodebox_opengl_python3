import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

def draw(canvas):
    canvas.clear()
    for x, y in grid(30,30,20,20):
        if random() > 0.6:
            # Here, we choose between two functions: oval and rect.
            # The chosen function is stored in the 'form' variable, which
            # is then called on the next line. Note that both functions
            # should have the same parameters, and in the same order.
            form = choice((oval, rect))
            form(x, y, 18,18)

canvas.size = 500, 500
canvas.run(draw)
