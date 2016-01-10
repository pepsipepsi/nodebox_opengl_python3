import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Small example demonstrating how to display unicode text.

white = color(1,1,1,0.9)
red = color(1,0,0,0.9)
black = color(0,0,0,0.9)

def draw(canvas):
    canvas.clear()

    for i in range(20):
        # Choose a color from the list. This list is created on-the-fly,
        # and is actually a tuple (a non-editable list). Therefore,
        # the list itself is wrapped in brackets. The second brackets
        # surrounding it are for the choice command.
        fill(choice((white,red,black)))
        font("Arial Bold")
        fontsize(random(600))

        # The TradeMark, Registered and Copyright signs are
        # Unicode characters. You should prefix the string with
        # a 'u', for Unicode.
        text(u"™", random(500),random(400))
        text(u"®", random(500),random(400))
        text(u"©", random(500),random(400))

canvas.size = 500,500
canvas.run(draw)