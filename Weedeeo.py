# -*- coding: utf-8 -*-

from FilesScanner import *
from SequenceGenerator import *
from Writer import *
from Compose import * 
from TimeEffects import *
from Mixing import *
import os
import sys
import moviepy
import logging
import random
import json
from moviepy.video.fx.all import *
import moviepy.audio.fx.all as afx
from math import *

class Videocringe(Writer, Compose, TimeEffects, Mixing):
    '''Main class of video cutter combine Defines how and how much video will be cringed. clips is original files, 
    sequences is a internal chops of these media clips'''

    def __init__(self, path='./', logging='DEBUG'):
        Writer.__init__(self)
        Compose.__init__(self)
        Mixing.__init__(self)
        self.sequences_video = []
        self.sequences_audio = []
        
        self.exec_numb = 5
        self.path = path
        # self.clips = []
        self.Scanner = FilesScanner(self.path)
        self._logger()
        

    def _logger(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)

    def shuffle_video(self, minLength=1, maxLength=1, times=1):
        
        self.clips_video = self.Scanner.scan_video()
        GeneratorVideo = SequenceGenerator(minLength, maxLength)
        for i in self.clips_video:
            for j in range(0,times):
                self.sequences_video.append(GeneratorVideo.rand_sequence(i))
        random.shuffle(self.sequences_video)
        # logging.debug("Video is: {}".format(self.sequences_video))

    def shuffle_images(self, minLength=1, maxLength=1, times=1):
        self.clips_video = self.Scanner.scan_images(maxLength)
        # logging.debug("images are: {}".format(self.clips_video))
        GeneratorImages = SequenceGenerator(minLength, maxLength)
        for i in self.clips_video:
            for j in range(0,times):
                self.sequences_video.append(GeneratorImages.rand_sequence(i))
        random.shuffle(self.sequences_video)

    def shuffle_audio(self, minLength=1, maxLength=1, times=1):
        
        self.clips_audio = self.Scanner.scan_audio()
        # logging.debug(self.clips_audio)
        GeneratorAudio = SequenceGenerator(minLength, maxLength)
        for i in self.clips_audio:
            self.clips_audio
            for j in range(0,times):
                self.sequences_audio.append(GeneratorAudio.rand_sequence(i))
        random.shuffle(self.sequences_audio)
        # logging.debug("Audio is: {}".format(self.sequences_audio))

    def chop_video(self, timecodes):
        if (hasattr(self, 'sequences_video')):
            self.clips_video = self.Scanner.scan_video()
            self.sequences_video = []
            with open(timecodes) as chopFile:
                chopStr = chopFile.read()
                chopData = json.loads(chopStr)
            GeneratorVideo = SequenceGenerator()
            for i in self.clips_video:
                for start, end in chopData.items():
                    self.sequences_video.insert(0,GeneratorVideo.sequence(i, start, end))
                # print(start, end)


    def audio_fx(self):
        '''bring audio fx '''
        # for i, pointerAudio in enumerate(self.sequences_audio):
        #     if random.randint(0,100) <= chance:
        #         self.sequences_audio[i] = pointerAudio.
    
    def reshuffle(self):
        if hasattr(self, 'sequences_video'):
            random.shuffle(self.sequences_video)
        if hasattr(self, 'sequences_audio'):
            random.shuffle(self.sequences_video)
        
    def invert_green_blue(self):
        pass

if __name__ == '__main__':
    i = 1
    try:
        def video_preset():
            # editor = None
            editor = Videocringe(sys.argv[1])
            # editor.shuffle_images(0.1,0.3,5)
            # editor.chop_video('./chop.json')
            # editor.shuffle_video(1,3,2) # cool 1-second preset
            editor.shuffle_video(1,3,5)
            # editor.time_warper(80)
            # editor.clips_wall(chance=50)
            editor.shuffle_audio(1,3,1)
            # editor.uncareful_mixing(chance=75)
            editor.careful_mixing(chance=25)
            # editor.speed_changer(minspeed=0.1, maxspeed=10, chance=80)
            editor.reverser(chance=75)
            editor.symmetrizer(chance=75)
            # editor.shuffle_video(1,2,10)
            # editor.shuffle_audio(1,3,10)
            # editor.write_audio()
            editor.reshuffle()
            # editor.write_video()
            editor.wirte_video_separate()
            # editor.wirte_audio_separate()

        def audio_preset():
            editor = Videocringe(sys.argv[1])
            editor.shuffle_audio(0.2,1,20)
            editor.shuffle_audio(1,2,10)
            editor.speed_changer(minspeed=0.1, maxspeed=10, chance=80)
            editor.reverser(chance=75)
            editor.symmetrizer(chance=75)
            editor.write_audio()
            # editor.write_video()

        video_preset()
    except Exception as e:
        if i >= 0: 
            print("Error occured")
            print(str(e))
            i -= 1
            video_preset()
        else:
            print("Exit")