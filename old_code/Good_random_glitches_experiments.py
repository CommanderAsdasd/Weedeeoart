# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time
import pip
from generate_sequence import *
from files_scanner import *


class VideoEditor():
	
	def __init__():
		pass

def test():
	pass


# =======================================================================OUT====================================
path = sys.argv[1]
print(files_scanner_video(path))
exec_numb = 5

dur = []

def randclip(maxclips):
	return random.randint(0, maxclips)

def cut_logic(exec_numb):
	clips = []
	print(clips)
	clipsList = files_scanner_video(path)
	clipsCounter = len(clipsList) - 1
	for i, objects in enumerate(clipsList[::1]):
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, i + random.uniform(1, 2)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
	for i, objects in enumerate(clips):
		if i % random.randint(1, 5) == 0:
			clips[i] = mirror_x(clips[i])
		if i % random.randint(1, 4) == 0:
			clips[i] = time_symmetrize(clips[i])
		if i % random.randint(3, 6) == 0:
			# if 1 == random.randint(1, 2):
				# clips[i] = speedx(clips[i], 4)
			clips[i] = speedx(clips[i], random.randint(1, 10) * 0.5)

	concat_and_write(clips, exec_numb)

def resulst_store(clips, exec_numb):
	pass

def concat_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	try:
		clipOut = concatenate_videoclips(clips, method='compose')
		clipOut.write_videofile("./output_video/" + write_data + "-out.mp4",fps=25)
	except Exception as err:
		print(str(err) + "\n An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			cut_logic(exec_numb)
		else:
			print("game over")



