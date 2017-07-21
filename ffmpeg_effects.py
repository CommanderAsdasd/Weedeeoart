# -*- coding: utf-8 -*-
from ffmpy import *
import time
from generate_sequence import *
from files_scanner import *

path = '../shaker/'
print(files_scanner_ffmpeg(path))
write_data = time.strftime("%I%M%S")
print(write_data)


# Ff = ffmpy
print(FFmpeg)
clipsList = files_scanner(path)
start = "00:00:05.0"
dur  = "00:00:05.0"
openFile = ""
for i, file in enumerate(clipsList):
    outFileName = "{}output.avi".format(write_data)
    print(type(outFileName))
    Ff = FFmpeg(  
     inputs={"E:\\Windows.old\\Users\\Cmmndr\\Videos\\Shortly_say\\SesamePinball.mp4" :None},
     outputs={outFileName : [ "-vf", "split [main][tmp]; [tmp] crop=iw:ih/2:0:0, vflip [flip]; [main][flip] overlay=0:H/2", '-af', "aecho=0.8:0.88:60:0.4", '-acodec aac', '-vcodec libx264', '-strict experimental', '-ss {}  -to {}'.format(start, dur), '-tune fastdecode'] }
    )
    print(Ff.cmd)
    Ff.run()

'''
Нужно замостырить стартовую и конечную последовательности рандомом
'''