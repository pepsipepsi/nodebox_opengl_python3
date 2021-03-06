#rom nodebox.graphics         import shader
from nodebox.graphics         import physics
from nodebox.graphics.context import Text
from nodebox.graphics.context import Canvas
from nodebox.graphics.noise   import noise
from nodebox.graphics.context import line
from nodebox.graphics.context import ellipse

physics.line    = line
physics.ellipse = ellipse
physics.Text    = Text

#-----------------------------------------------------------------------------------------------------
# Expose the canvas and some common canvas properties on global level.
# Some magic constants from NodeBox are commands here:
# - WIDTH  => width()
# - HEIGHT => height()
# - FRAME  => frame()

canvas = Canvas()

def size(width=None, height=None):
    if width is not None:
        canvas.width = width
    if height is not None:
        canvas.height = height
    return canvas.size

def speed(fps=None):
    if fps is not None:
        canvas.fps = fps
    return canvas.fps

def frame():
    return canvas.frame
    
def clear():
    canvas.clear()
