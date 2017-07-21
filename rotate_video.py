# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random, time

from generate_sequence import *
from files_scanner import *


def rotate_video(video):
	rotatedVideo = rotate(video, 90)
	return rotatedVideo

path = '../shaker/'
seq = generate_sequence(files_scanner(path)[0], 2)
clipOut = rotate_video(seq)
write_data = time.strftime("%I%M%S")
clipOut.write_videofile("./" + write_data + "-out.mp4",fps=25)
