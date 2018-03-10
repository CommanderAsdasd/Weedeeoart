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


# =======================================================================OUT====================================
path = '../shaker/'
print(files_scanner_video(path))
exec_numb = 5

# clips.append(generate_rand_sequence(clipsList[0], 5, 4))
dur = []

def randclip(maxclips):
	return random.randint(0, maxclips)

def cut_logic(exec_numb):
	clips = []
	print(clips)
	clipsList = files_scanner_video(path)
	clipsCounter = len(clipsList) - 1
	for i, objects in enumerate(clipsList[::1]):
		clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 2))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(0, 1)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)],1 , i + random.uniform(1, 2)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 2)))
		# clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, i + random.uniform(1, 2)))
		# clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, i + random.uniform(1, 2)))
		# clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 2))
		clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 2))
		# clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 2)))
		# clips.append(generate_sequence(clipsList[randclip(clipsCounter)], [6.7, 6.8])
	for i, objects in enumerate(clips):
	# if i % 3 == 0:
	# 	clips[i] = mirror_x(clips[i])
		if i % random.randint(1, 5) == 0:
			clips[i] = speedx(clips[i], random.uniform(0.5, 2))
		if i % random.randint(1, 5) == 0:
			clips[i] = time_symmetrize(clips[i])
		# try:
		# 	if i < len(clips)-5:
		# 		clips.append(clips_array([[clips[i], clips[i+1]],
	 #                          [clips[i+3], clips[i+4]]]))
		# except:
		# 	pass
	concat_and_write(clips, exec_numb)

def concat_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	try:
		clipOut = concatenate_videoclips(clips, method='compose')
		clipOut.write_videofile("./output_video/" + write_data + "-out.mp4",fps=25)
	except Exception as e:
		print(str(e))
		print("An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			cut_logic(exec_numb)
		else:
			print("game over")


cut_logic(exec_numb)