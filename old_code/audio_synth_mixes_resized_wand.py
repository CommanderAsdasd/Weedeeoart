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
from wand.image  import Image as wndImage
from scipy import ndimage
# import willow as willImage
import willow.image as willImage
import numpy as np
import numpy
import math
import StringIO
import sys

# print(willWand)

class VideoEditor():
    pass


def test():
    pass


# =======================================================================OUT====================================
# Better not to stor audio and video in same folder
path = sys.argv[1]
pathAudio = sys.argv[2]
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
    temp = StringIO.StringIO()
    temp = inpImage.save(temp, format="png")
    # inpImage = willImage.Image(inpImage)
    # inpImage = inpImage.filter(randFilter)
    with wndImage(file=temp) as img:
        print('width =', inpImage.width)
        print('height =', inpImage.height)
     # imArr = numpy.fromstring(inpImage.tobytes(), dtype=np.uint8)
    # imArr = imArr.reshape((inpImage.size[1], inpImage.size[0], 3))
    # return imArr

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

        for i, objects in enumerate(clipsAudioList[::6]):
            for j in range(0, 2):
                piecesAudio.append(generate_rand_sequence(clipsAudioList[randclip(clipsAudioCounter)], minLength=4, clipLength=pieceLength))

        	
        for i, objects in enumerate(clipsList[::6]):
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


cut_logic(exec_numb)
