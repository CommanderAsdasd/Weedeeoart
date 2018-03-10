# -*- coding: utf-8 -*-
# C:/Python27/python.exe

from fabric.api import local
import time
import sys
import random
import time

from generate_sequence import *
from files_scanner import *


	# # It works!

def film_rand_cutter():
	writeData = time.strftime("%I%M%S")
	outfile = writeData + '_ffef_vegas-enc.mp4'
	points = generate_ffmpeg_cutter_sequence(sys.argv[1], 0, 600, 3600)
	local('echo $OUTFILE')
	local('ffmpeg -i {} -acodec aac -vcodec libx264 -strict experimental -ss {} -to {} -tune fastdecode {}'.format(sys.argv[1], points[0], points[1], outfile))
	print(outfile)

def film_cutter():
	writeData = time.strftime("%I%M%S")
	outfile = writeData + '_ffef_vegas-enc.mp4'
	points = generate_ffmpeg_cutter_sequence(sys.argv[1], 0, 600, 3600)
	local('echo $OUTFILE')
	local('ffmpeg -i {} -acodec aac -vcodec libx264 -strict experimental -ss {} -to {} -tune fastdecode {}'.format(sys.argv[1], points[0], points[1], outfile))
	print(outfile)


film_cutter()