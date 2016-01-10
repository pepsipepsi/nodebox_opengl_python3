import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Generate compositions using predefined words.
def draw(canvas):
    canvas.clear()

    txt = [
           'DIE',
           'BUY',
           'WHY',
           'NOW',
           '!'
           ]

    font('Arial Black')

    # Define some colors.
    white = color(1,1,1)
    black = color(0,0,0)
    red = color(1,0,0)

    translate(0,-200)
    for i in range(100):
        # The next line isn't inside of the push-pops and therefore
        # the translate is appended every time. This might mean that
        # the composition goes off-screen. This also means that
        # it creates more interesting compositions.
        translate(random(-100,100),random(-100,100))
        # Save the current transformation. It's a good idea
        # to do this in the beginning of a loop. End the
        # loop with a pop.
        push()
        # Rotate in increments of 45 degrees.
        rotate(random(5)*45)
        fontsize(random(800))
        fill(choice((white,black,red)))
        someText = choice(txt)
        # One in two times, change the text to lowercase.
        if random(2) == 1:
            someText = someText.lower()
        text(someText, 0,0)
        pop()

canvas.size = 500,500
canvas.run(draw)