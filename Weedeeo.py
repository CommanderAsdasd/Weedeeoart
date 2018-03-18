# -*- coding: utf-8 -*-

from FilesScanner import *
from SequenceGenerator import *
from Writer import *
import os
import sys
import moviepy
import logging
import random

class Videocringe(Writer):
    '''Main class of video cutter combine Defines how and how much video will be cringed. clips is original files, sequences is a internal chops of these media clips'''

    def __init__(self, path='./'):
        self.exec_numb = 5
        self.path = path
        # self.clips = []
        self.date = time.strftime("%I%M%S")
        self.Scanner = FilesScanner(self.path)
        self.logger()

    def logger(self):
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
        logging.debug("Video is: {}".format(self.sequences_video))

    def shuffle_audio(self, minLength=1, maxLength=1, times=1):
        self.clips_audio = self.Scanner.scan_audio()
        self.sequences_audio = []
        print('DEBUG clips_audio is only audio:', self.clips_audio)
        logging.debug(self.clips_audio)
        GeneratorAudio = SequenceGenerator(minLength, maxLength)
        for i in self.clips_audio:
            self.clips_audio
            for j in range(0,times):
                self.sequences_audio.append(GeneratorAudio.rand_sequence(i))
        random.shuffle(self.sequences_audio)
        logging.debug("Audio is: {}".format(self.sequences_audio))
        # logging.debug(self.sequences_audio)

    def rand_mixing(self, chance=50):
        
        '''this method randmoly choose item from sequences_audio and append it to sequences_video due to chance variable '''

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
                logging.debug('DEBUG AUDIO IS EXIST: {}'.format(pointerAudio))
                sequences_video[i] = pointerVideo.set_audio(pointerAudio)


    


    '''helper function for getting filename (or dirname) from path'''

if __name__ == '__main__':
    editor = Videocringe(sys.argv[1])
    # editor.shuffle_video(1,3,10)
    editor.shuffle_video(0.1,3,5) # cool 1-second preset
    editor.shuffle_audio(0.1,15,5)
    editor.rand_mixing(chance=50)
    # editor.shuffle_video(1,2,10)
    # editor.shuffle_audio(1,3,10)
    # editor.write_audio()
    editor.write_video()