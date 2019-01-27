#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont

# show image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

def createResults(resize_coeff_satisfied,resize_coeff_shocked,resize_coeff_neutral,resize_coeff_bored,backgroung_color):
	canvas = Image.new('RGB', (1024, 768), color = backgroung_color)
	yellow_text = (255, 255, 0)
	black_text = (0,0,0)
	#fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
	emoji_font = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf', 48)
	background= ImageDraw.Draw(canvas)

	resize_coeff_satisfied = resize_coeff_satisfied*2.0/100
	satisfied_png = Image.open('./emojies/satisfied.png', 'r')
	dimensions = satisfied_png.size
	new_dimensions = (int(math.floor(resize_coeff_satisfied*dimensions[0])), int(math.floor(resize_coeff_satisfied*dimensions[1])))
	if(new_dimensions[0]<30):
		new_dimensions = (30,30)
	satisfied_png = satisfied_png.resize(new_dimensions, Image.ANTIALIAS)
	satisfied_png_location = (160-int(math.floor(new_dimensions[0]/2)), 400-int(math.floor(new_dimensions[1]/2)))
	satisfied_location = (128-18,552) #256-18
	satisfied_text = str(resize_coeff_satisfied*50.0) # it was scalled x2, up to 200%, and then divided by 100

	resize_coeff_shocked = resize_coeff_shocked*2.0/100
	shocked_png = Image.open('./emojies/shocked.png', 'r')
	dimensions = shocked_png.size
	new_dimensions = (int(math.floor(resize_coeff_shocked*dimensions[0])), int(math.floor(resize_coeff_shocked*dimensions[1])))
	if(new_dimensions[0]<30):
		new_dimensions = (30,30)
	shocked_png = shocked_png.resize(new_dimensions, Image.ANTIALIAS)
	shocked_png_location = (225+160-int(math.floor(new_dimensions[0]/2)), 400-int(math.floor(new_dimensions[1]/2)))
	shocked_location = (384-2*18,552) #384-36
	shocked_text = str(resize_coeff_shocked*50.0)

	resize_coeff_neutral = resize_coeff_neutral*2.0/100
	neutral_png = Image.open('./emojies/neutral.png', 'r')
	dimensions = neutral_png.size
	new_dimensions = (int(math.floor(resize_coeff_neutral*dimensions[0])), int(math.floor(resize_coeff_neutral*dimensions[1])))
	if(new_dimensions[0]<30):
		new_dimensions = (30,30)
	neutral_png = neutral_png.resize(new_dimensions, Image.ANTIALIAS)
	neutral_png_location = (2*235+160-int(math.floor(new_dimensions[0]/2)), 400-int(math.floor(new_dimensions[1]/2)))
	neutral_location = (640-3*18,552) #640-54
	neutral_text = str(resize_coeff_neutral*50.0)

	resize_coeff_bored = resize_coeff_bored*2.0/100
	bored_png = Image.open('./emojies/bored.png', 'r')
	dimensions = bored_png.size
	new_dimensions = (int(math.floor(resize_coeff_bored*dimensions[0])), int(math.floor(resize_coeff_bored*dimensions[1])))
	if(new_dimensions[0]<30):
		new_dimensions = (30,30)
	bored_png = bored_png.resize(new_dimensions, Image.ANTIALIAS)
	bored_png_location = (3*235+160-int(math.floor(new_dimensions[0]/2)), 400-int(math.floor(new_dimensions[1]/2)))
	bored_location = (896-4*18,552) #896-72
	bored_text = str(resize_coeff_bored*50.0)

	canvas.paste(satisfied_png, satisfied_png_location)
	background.text(satisfied_location, satisfied_text, font=emoji_font, fill=black_text)

	canvas.paste(shocked_png, shocked_png_location)
	background.text(shocked_location, shocked_text, font=emoji_font, fill=black_text)

	canvas.paste(neutral_png, neutral_png_location)
	background.text(neutral_location, neutral_text, font=emoji_font, fill=black_text)

	canvas.paste(bored_png, bored_png_location)
	background.text(bored_location, bored_text, font=emoji_font, fill=black_text)
	 
	canvas.save('Result_Image.png')

green = (34,139,34)
black = (0,0,0)
orange = (255,165,0)
red = (255,0,0)
yellow = (255,255,0)

satisfied = 55
shocked = 5.4
neutral = 19
bored = 25.6

createResults(satisfied,shocked,neutral,bored, orange)
#output = Image.open("Result_Image.png")
#output.show()