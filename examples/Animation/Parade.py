import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# The parade!
#
# This example shows object-oriented design in animation for
# defining a set of "actors" (the balls) that parade on stage.

# Import random and geometry functions
from random import seed

# Define our own circle method (NodeBox doesn't have one)
# that draws from the center.
def circle(x, y, size):
    oval(x-size/2, y-size/2, size, size)

# The main actor in the animation is a Ball. 
# A Ball has a set of state values: its position, size, color and delta-values.
# The delta-values affect the position and size, and are a simple way to give
# each ball "character". Higher delta-values make the ball more hectic.
class Ball:
    # Initialize a ball -- set all the values to their defaults.
    def __init__(self):
        self.x = random(500)
        self.y = random(500)
        self.size = random(10, 72)
        self.dx = self.dy = self.ds = 0.0
        self.color = color(random(), 1, random(0,2), random())

    # Update the internal state values.
    def update(self):
        self.dx = sin(canvas.frame/float(random(1,100))) * 20.0
        self.dy = cos(canvas.frame/float(random(1,100))) * 20.0
        self.ds = cos(canvas.frame/float(random(1,123))) * 10.0

    # Draw a ball: set the fill color first and draw a circle.
    def draw(self):
        fill(self.color)
        circle(self.x + self.dx, self.y + self.dy, self.size + self.ds)

# Initialize the animation by instantiating a list of balls.

global balls
balls = []
for i in range(30):
        balls.append(Ball())

# Draw the animation by updating and drawing each individual ball.
def draw(canvas):
    canvas.clear()

    global balls
    seed(1)
    # This translate command makes the ball move up on the screen.
    translate(0, 500-canvas.frame)
    for ball in balls:
        ball.update()
        ball.draw()

canvas.size = 500, 500 # Set the size of the canvas.
canvas.run(draw)       # Register the draw function and start the application.
