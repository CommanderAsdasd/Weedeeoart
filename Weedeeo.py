# -*- coding: utf-8 -*-

from FilesScanner import *
from SequenceGenerator import *
from Writer import *
from Compose import * 
from TimeEffects import *
from ImageEffects import *
from Mixing import *
from math import *
from moviepy.video.fx.all import *
import os
import sys
import moviepy
import logging
import random
import json
import moviepy.audio.fx.all as afx
import multiprocessing
from itertools import product


class Weedeeo(FilesScanner, Writer, Compose, TimeEffects, ImageEffects, Mixing):
    '''Main class of video cutter combine Defines how and how much video will be cringed. Term 'Clips' is used for original files, 
    sequences is a internal cuts of these media clips'''

    def __init__(self, path='./', logging='DEBUG', scantype = 'default'):
        Compose.__init__(self)
        Mixing.__init__(self)
        ImageEffects.__init__(self)
        self.sequences_video = []
        self.sequences_audio = []
        self.exec_numb = 5
        self.path = path
        self.Scanner = FilesScanner(self.path)
        self._logger()
        if scantype =="recur":
            self._scan_recur()
        elif scantype == "default":
            self._scan_default()
    
    def _scan_recur(self):
        self.Scanner.random_iterative_crawler()
        

    def _scan_default(self):
        # self.clips_video = self.Scanner.scan_video()
        # self.clips_audio = self.Scanner.scan_audio()
        pass

    def _count_clips():
    	return len(self.clips_video)

    def _count_sequences(self):
    	return len(self.sequences_video)

    def _logger(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)

    def shuffle_video(self, minLength=1, maxLength=1, times=1):
        GeneratorVideo = SequenceGenerator(minLength, maxLength)
        for i in self.Scanner.clips_video:
            for j in range(0,times):
                self.sequences_video.append(GeneratorVideo.rand_sequence(i))
        random.shuffle(self.sequences_video)
        # logging.debug("Video is: {}".format(self.sequences_video))

    def shuffle_images(self, minLength=1, maxLength=1, times=1):
        # logging.debug("images are: {}".format(self.clips_video))
        self.clips_video.append(self.Scanner.scan_images(maxLength))
        GeneratorImages = SequenceGenerator(minLength, maxLength)
        for i in self.clips_video:
            for j in range(0,times):
                self.sequences_video.append(GeneratorImages.rand_sequence(i))
        random.shuffle(self.sequences_video)

    def shuffle_audio(self, minLength=1, maxLength=1, times=1):
        # logging.debug(self.clips_audio)
        GeneratorAudio = SequenceGenerator(minLength, maxLength)
        for i in self.clips_audio:
            self.clips_audio
            for j in range(0,times):
                self.sequences_audio.append(GeneratorAudio.rand_sequence(i))
        random.shuffle(self.sequences_audio)
        # logging.debug("Audio is: {}".format(self.sequences_audio))

    def chop_sequences(self, timecodes):
        if (len(self.sequences_video)>0):
            with open(timecodes) as chopFile:
                chopStr = chopFile.read()
                chopData = json.loads(chopStr)
            GeneratorVideo = SequenceGenerator()
            for i in self.clips_video:
                for start, end in chopData.items():
                    self.sequences_video.insert(0,GeneratorVideo.sequence(i, start, end))
                # print(start, end)

    def chop_clips(self, timecodes):
        # if (hasattr(self, 'sequences_video')):
        if (len(self.clips_video)>0):
            clips_video_chop = []
            with open(timecodes) as chopFile:
                chopStr = chopFile.read()
                chopData = json.loads(chopStr)
            GeneratorVideo = SequenceGenerator()
            for i, clip in enumerate(self.clips_video):
                for start, end in chopData.items():
                    try:
                        clips_video_chop.append(GeneratorVideo.sequence(clip, start, end))
                    except Exception as e:
                        logging.info("An error in function {} occured: '{}'".format(sys._getframe().f_code.co_name, e))
            self.clips_video = clips_video_chop
                # print(start, end)


    def audio_fx(self):
        '''bring audio fx '''
        # for i, pointerAudio in enumerate(self.sequences_audio):
        #     if random.randint(0,100) <= chance:
        #         self.sequences_audio[i] = pointerAudio.
    
    def reshuffle(self):
        if len(self.sequences_video) != 0:
            random.shuffle(self.sequences_video)
        if len(self.sequences_audio) != 0:
            random.shuffle(self.sequences_video)
        # if len(self.sequences_audio) != 0:
        #     self.sequences_altered + self.sequences_video)
        
    def invert_green_blue(self):
        pass

