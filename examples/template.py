import os, sys
sys.path.insert(0, os.path.join(".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

def draw(canvas):
    canvas.clear()
    
canvas.size = 500, 500
canvas.run(draw)