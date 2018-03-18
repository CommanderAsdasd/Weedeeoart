# -*- coding: utf-8 -*-
from moviepy.editor import *
from moviepy.video.fx.all import *
import ntpath
import logging

class Writer():
    '''Main class of video cutter combine
       Defines how and how much video will be cringed'''

    def get_filename(self):
        head, tail = ntpath.split(self.path)
        return tail or ntpath.basename(head)

    def write_video(self):
        '''writes only video, resizing it to 1920x1080 size'''
        for i, sequence in enumerate(self.sequences_video):
            self.sequences_video[i] = sequence.resize( (1920, 1080) )
        clipOut = concatenate_videoclips(self.sequences_video, method='compose')
        clipOut.write_videofile("./output_video/" + self.get_filename() + self.date + "-out.mp4", fps=30, codec='libx264', audio_codec='aac')

    def write_audio(self):
        '''writes only audio'''
        clipOut = concatenate_audioclips(self.sequences_audio)
        clipOut.write_audiofile("./output_video/" + self.get_filename() + self.date + "-out.wav")

    def write(self):
        pass