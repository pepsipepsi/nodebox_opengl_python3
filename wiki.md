--coordinates 0, 0 are in lower left corner of window 

# primitives

	line(begin x, begin y, end x, end y)  
	rect(lower left x, lower left y, width, height)  
	ellipse(center x, center y, width, height)  
	triangle(point 1 x, point 1 y, point 2 x, point 2 y, point 3 x, point 3 y)  

# color commands

0 - 1 decimal value

	fill(red,green,blue,alpha)  
	fill(black,alpha)  
	stroke(red,green,blue,alpha)  

	strokewidth()  
--int value 1 - 5

# transform commands

	translate(distance right, distance up)  
	rotate()  
--positive clockwise  
	scale()  
--0 - 1 decimal = shrink  
--more than 1 = grow
	push()  
	pop()  

# bezier commands

	beginpath()  
	endpath()  

	moveto(origin x, origin y)  
	curveto(point 1 x, point 1 y, point 2 x, point 2 y, point 3 x, point 3 y)  

	lineto(destination x, destination y)  

	drawpath()  

--using beginpath/endpath  

	beginpath(0, 0)  
	curveto(50, 50, 0, 150, 0, 200)  
	curveto(0, 150, -50, 50, 0, 0)  
	endpath()  

--there are some interesting methods that are exposed when creating a BezierPath instead of using the beginpath/endpath methods  

--using moveto and drawpath  

	leaf = BezierPath()  
	leaf.moveto(0, 0)  
	leaf.curveto(50, 50, 0, 150, 0, 200)  
	leaf.curveto(0, 150, -50, 50, 0, 0)  
	drawpath(leaf)  

--interesting color gradient  

	beginclip(leaf)  
	colorplane(-75, 0, 150, 200,
	    color(r,g,b,a), # Gradient top color.  
	    color(r,g,b,a)  # Gradient bottom color.  
	)  
	endclip()  

--getting a generator representing points along a BezierPath  

	BezierPath.points(int how many points you want)  

	leaf = BezierPath()  
	leaf.moveto(0, 0)  
	leaf.curveto(50, 50, 0, 150, 0, 200)  
	leaf.curveto(0, 150, -50, 50, 0, 0)  

	for i in leaf.points(5):  
		print("a point : ", i)  

--returns line below 5 times  

	DynamicPathElement(cmd='curveto', x=7.0, y=154.7, ctrl1=(18.8, 103.1), ctrl2=(3.1, 171.9))  

# canvas/mouse control

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

# math

	sin()  
	cos()  
	abs()  
--absolute value  
	grid(how many x, how many y)  
	noise()  
--returns smoothed 0-1 decimal value simulating perlin noise  

# easing

	smoothstep(bottom, top, rate)  

# image commands

--load file

	Image("filename")  
--jpeg, png, tiff  
	image(Image("filename"), x, y)  
	image(Image("filename"), x, y, (red, green, blue), alpha)  
--coords are of lower left corner  
	crop()  

# image filters 

when filter is applied it overrides color/alpha property  

	invert()  
	colorize()  
	blur()  
	desaturate()  
	mask()  
	blend()  
	distort()  
	twirl()  
	bump()  

--the stuff below isn't working because shader.py has some issues  

	inverted(), colorized(), blurred(), desaturated(), masked(), blended() and distorted() can be passed to the "filter" parameter of an image() command  

--image quad  

--bend the image  

	img.quad.dx1 =  200  
	img.quad.dy1 =  100  
	img.quad.dx2 =  100  
	img.quad.dy2 = -100  

--get pixels from image to convert it to an iterable palette  

	Pixels(img)  

--example  

	image(img, 50, 50, filter=distorted(STRETCH, dx=canvas.mouse.relative_x, dy=canvas.mouse.relative_y))  

# text commands

	text("text string", int size of font)  

--load text and font  

	textObject = Text("text string", font="Droid Serif", fontsize=20, fontweight=BOLD)  

--styling  

	textObject.style("text string",font = "Droid Serif",  
		fontsize = 20,  
		fontweight = BOLD,  
		lineheight = 1.2,
		fill = color(0.25)))  

	font()  
	fontsize()  

TODO  

filter descriptions  
physics  
layers  

etc  