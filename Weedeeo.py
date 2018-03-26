# -*- coding: utf-8 -*-

from FilesScanner import *
from SequenceGenerator import *
from Writer import *
import os
import sys
import moviepy
import logging
import random
from moviepy.video.fx.all import *
import moviepy.audio.fx.all as afx
from math import *

class Videocringe(Writer):
    '''Main class of video cutter combine Defines how and how much video will be cringed. clips is original files, 
    sequences is a internal chops of these media clips'''

    def __init__(self, path='./', logging='DEBUG'):
        Writer.__init__(self)
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
        self.sequences_video = []
        GeneratorVideo = SequenceGenerator(minLength, maxLength)
        for i in self.clips_video:
            for j in range(0,times):
                self.sequences_video.append(GeneratorVideo.rand_sequence(i))
        random.shuffle(self.sequences_video)
        # logging.debug("Video is: {}".format(self.sequences_video))

    def shuffle_audio(self, minLength=1, maxLength=1, times=1):
        self.clips_audio = self.Scanner.scan_audio()
        self.sequences_audio = []
        # logging.debug(self.clips_audio)
        GeneratorAudio = SequenceGenerator(minLength, maxLength)
        for i in self.clips_audio:
            self.clips_audio
            for j in range(0,times):
                self.sequences_audio.append(GeneratorAudio.rand_sequence(i))
        random.shuffle(self.sequences_audio)
        # logging.debug("Audio is: {}".format(self.sequences_audio))

    def careful_mixing(self, chance=50):
        '''this method randmoly choose item from sequences_audio and append it to sequences_video due to chance variable.
        Audio/video sync'''
        if (hasattr(self, 'sequences_audio')) and (hasattr(self, 'sequences_video')):
            sequences_video = self.sequences_video
            sequences_audio = self.sequences_audio
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    pointerAudio = random.choice(sequences_audio)
                    print('DEBUG pointer is point on audio:', pointerAudio)
                    video_duration, audio_duration = sequences_video[i].duration, pointerAudio.duration
                    # How to rewrite it to .set_end
                    if video_duration > audio_duration:
                        pointerVideo = sequences_video[i].subclip(0, audio_duration)
                    elif video_duration < audio_duration:
                        pointerAudio = pointerAudio.subclip(0, video_duration)
                    # logging.debug('DEBUG AUDIO IS EXIST: {}'.format(pointerAudio))
                    sequences_video[i] = pointerVideo.set_audio(pointerAudio)
        else:
            logging.info("This method requires both audio and video providing")

    def uncareful_mixing(self, chance=50):
        '''Audio/video async'''
        if (hasattr(self, 'sequences_audio')) and (hasattr(self, 'sequences_video')):
            sequences_video = self.sequences_video
            sequences_audio = self.sequences_audio
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    pointerAudio = random.choice(sequences_audio)
                    video_duration, audio_duration = sequences_video[i].duration, pointerAudio.duration
                    # if video_duration > audio_duration:
                    #     pointerVideo = sequences_video[i].subclip(0, audio_duration)
                    # elif video_duration < audio_duration:
                    #     pointerAudio = pointerAudio.subclip(0, video_duration)
                    logging.debug('DEBUG AUDIO IS EXIST: {}'.format(pointerAudio))
                    sequences_video[i] = pointerVideo.set_audio(pointerAudio)
        else:
            logging.info("This method requires both audio and video providing")

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

    def audio_fx(self):
        '''bring audio fx '''
        # for i, pointerAudio in enumerate(self.sequences_audio):
        #     if random.randint(0,100) <= chance:
        #         self.sequences_audio[i] = pointerAudio.

    def time_warper(self, chance=50):
        for i, pointerVideo in enumerate(self.sequences_video):
            if random.randint(0,100) <= chance:
                changedClip = pointerVideo.fl_time(lambda t: 1+sin(t))
                self.sequences_video[i] = pointerVideo.fl_time(lambda t: 1+sin(t))
                logging.debug("Clip changing time_warper debug {}".format(changedClip))

    def clips_wall(self, chance=50, wallSize=4, mode='multiply'):

        wallModes = {
            'multiply' : lambda clips: clips_array([clips])
        }
        clipsArray = []

        if hasattr(self, 'sequences_video'):
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    for k in range(wallSize):
                        clipsArray.append(random.choice(self.sequences_video))
                    self.sequences_video[i] = wallModes[mode](clipsArray)
                            
    
    def reshuffle(self):
        if hasattr(self, 'sequences_video'):
            random.shuffle(self.sequences_video)
        if hasattr(self, 'sequences_audio'):
            random.shuffle(self.sequences_video)
        
    def invert_green_blue(self):
        pass

if __name__ == '__main__':
    i = 3
    try:
        def video_preset():
            editor = Videocringe(sys.argv[1])
            editor.shuffle_video(1,3,5)
            # editor.shuffle_video(1,3,2) # cool 1-second preset
            # editor.time_warper(80)
            editor.clips_wall(chance=50)
            # editor.shuffle_audio(5,5,10)
            # editor.uncareful_mixing(chance=75)
            # editor.careful_mixing(chance=25)
            editor.speed_changer(minspeed=0.1, maxspeed=10, chance=80)
            editor.reverser(chance=75)
            editor.symmetrizer(chance=75)
            # editor.shuffle_video(1,2,10)
            # editor.shuffle_audio(1,3,10)
            # editor.resize()
            # editor.write_audio()
            editor.reshuffle()
            editor.write_video()

        def audio_preset():
            editor = Videocringe(sys.argv[1])
            editor.shuffle_audio(0.2,1,20)
            editor.shuffle_audio(1,2,10)
            editor.speed_changer(minspeed=0.1, maxspeed=10, chance=80)
            editor.reverser(chance=75)
            editor.symmetrizer(chance=75)
            editor.resize()
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