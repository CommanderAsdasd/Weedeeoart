# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

# from generate_sequence import *
from generate_sequence import *
from files_scanner import *


class VideoEditor():
    pass


def test():
    pass


# =======================================================================OUT====================================


def cut_logic(exec_numb, path, pathAudio):
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
    	for j in range(0, 3):
	    	piecesAudio.append(generate_rand_sequence(clipsAudioList[randclip(clipsAudioCounter)], minLength=4, clipLength=pieceLength))

    	
    for i, objects in enumerate(clipsList[::1]):
        for j in range(0, 3):
        	pieces.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], minLength=4, clipLength=pieceLength))
        	# print(pieces)
        	# print(piecesAudio)

        # if i % random.randint(0, 4) == 0:
        # if i %  == 0:
            # 
	        pointer = random.randint(0, len(pieces) - 1)
	        pointerAudio = piecesAudio[random.randint(0, len(piecesAudio) - 1)]
	        pieces[pointer] = pieces[pointer].set_audio(pointerAudio)
	        pointer = random.randint(0, len(pieces) - 1)

    concat_and_write(pieces, exec_numb)


def resulst_store(clips, exec_numb):
    pass
