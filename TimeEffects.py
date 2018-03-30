# -*- coding: utf-8 -*-
from moviepy.video.fx.all import *
import moviepy.audio.fx.all as afx
from moviepy.editor import *
import moviepy
import random

class TimeEffects():

    def __init__(self):
        pass

    def reverser(self, chance=50):
        '''reverses_the_clips'''
        
        if hasattr(self, 'sequences_audio'):
            for i, pointerAudio in enumerate(self.sequences_audio):
                if random.randint(0,100) <= chance:
                    self.sequences_audio[i] = time_mirror(pointerAudio)
        if hasattr(self, 'sequences_video'):
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    self.sequences_video[i] = time_mirror(pointerVideo)
        if not (hasattr(self, 'sequences_audio')) and not (hasattr(self, 'sequences_video')):
            logging.info("no video and audio sequences provided") 

    def symmetrizer(self, chance=50):
        '''reverses_the_clips. Currently not implement audio'''

        # if hasattr(self, 'sequences_audio'):
        #     for i, pointerAudio in enumerate(self.sequences_audio):
        #         if random.randint(0,100) <= chance:
        #             self.sequences_audio[i] = time_symmetrize(pointerAudio)
        if hasattr(self, 'sequences_video'):
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    self.sequences_video[i] = time_symmetrize(pointerVideo)
        if not (hasattr(self, 'sequences_audio')) and not (hasattr(self, 'sequences_video')):
            logging.info("no video or audio sequences provided")            


    def speed_changer(self, minspeed=0.5, maxspeed=2, chance=50):
        '''randomly chages speed'''
        if hasattr(self, 'sequences_audio'):
            for i, pointerAudio in enumerate(self.sequences_audio):
                if random.randint(0,100) <= chance:
                    self.sequences_audio[i] = speedx(pointerAudio, random.uniform(minspeed, maxspeed))
        if hasattr(self, 'sequences_video'):
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    self.sequences_video[i] = speedx(pointerVideo, random.uniform(minspeed, maxspeed))
        if not (hasattr(self, 'sequences_audio')) and not (hasattr(self, 'sequences_video')):
            logging.info("no video or audio sequences provided")

    def time_warper(self, chance=50):
        for i, pointerVideo in enumerate(self.sequences_video):
            if random.randint(0,100) <= chance:
                changedClip = pointerVideo.fl_time(lambda t: 1+sin(t))
                self.sequences_video[i] = pointerVideo.fl_time(lambda t: 1+sin(t))
                logging.debug("Clip changing time_warper debug {}".format(changedClip))