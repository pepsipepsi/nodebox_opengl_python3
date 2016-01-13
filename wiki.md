# Basics  

The first line imports os and sys modules and the second line is telling python where the nodebox libraries are. The examples are in a subfolders of the examples folder, so the first lines...  

	import os, sys  
	sys.path.insert(0, os.path.join("..",".."))

is telling the python that the nodebox libraries are back two directories from the location of the file being run.  

Now that python knows where to look, import the basic libraries you're going to use. At a minimum, include the following two imports.  

	from nodebox.graphics.context import *  
	from nodebox.graphics import *  

You will need additional imports for various libraries used in your scripts. Check the examples to see which ones belong with which methods.  

Every script you create will need the following: a "draw(canvas)" function which will be invoked repeatedly as the program runs, and a "canvas.run(draw)" statement which takes care of the window. There's nothing special about the word draw, you could call it anything.  


	def draw(canvas):  
		# code goes here  

	canvas.size = 500,500  
	canvas.run(draw)  

Whatever you put in the draw method will be called over and over as the program runs. You could run the program with just what is there so far and you would see an empty window 500 x 500 pixels. Put some of the methods below into the draw function to get started...  

note: coordinates 0, 0 are in lower left corner of window  

# Colors  

0 - 1 decimal value

	fill(red, green, blue, alpha)  
	fill(black, alpha)  
	stroke(red, green, blue, alpha)  

optional colorspace parameter to switch to Hue, Saturation, Brightness mode  

	stroke(red, green, blue, alpha, colorspace=HSB)  
	strokewidth()  

int value 1 - 5

# Primitives  

	line(begin x, begin y, end x, end y)  
	rect(lower left x, lower left y, width, height)  
	ellipse(center x, center y, width, height)  
	triangle(point 1 x, point 1 y, point 2 x, point 2 y, point 3 x, point 3 y)  

# Transform  

	translate(distance right, distance up)  
	rotate()  

positive clockwise  

	scale()  

0 - 1 decimal = shrink  
more than 1 = grow  

	push()  
	pop()  

# Bezier Curves  

	beginpath()  
	endpath()  

	moveto(origin x, origin y)  
	curveto(point 1 x, point 1 y, point 2 x, point 2 y, point 3 x, point 3 y)  

	lineto(destination x, destination y)  

	drawpath()  

using beginpath/endpath  

	beginpath(0, 0)  
	curveto(50, 50, 0, 150, 0, 200)  
	curveto(0, 150, -50, 50, 0, 0)  
	endpath()  

there are some interesting methods that are exposed when creating a BezierPath instead of using the beginpath/endpath methods  

using moveto and drawpath  

	leaf = BezierPath()  
	leaf.moveto(0, 0)  
	leaf.curveto(50, 50, 0, 150, 0, 200)  
	leaf.curveto(0, 150, -50, 50, 0, 0)  
	drawpath(leaf)  

interesting color gradient  

	beginclip(leaf)  
	colorplane(-75, 0, 150, 200,
	    color(r,g,b,a), # Gradient top color.  
	    color(r,g,b,a)  # Gradient bottom color.  
	)  
	endclip()  

getting a generator representing points along a BezierPath  

	BezierPath.points(int how many points you want)  

	leaf = BezierPath()  
	leaf.moveto(0, 0)  
	leaf.curveto(50, 50, 0, 150, 0, 200)  
	leaf.curveto(0, 150, -50, 50, 0, 0)  

	for i in leaf.points(5):  
		print("a point : ", i)  

returns line below 5 times  

	DynamicPathElement(cmd='curveto', x=7.0, y=154.7, ctrl1=(18.8, 103.1), ctrl2=(3.1, 171.9))  

# Canvas/Mouse/Keyboard Control

	canvas.size  
	canvas.run()  
	canvas.clear()  
	canvas.frame  
	canvas.mouse.x  
	canvas.mouse.y  
	canvas.mouse.dx  
	canvas.mouse.dy  
	canvas.mouse.button (LEFT | MIDDLE | RIGHT | None)  
	canvas.mouse.modifiers (CTRL | SHIFT | ALT)  
	canvas.mouse.pressed  
	canvas.mouse.dragged  

        key = canvas.keys  

        if key.pressed:  
            if key.code == UP:  
                xPostion += 1
            if key.code == DOWN:    
                xPostion -= 1  

# Math

	sin()  
	cos()  
	abs()  

	grid(howManyX, howManyY)  
	noise()  

returns smoothed 0-1 decimal value simulating perlin noise  

	smoothstep(bottom, top, rate)  

easing

# Physics

--placeholder  

# Images  

to load a file

	Image("filename")  

jpeg, png, tiff  

	image(Image("filename"), x, y)  
	image(Image("filename"), x, y, (red, green, blue), alpha)  

coords are of lower left corner of the image file  

	crop()  

# Image Filters 

image quad (bend the image)    

	img.quad.dx1 =  200  
	img.quad.dy1 =  100  
	img.quad.dx2 =  100  
	img.quad.dy2 = -100  

get pixels from image to convert it to an iterable palette  

	Pixels(img)  

example  

	image(img, 50, 50, filter=distorted(STRETCH, dx=canvas.mouse.relative_x, dy=canvas.mouse.relative_y))  


when filter is applied it overrides color/alpha property  

Note: The filters aren't working because shader.py seems to have some issues  

	invert()  
	colorize()  
	blur()  
	desaturate()  
	mask()  
	blend()  
	distort()  
	twirl()  
	bump()  

# Text  

	text("text string", int size of font)  

load text and font  

	textObject = Text("text string", font="Droid Serif", fontsize=20, fontweight=BOLD)  

styling  

	textObject.style("text string",font = "Droid Serif",  
		fontsize = 20,  
		fontweight = BOLD,  
		lineheight = 1.2,
		fill = color(0.25)))  

	font()  
	fontsize()  

# Layers and Dragging  

--placeholder

# Graphical User Interface Elements

--placeholder  

# Graph  

--placeholder