# -*- coding: utf-8 -*-
from moviepy.editor import *
from moviepy.video.fx.all import *
import ntpath
import logging
import time

class Writer():
    '''Helper class to write video'''
    def __init__(self):
        self.counter = 5 #debugging option
        self.clipOut = None

    def get_filename(self):
        head, tail = ntpath.split(self.path)
        return tail or ntpath.basename(head)

    def resize(self):
        '''writes only video, resizing it to 1920x1080 size'''
        try:
            for i, sequence in enumerate(self.sequences_video):
                self.sequences_video[i] = sequence.resize( (1920, 1080) )
        except Exception as NoVideoError:
            logging.info("Error occured, \n {}".format(NoVideoError))


    def write_video(self):
        # if (hasattr(self, 'sequences_video')):
            # while (self.counter > 0):
        self.date = time.strftime("%I%M%S")
        self.resize()
        # try:
        self.clipOut = concatenate_videoclips(self.sequences_video, method='compose')
        self.clipOut.write_videofile("./output_video/" + self.get_filename() + self.date + "-out.mp4", fps=30, codec='libx264', audio_codec='aac')
        # except Exception as e:
            # self.counter -= 1
        self.write_video()
                    
        # else:
        #     logging.info("No video available for write")



    def write_audio(self):
        '''writes only audio'''
        self.date = time.strftime("%I%M%S")
        clipOut = concatenate_audioclips(self.sequences_audio)
        clipOut.write_audiofile("./output_video/" + self.get_filename() + self.date + "-out.wav")

    def write(self):
        pass