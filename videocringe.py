# -*- coding: utf-8 -*-

from FilesScanner import *
from SequenceGenerator import *
import os
import sys
import moviepy
import ntpath
import logging

class Videocringe():
    '''Main class of video cutter combine
       Defines how and how much video will be cringed'''

    def __init__(self, path='./'):
        self.exec_numb = 5
        self.path = path
        self.clips = []
        self.sequences = []
        self.date = time.strftime("%I%M%S")
        self.Scanner = FilesScanner(self.path)

    def cut_video(self, minLength=1, maxLength=1, times=1):
        self.clips_video = self.Scanner.scan_video()
        GeneratorVideo = SequenceGenerator(minLength, maxLength)
        for i in self.clips_video:
            for j in range(0,times):
                self.sequences.append(Generator.rand_sequence(i))
        random.shuffle(self.sequences)
        # print(self.sequences)

    def cut_audio(self, minLength=1, maxLength=1, times=1):
        self.clips_audio = self.Scanner.scan_audio()
        print(self.clips_audio)
        GeneratorAudio = SequenceGenerator(minLength, maxLength)
        for i in self.clips_audio:
            for j in range(0,times):
                self.sequences.append(GeneratorAudio.rand_sequence(i))
        random.shuffle(self.sequences)
        # print(self.sequences)


    '''helper function for getting filename (or dirname) from path'''
    def get_filename(self):
        head, tail = ntpath.split(self.path)
        return tail or ntpath.basename(head)

    def write_video(self):
        '''writes only video, resizing it to 1920x1080 size'''
        for i, sequence in enumerate(self.sequences):
            self.sequences[i] = sequence.resize( (1920, 1080) )
        clipOut = concatenate_videoclips(self.sequences, method='compose')
        clipOut.write_videofile("./output_video/" + self.get_filename() + self.date + "-out.mp4", fps=30, codec='libx264', audio_codec='aac')

    def write_audio(self):
        '''writes only audio'''
        clipOut = concatenate_audioclips(self.sequences)
        clipOut.write_audiofile("./output_video/" + self.get_filename() + self.date + "-out.wav")

if __name__ == '__main__':
    editor = Videocringe(sys.argv[1])
    # editor.cut_video(1,3,10)
    # editor.cut_video(0.1,0.2,20)
    # editor.cut_video(1,2,10)
    editor.cut_audio(4,5,10)
    editor.write_audio()