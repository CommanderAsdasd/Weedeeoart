# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

# from generate_sequence import *
from refactor.generate_sequence import *
from files_scanner import *


class VideoEditor():
    pass


def test():
    pass


# =======================================================================OUT====================================
# Better not to stor audio and video in same folder
path = '../shaker/'
pathAudio = '../audioShaker/'
# print(files_scanner_video(path))
exec_numb = 5

dur = []


def randclip(maxclips):
    return random.randint(0, maxclips)


def cut_logic(exec_numb):
    pieces = []
    piecesAudio = []
    clipsList = files_scanner_video(path)
    clipsAudioList = files_scanner_audio(pathAudio)
    print(clipsAudioList)
    clipsCounter = len(clipsList) - 1
    clipsAudioCounter = len(clipsAudioList) - 1
    # iterate over
    for i in range(0,2):
    	pieceLength = random.uniform(1, 2)

    for i, objects in enumerate(clipsAudioList[::1]):
    	for j in range(0, 2):
	    	piecesAudio.append(generate_rand_sequence(clipsAudioList[randclip(clipsAudioCounter)], minLength=4, clipLength=pieceLength))

    	
    for i, objects in enumerate(clipsList[::1]):
        for j in range(0, 2):
        	pieces.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], minLength=4, clipLength=pieceLength))
        	# print(pieces)
        	# print(piecesAudio)

        # if i % random.randint(0, 4) == 0:
        # if i %  == 0:
            # 
	        pointer = random.randint(0, len(pieces) - 1)
	        pointerAudio = piecesAudio[random.randint(0, len(piecesAudio) - 1)]
	        # pieces[1] = time_symmetrize(pieces[1])
	        pieces[pointer] = pieces[pointer].set_audio(pointerAudio)
	        pointer = random.randint(0, len(pieces) - 1)
	        # print(pointer)
	        # print(clipsCounter)
	        # print("Debug 4-07: ", pointer, pointerAudio)
            # print(clips)

    concat_and_write(pieces, exec_numb)


def resulst_store(clips, exec_numb):
    pass

def concat_and_write(clips, exec_numb):
    write_data = time.strftime("%I%M%S")
    print(write_data)
    try:
	    clipOut = concatenate_videoclips(clips, method='compose')
	    clipOut.write_videofile("./output_video/" + write_data + "-out.mp4", fps=25)
    except Exception as e:
        print(str(e))
        print("An error occured, try {} times".format(exec_numb))
        if exec_numb > 0:
            exec_numb -= 1
            cut_logic(exec_numb)
        else:
            print("game over")


cut_logic(exec_numb)
