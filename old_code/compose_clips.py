# -*- coding: utf-8 -*-

from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

from generate_sequence import *
from files_scanner import *


exec_numb = 5

path = '../shaker/'
print(files_scanner(path))

def randclip(maxclips):
	return random.randint(0, maxclips)

def composing_clips(path, exec_numb):
	clips = []
	clipsList = files_scanner(path)
	clipsCounter = len(clipsList) - 1
	for i, objects in enumerate(clipsList[::1]):
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
	compose_and_write(clips, exec_numb)

def compose_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	try:
		# clipOut = concatenate_videoclips(clips, method='compose')
		for i, objects in enumerate(clips):
			clipOut = CompositeVideoClip([clips[0].resize(1.5).set_pos((45,150)),clips[1].crossfadeout(1),clips[2]])
		clipOut.write_videofile("./" + write_data + "-out.mp4",fps=25)
	except Exception as e:
		print(e.message + "\n An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			composing_clips(path, exec_numb)
		else:
			print("game over")

composing_clips(path, exec_numb)