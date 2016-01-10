import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# Avoider: the first NodeBox game!
# The purpose of the game is pretty simple: 
# try to avoid the red blobs for as long as possible.

# This example is a bit longer than the others, and features some geometry,
# object-oriented programming, and interactivity.

# You can change the size of the canvas to get a bigger or smaller playing field.

# The height of the bar at the bottom displaying the current time.
STATUS_BAR_HEIGHT = 12

# The import statement imports some import functions needed for geometry calculations
from math import pi, sqrt, sin, cos, asin, atan2

#old nodebox 1 import below - not sure if I should try to port that
#from nodebox.geo import angle, coordinates, distance
# The time import is used for calculating game time
import time

class Hero:
    """The hero of the game."""

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.speed = 5.0
        self.size = 5.0

    def show(self):
        fill(0, 0, 0)
        oval(self.x-self.size, self.y-self.size, self.size*2, self.size*2)

class Blob:
    """"The bad guys in the game. Avoid them!

    These are non-player characters, meaning they aren't controlled by the player directly.
    The update method contains their "brain"."""

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size = 5.0
        self.speed = random(0.5,0.8)
        self.seed = random()
        self.angle = 0.0

    def show(self):
        # This drawing code draws the circle body and the "eye".
        # To do this, we use a translation to move the blob's position,
        # then draw using relative coordinates.
        push()
        sz = self.size # We use size a lot in this method -- store it
        # Move to the center of the blob
        translate(self.x+sz, self.y+sz)
        scale(sz)
        # Rotate the blob. You won't see this when drawing the first oval,
        # since it's round, but it affects x and y coordinates, so the
        # eye will point in the right direction
        rotate(-self.angle)
        # Draw the body
        fill(1,0,0)
        oval(-1.0, -1.0, 2.0, 2.0)
        # Draw the eye
        fill(0, 0 ,0)
        oval(0.2, -0.5, 1.0, 1.0)
        pop()

def update(self, hero, blobs):
    # Increase and decrease the size based on the speed of the blob
    self.size = abs(sin(self.seed+FRAME/(5.0-self.speed*2.0)) * 2.0+self.seed) + 4.0
    # This code implements the chase behaviour of the blobs.
    # First, calculate the angle between ourselves and the hero
    self.angle = angle(self.x, self.y, hero.x, hero.y)
    # Then, move in that direction using the moving speed
    self.x, self.y = coordinates(self.x, self.y, self.speed, self.angle)
    # Calculate if I'm not bumping into another blob. If I am, calculate a new
    # jump to an empty spot on the board.
    for blob in blobs:
        if blob is not self and abs(distance(self.x, self.y, blob.x, blob.y)) < blob.size*2:
            self.x, self.y = random_spot_away_from_hero(hero)


def random_spot_away_from_hero(hero, mindist = 20.0):
    """Calculate a random spot that is at least mindist away from the hero."""
    dist = 0.0
    # We use a brute-force: while we have not found a good point, choose a random
    # point and calculate its distance. Rinse and repeat until a good point is found.
    while dist < mindist:
        x, y = random(500), random(500)
        dist = distance(x, y, hero.x, hero.y)
        return x, y

    # The setup of the game. This initializes the positions of the hero and the blobs,
    # sets the begintime and various other constants.
def setup():
    global hero, blobs, gameover, starttime, endtime
    hero = Hero(100, 100)
    blobs = []
    gameover = False
    endtime = None
    starttime = time.time()
    for i in range(10):
        x, y = random_spot_away_from_hero(hero)
        blobs.append(Blob(x, y))

# The main game loop
def draw(canvas):
    canvas.clear()
    global hero, blobs, gameover, starttime, endtime

    # To make things a little more interesting, we rotate and scale the canvas while
    # the game is running. For this to work, we need corner-mode transformations.
    transform(CORNER)
    # Move to the middle of the screen to set the rotation. This makes sure the rotation
    # isn't applied from a corner, but from the middle of the screen.
    translate(500/2, 500/2)
    # The rotation amount and speed is linked to the current FRAME. The farther in the game,
    # the faster and bigger the rotation gets
    rotate(sin(canvas.frame/70.0)*canvas.frame/10.0)
    # The speed of the saling is also linked to the current FRAME.
    scale(0.6 + abs(sin(FRAME/100.0)*0.4))
    # Move the canvas back. The rotation is now applied.
    translate(-500/2, -500/2)

    # Draw a rectangle, defining the playing field
    stroke(0)
    nofill()
    rect(0,0,500,500-STATUS_BAR_HEIGHT)
    nostroke()

    # The following functions apply when the game is not over,
    # in other words when we are still playing.
    if not gameover:
        # Check the keys and move the hero accordingly.
        # The min and max lines keep the hero within the bounds
        # of the playing field
        if keydown:
            if keycode == KEY_UP:
                hero.y -= hero.speed
                hero.y = max(hero.size, hero.y)
            if keycode == KEY_DOWN:
                hero.y += hero.speed
                hero.y = min(500-hero.size, hero.y)
            if keycode == KEY_LEFT:
                hero.x -= hero.speed
                hero.x = max(hero.size, hero.x)
            if keycode == KEY_RIGHT:
                hero.x += hero.speed
                hero.x = min(500-hero.size, hero.x)

        # Update the blobs. This part is the actual "intelligence" of the game.
        # This routine also calculates if one of the blobs hits your hero, in
        # which case the game is over.
        for blob in blobs:
            blob.update(hero, blobs)
            if abs(distance(hero.x, hero.y, blob.x, blob.y)) < blob.size + hero.size:
                gameover = True
                # The endtime stores how long we survived.
                endtime = time.time()

    # Draw everything. This is done even when the game is over.
    hero.show()
    for blob in blobs:
        blob.show()

    # The status indicators are drawn on-screen without all the funky rotations
    # and scaling. Reset the canvas.
    reset()

    # The time to display is either the endtime (on gameover), or the current time.
    if endtime is not None:
        t = endtime - starttime
    else:
        t = time.time()-starttime
    # Draw the time
    fontsize(12)
    fill(0,0.6)
    rect(0,500-STATUS_BAR_HEIGHT, 500, STATUS_BAR_HEIGHT)
    fill(1)
    text("%.2f seconds" % t, 5, 500-2)

    # If the game is over, scale up the hero to get a black screen
    # and draw the "GAME OVER" message
    if gameover:
        if hero.size < 500:
            hero.size += 30.0
        fill(1)
        text("GAME OVER", (500/2.0)-textwidth("game over")/2.0, 500/2)

setup()
canvas.size = 500,500
canvas.run(draw)