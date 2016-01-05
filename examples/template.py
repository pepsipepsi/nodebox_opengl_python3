from graphics import canvas
from graphics.context import *

def draw(canvas):
    canvas.clear()
    
canvas.size = 500, 500
canvas.run(draw)