# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

# from generate_sequence import *
from refactor.generate_sequence import *
from files_scanner import *
from PIL import ImageFilter
from PIL import Image
from scipy import ndimage
import numpy as np
import numpy
import math


class VideoEditor():
    pass


def test():
    pass


# =======================================================================OUT====================================
# Better not to stor audio and video in same folder
path = '../shaker/'
pathAudio = '../audioShaker/'
exec_numb = 5

dur = []


def randclip(maxclips):
    return random.randint(0, maxclips)

def PIL_framerand_filters(inpImage):
    print("Effecting")
    filters = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SMOOTH", "SMOOTH_MORE", "SHARPEN"]
    randFilter = getattr(ImageFilter, random.choice(filters))
    im_array = inpImage
    inpImage = Image.fromarray(inpImage, 'RGB')
    inpImage = inpImage.filter(randFilter)
    imArr = numpy.fromstring(inpImage.tobytes(), dtype=np.uint8)
    imArr = imArr.reshape((inpImage.size[1], inpImage.size[0], 3))
    return imArr

def Wand_filters(inpImage):
    # print("Effecting")
    # filters = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SMOOTH", "SMOOTH_MORE", "SHARPEN"]
    # randFilter = getattr(ImageFilter, random.choice(filters))
    im_array = inpImage
    inpImage = Image.fromarray(inpImage, 'RGB')
    inpImage = inpImage.filter(randFilter)
    with Image(blob=inpImage.tobytes()) as img:
        print('width =', img.width)
        print('height =', img.height)
    
    # imArr = numpy.fromstring(inpImage.tobytes(), dtype=np.uint8)
    # imArr = imArr.reshape((inpImage.size[1], inpImage.size[0], 3))
    return imArr

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
                pointer = random.randint(0, len(pieces) - 1)
                pointerAudio = piecesAudio[random.randint(0, len(piecesAudio) - 1)]
                pieces[pointer] = pieces[pointer].set_audio(pointerAudio)
                pointer = random.randint(0, len(pieces) - 1)

    for i, objects in enumerate(pieces):
        if i % 3 == 0:
            pieces[i] = mirror_x(pieces[i])
            if i % random.randint(3, 4) == 0:
                pieces[i] = speedx(pieces[i], 0.5)
            if i % random.randint(1, 5) == 0:
            # textSub = TextClip('Lol')
                pieces[i] = (pieces[i].fl_image(Wand_filters))

    # concat_and_write(pieces, exec_numb)


def resulst_store(clips, exec_numb):
    pass

def concat_and_write(clips, exec_numb):
    write_data = time.strftime("%I%M%S")
    print(write_data)
    for i, clip in enumerate(clips):
    	clips[i] = clips[i].resize( (1920, 1080) )
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
