# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

# from moviepy_effetcs import *
from generate_sequence import *
from files_scanner import *
from text_tools import *

class VideoEditor():
	pass

def test():
	pass


# =======================================================================OUT====================================
exec_numb = 5
dur = []
textEffects = ["Blur", "Mirror", "BlackCircle", "Fractal", "DoubleFace", "Glitchface", ]

def randclip(maxclips):
	return random.randint(0, maxclips)

def cut_logic(exec_numb):
	clips = []
	print(clips)
	clipsList = files_scanner_video(path)
	imagesList = files_scanner_images(pathImages, 1)
	clipsCounter = len(clipsList) - 1
	imagesCounter = len(imagesList) - 1
	for i, objects in enumerate(clipsList[::1]):
		for j in range(0,3):
			clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, random.uniform(1, 4)))
			clips.append(imagesList[randclip(imagesCounter)])
			clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, random.uniform(1, 3)))
			clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
	for i, objects in enumerate(clips):
		pass
		if i % 3 == 0:
			clips[i] = supersample(clips[i], 1, 3)
	concat_and_write(clips, exec_numb)

def concat_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	try:
		clipOut = concatenate_videoclips(clips, method='compose')
		clipOut.write_videofile("./" + write_data + "-out.mp4",fps=25)
	except Exception as e:
		print(str(e))
		print("An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			cut_logic(exec_numb)
		else:
			print("game over")


cut_logic(exec_numb)