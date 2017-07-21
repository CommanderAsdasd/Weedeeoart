# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx import *
import random
import time

from generate_sequence import *
from files_scanner import *
# from moviepy.video.fx import volumex, resize, mirrorx

class VideoEditor():
	pass

def test():
	pass

# resize()

path = '../shaker/'
print(files_scanner(path))
write_data = time.strftime("%I%M%S")
print(write_data)

clips = []
clipsList = files_scanner(path)
print(clips)
dur = []

def randee(i):
	randee = random.uniform(0,dur[i])
	return randee

def freeze_files_list(clipsList):
	for i, objects in enumerate(clipsList):
		dur.append(clipsList[i].duration)
		rand = randee(i)
		clips.extend(generate_freeze(clipsList[i], [rand, rand+0.1], 10))
		rand = randee(i)
		clips.extend(generate_freeze(clipsList[i], [rand, rand+0.1], 10))
		rand = randee(i)
		clips.extend(generate_freeze(clipsList[i], [rand, rand+0.1], 10))
		rand = randee(i)
		clips.extend(generate_freeze(clipsList[i], [rand, rand+0.1], 10))
	return clips

''' used for applying mirror'''
clips = freeze_files_list(clipsList)
for i, objects in enumerate(clips):
	if i % 3 == 0:
		clips[i] = mirror_x(clips[i])
	if i % 2 == 0:
		clips[i] = mirror_y(clips[i])

print(clips)
clipOut = concatenate_videoclips(clips, method='compose')
clipOut.write_videofile("./" + write_data + "-out.mp4",fps=25)