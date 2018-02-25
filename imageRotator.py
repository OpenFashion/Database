from PIL import Image
import random
import math

#GLOBALS
PERCENT = 0.01
RGB_PERCENT = 0.50

''' gets the average color from the left and right sides 
	@ params -
	  n = 0 top side of image, 1 = bottom side, -1 = error
	  image = input image
	@ return average value of rows
'''
def get_average_color_tb(n, image):
	width, height = image.size

	diff = int(height * PERCENT)

	# 0 = starting at top, 1 = starting at bottom
	if n==0:
		yval=0
	elif n==1:
		yval= int(height*(1-PERCENT))
	else:
		yval= -1

	xend = width

	r, g, b = 0, 0, 0
	count = 0

	#loop through edges and get the average color
	for s in range(0, xend):
		for t in range (yval, yval+diff):
			rgb_im = image.convert('RGB')

			pixlr, pixlg, pixlb = rgb_im.getpixel((s, t))
			r += pixlr
			g += pixlg
			b += pixlb
			count += 1

	return ( int (r/count), int (g/count), int (b/count))


''' gets the average color from the left and right sides 
	@ params -
	  n = 0 left side of image, 1 = right side, -1 = error
	  image = input image
	@ return average value of rows
'''
def get_average_color_lr(n, image):
	width, height = image.size

	diff = int(width * PERCENT)

# 
	if n==0:
		xval=0
	elif n==1:
		xval= int(width*(1-PERCENT))
	else:
		xval= -1

	yend = height

	r, g, b = 0, 0, 0
	count = 0

	# loop through left/right row and get the average color
	for s in range(0, yend):
		for t in range (xval, xval+diff):
			rgb_im = image.convert('RGB')

			pixlr, pixlg, pixlb = rgb_im.getpixel((t, s))
			r += pixlr
			g += pixlg
			b += pixlb
			count += 1

	return ( int(r/count), int (g/count), int (b/count))


#add random noise based on +/- RGB_PERCENT * average color
def add_noise(avg):
	randR = int(avg[0] + random.uniform(-1* RGB_PERCENT*avg[0], RGB_PERCENT*avg[0]))
	randG = int(avg[1] + random.uniform(-1* RGB_PERCENT*avg[1], RGB_PERCENT*avg[1]))
	randB = int(avg[2] + random.uniform(-1* RGB_PERCENT*avg[2], RGB_PERCENT*avg[2]))
	return (randR, randG, randB)


#returns average side color in top, right, bottom, left order
#clockwise from top
def getSideAvg(image):
	# each is a tuple of the RGB corresponding to the average pixel value of
	# each side: left right top bottom
	tColor = get_average_color_tb(0,image)
	bColor = get_average_color_tb(1,image)
	lColor = get_average_color_lr(0,image)
	rColor = get_average_color_lr(1,image)

	return (tColor, rColor, bColor, lColor)


# calls all other functions: rotates image, evaluates average pixel value 
# of each side and fills rotated image corners
# colors contains average RGB value in tuple, clockwise from top
def rotAndFill(image, angle, colors):
	angleRad = angle *3.14159 /180

	imWidth, imHeight = image.size
	rot = image.rotate(angle, expand=2)
	width, height = rot.size

	# each is a tuple of the RGB corresponding to the average pixel value of
	# each side: left right top bottom
	tColor = colors[0]
	rColor = colors[1]
	bColor = colors[2]
	lColor = colors[3]

	#,rColor,bColor,lColor = getSideAvg(image)
	

	#loads rotated image into array
	pix = rot.load()


	#calculates old image corners in new rotated image
	topXpoint = int(imWidth * math.cos(angleRad))
	bottomXpoint = int(imHeight * math.sin(angleRad))
	leftYpoint = int(imWidth * math.sin(angleRad))
	rightYpoint = int(imHeight * math.cos(angleRad))

	#filling in algorithm:
	# iterate through pixel values and if pixel is pureblack, change its value to 
	# filler value

	#top left corner
	for i in range(0,topXpoint):
		for j in range(0,	leftYpoint):
			# get r g b values from image
			r, g, b= rot.getpixel((i, j))

			if ((r,g,b) == (0,0,0)):
				pix[i,j] =  add_noise(tColor)


	#top right corner
	for i in range(topXpoint,width):
		for j in range(0,	rightYpoint):
			# get r g b values from image
			r, g, b= rot.getpixel((i, j))

			if ((r,g,b) == (0,0,0)):
				pix[i,j] =  add_noise(rColor)


	#bottom left corner
	for i in range(0,bottomXpoint):
		for j in range(leftYpoint,	height):
			# get r g b values from image
			r, g, b= rot.getpixel((i, j))

			if ((r,g,b) == (0,0,0)):
				pix[i,j] =  add_noise(lColor)


	#bottom right corner
	for i in range(bottomXpoint, width):
		for j in range(rightYpoint,	height):
			# get r g b values from image
			r, g, b= rot.getpixel((i, j))

			if ((r,g,b) == (0,0,0)):
				pix[i,j] =  add_noise(bColor)

	return rot

def outImages(image):

	colors = getSideAvg(image)

	maxsize = (500, 500)
	ang = -30
	flip = False
	ret =[]

	while ang<35:

		if ang<0:
			ang=-ang
			flip = True

		tn_image = im.thumbnail(maxsize, Image.ANTIALIAS)
		rot = rotAndFill(im, ang, colors)

		if flip:
			rot=rot.transpose(Image.FLIP_LEFT_RIGHT)
			ang = -ang

		ang+=5
		flip=False

		ret.append(rot)
	

	return ret


#TESTING
if __name__ == "__main__":
# 	im = Image.open("shirt.jpg")

# 	rot = outImages(im)

# 	rot[0].save("testNew.jpg")
