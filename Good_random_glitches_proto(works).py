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
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 2)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)],1 , i + random.uniform(1, 2)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 2)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, i + random.uniform(1, 2)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, i + random.uniform(1, 2)))
		clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 2))
		clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 2))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 2)))
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

def resulst_store(clips, exec_numb):
	pass
	# if i % 4 == 0:
	# 	clips[i] = time_symmetrize(clips[i])
	# clips.append(generate_rand_sequence(clipsList[i], 1, random.uniform(1, 1.1)))
# 	clips.append(generate_rand_sequence(clipsList[random.randint(0, len(clipsList)-1)], 1, i + random.uniform(0, 4)))
# 	clips.extend(generate_freeze(clipsList[i], [1.01, 1.02], 3))
# 	clips.append(generate_rand_sequence(clipsList[i], 1, 2))
# 	clips.append(generate_rand_sequence(clipsList[i], 1, random.uniform(0, 0.1)))
# 	clips += generate_freeze(clipsList[1], [1, 1.02, 3, 3.05, 7, 5.24], 2)
# randpoints = []
# clips = []
# print()
# 	currclipDuration = clipsList[i].duration
# 	for j in range(0,1):
# 		point1 = random.uniform(0, currclipDuration)
# 		point2 = point1 + 0.2
# 		randpoints.append(point1)
# 		randpoints.append(point2)
# 		print(randpoints)








# Значит где-то внутри generate_freeze теряется инстанс и превращается в число.

# clip_in = generate_sequence(clip, 1.90)
# clip_in2 = generate_sequence(clip2, 5)
# print(clips)
# print(clips[0])
# clipOut.write_videofile("./" + write_data + "-out.avi",fps=25,codec='libx264',audio_codec='pcm_s16le')
def concat_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	try:
		clipOut = concatenate_videoclips(clips, method='compose')
		clipOut.write_videofile("./output_video/" + write_data + "-out.mp4",fps=25)
	except Exception:
		print("An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			cut_logic(exec_numb)
		else:
			print("game over")


cut_logic(exec_numb)