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
# Better not to stor audio and video in same folder
path = '../shaker/'
pathAudio = '../audioShaker/'
# print(files_scanner_video(path))
exec_numb = 5

dur = []


def randclip(maxclips):
    return random.randint(0, maxclips)


def cut_logic(exec_numb):
    clips = []
    clipsAudio = []
    print(clips)
    clipsList = files_scanner_video(path)
    clipsAudioList = files_scanner_audio(pathAudio)
    print(clipsAudioList)
    clipsCounter = len(clipsList) - 1
    clipsAudioCounter = len(clipsList) - 1
    for i, objects in enumerate(clipsList[::1]):
        for j in range(0, 4):
        	clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
        	clipsAudio.append(generate_rand_sequence_audio(clipsAudioList[randclip(clipsAudioCounter)], 0, random.uniform(1, 1.5)))
        	print(clips)
        	print(clipsAudio)

        if i % random.randint(2, 4) == 0:
            # clips[random.randint(0,clipsAudioCounter)] = time_symmetrize(clips[i])
            pointer = random.randint(0,clipsCounter)
            # clips[pointer] = clips[pointer].set_audio(clipsAudio[random.randint(0,clipsAudioCounter)])
            # print(clips)

    concat_and_write(clips, clipsAudio, exec_numb)


def resulst_store(clips, exec_numb):
    pass

def concat_and_write(clips, clipsAudio, exec_numb):
    write_data = time.strftime("%I%M%S")
    print(write_data)
    # try:
    clipOut = concatenate_videoclips(clips, method='compose').set_audio(clipsAudio[0])
    print("debug3-41: ", clipOut)
    print(dir(clipOut))
    clipOut.write_videofile("./output_video/" + write_data + "-out.mp4", fps=25)
    # except Exception as e:
    #     print(str(e))
    #     print("An error occured, try {} times".format(exec_numb))
    #     if exec_numb > 0:
    #         exec_numb -= 1
    #         cut_logic(exec_numb)
    #     else:
    #         print("game over")


cut_logic(exec_numb)
