import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Automatically generates text based on the Kant Generator Pro.
# The Kant Generator Pro is an example script of the
# "Dive Into Python" manual.

# Generate automatic text from an XML file and store it as a string
# in the txt variable. Also try the "thanks.xml", which generates
# "thank you" notes, and "insults.xml", which generates all sorts
# of crazy insults.

def draw(canvas):
    canvas.clear()

    txt = autotext("kant.xml")

    font("Times", 12)
    lineheight(1.7)

    text(txt, 25, 30, width=320, height=950)

canvas.size = 500,500
canvas.run(draw)