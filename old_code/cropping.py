# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

from generate_sequence import *
from files_scanner import *

class VideoEditor():
	pass

def test():
	pass

def rand_cropper(clip, count, size):
	clipSize = clip.size
	cropCoords = []
	for i in range(0, count*4):
		cropCoords.append(random.randint(0, clipSize[0]))
		cropCoords.append(random.randint(0, clipSize[1]))
	for j in range(0, len(cropCoords), 4):
		croppedClip = crop(clip, x1=j-3, y1=j-2, x2=j-1, y2=j)
	return croppedClip




# =======================================================================OUT====================================
path = '../shaker/'
clip = files_scanner(path)[0]
# print(random.randint(0, clip.size[0]))
cropped = rand_cropper(clip, 200, 10)
# print(clip.size)
# croppedClip = crop(clip, x1=10, width=10)
clip.set_pos((45,150))
write_data = time.strftime("%I%M%S")
video = CompositeVideoClip([files_scanner(path)[0],files_scanner(path)[1],files_scanner(path)[2]], size=(720,460))
# clipOut = concatenate_videoclips(clips, method='compose')
clipOut = cropped
clipOut.write_videofile("./" + write_data + "-out.mp4",fps=25)

'''
# Написать хуйню, которая вырезает несколько кусков из видеофайла.
	- 
'''