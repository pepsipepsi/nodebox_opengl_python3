import os, sys
sys.path.insert(0, os.path.join("..",".."))

from nodebox.graphics.context import *
from nodebox.graphics import *

# This example allows you to draw lines on screen.
# It also transforms the line while you're drawing it.

# Each time you move the mouse, a new point is stored in a list of points.
# The draw method first transforms this list (to get a mutated line),
# then draws the points in this list. We use findpath to find a path
# "through" the list of points.

def setup():
    # px/py are the previous mouse coordinates. 
    global px, py
    px, py = 0, 0

    # pointlist is the list of points we created by moving the mouse.
    global pointlist
    pointlist = []

def draw(canvas):
    canvas.clear()

    global px, py
    global pointlist

    # For each frame, set the background color to a darkish blue.
    background(0.0, 0.0, 0.2)
    x, y = canvas.mouse.xy

    # Only draw a new point if the mouse has moved, which means the current mouse 
    # position is different from the previous one.
    # You can append "and mousedown" to the if statement to only draw points when
    # you hold down the mouse button. If you do, try clicking to get lines.
    if x != px and y != py:
        pointlist.append(Point(x, y))
        px, py = x, y

    print("pointlist : ", pointlist)
    # Set the correct color, a light blue.
    nofill()
    stroke(0.9, 0.9, 1.0)
    strokewidth(2)

    # This method actually transforms the points. We replace our current list of points
    # by the transformed version.
    # If you comment this line out, points won't be transformed, and you get a regular
    # line drawing program, but where's the fun in that?
    pointlist = transform_list(pointlist)

    # If there are points in the list...
    if len(pointlist) > 0:
        # ...draw them. We use the new findpath function to find a path
        # that goes through the list of points. The curvature defines
        # whether the path is rounded (1.0) or straight (0.0).
        # jf - findpath doesn't work that way

        #drawpath(findpath(pointlist, curvature=1.0))
        drawpath(findpath(pointlist, curvature=1.0))

    
def transform_point(pt, index, total_length):
    """This is the transformation function that gets applied to all points in the path.
    It returns either a new point, or None if the point needs to be deleted.
    Currently, it applies some sinus/cosinus functions to the point to make them curl
    and move offscreen."""
    # Add something to the x and y coordinates.
    # The formula (total_length - index), makes the influence on "older"
    # points (in the beginning of the list, with a low index) greater.
    pt.x += sin(index/50.0) * (total_length-index) / 100.0
    pt.y -= cos(index/100.0) * (total_length-index) / 100.0
    # If the point is offscreen, return None to indicate that we want the point deleted.
    if pt.x < 0 or pt.x > 500 or pt.y < 0 or pt.y > 500:
        return None
    return pt
    
def transform_list(pointlist, fn=transform_point):
    """This method transforms a list of points, and returns a new list. 
    For advanced users, you can specify the function that will be used to transform
    each point. You can copy/paste the transform_point function and try to make a
    new one yourself."""
    total_length = len(pointlist)
    # We make a new list because we are going to be deleting elements from the old list.
    # This messes up enumeration.
    newlist = []
    # Enumerate not only returns each point, but also its index, which the transform_point
    # method uses.
    for i, pt in enumerate(pointlist):
        # For each point, "apply" the method to get a new point. Note that we can specify
        # the method as a parameter (fn), which is a function.
        newpoint = fn(pt, i, total_length)
        # If the transformation method returns None, it means that the point can be
        # deleted. We don't actually delete the point, we just don't include it in
        # the new list.
        if newpoint is not None:
            newlist.append(newpoint)
    return newlist

setup()
canvas.size = 500,500
canvas.run(draw)