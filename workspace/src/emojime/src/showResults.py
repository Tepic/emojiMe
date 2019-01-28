#!/usr/bin/env python

import os
from PIL import Image, ImageDraw, ImageFont

# show image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

import numpy as np
import cv2

import threading
import time

global satisfied
global shocked
global neutral
global bored
global stopFlag
	
satisfied = 25
shocked   = 25
neutral   = 25
bored     = 25
stopFlag = False

def getColor(percentages):
	satisfied = percentages[0]

	ordered = [percentages[0], percentages[1], percentages[2], percentages[3]]

	ordered.sort()
	value_1 = ordered[3] # MAX
	value_2 = ordered[2]
	value_3 = ordered[1]
	value_4 = ordered[0] # MIN

	if(value_1==satisfied):
		if(value_1>=2*value_2):
			return green
		if(value_1>=1.5*value_2):
			return yellow
		if(value_1>value_2):
			return orange
	else:
		return red

def createResults(percentages):
	resize_coeff_satisfied = percentages[0]
	resize_coeff_shocked   = percentages[1]
	resize_coeff_neutral   = percentages[2]
	resize_coeff_bored     = percentages[3]

	background_color = getColor(percentages)
	canvas = Image.new('RGB', (1024, 768), color = background_color)
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

	canvas.paste(satisfied_png, satisfied_png_location,satisfied_png)
	background.text(satisfied_location, satisfied_text, font=emoji_font, fill=black_text)

	canvas.paste(shocked_png, shocked_png_location,shocked_png)
	background.text(shocked_location, shocked_text, font=emoji_font, fill=black_text)

	canvas.paste(neutral_png, neutral_png_location,neutral_png)
	background.text(neutral_location, neutral_text, font=emoji_font, fill=black_text)

	canvas.paste(bored_png, bored_png_location,bored_png)
	background.text(bored_location, bored_text, font=emoji_font, fill=black_text)
	 
	canvas.save('Result_Image.png')
	canvas.close()

def getNewResults():
	global satisfied
	global shocked
	global neutral
	global bored
	global stopFlag
	global percentages
    
	while(True):
		satisfied = float(raw_input("Satisfied: "))
		shocked   = float(raw_input("Shocked: "))
		neutral   = float(raw_input("Neutral: "))
		bored     = float(raw_input("Bored: "))
		percentages = [satisfied,shocked,neutral,bored]
		if(raw_input("Do you want to terminate? ")=='yes'):
			stopFlag = True
			break
	

green = (34,139,34)
yellow = (255,255,0)
orange = (255,165,0)
red = (255,0,0)
black = (0,0,0)

percentages = [satisfied,shocked,neutral,bored]
# createResults(percentages)

input_thread = threading.Thread(target=getNewResults)
input_thread.start()

pressed = 0
while(not stopFlag):#pressed!=101): # press e for exit

	#percentages = [satisfied,shocked,neutral,bored]

	createResults(percentages)
	output = cv2.imread("Result_Image.png")
	cv2.imshow('Results',output)
	cv2.waitKey(1000)
	#pressed = cv2.waitKey(0) & 0xFF