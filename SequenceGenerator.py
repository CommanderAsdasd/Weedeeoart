# -*- coding: utf-8 -*-
# C:/Python27/python.exe
import random
from moviepy.editor import *
from moviepy.video.fx.all import *


class SequenceGenerator():
    '''Class for making sequences from video based on different parametes and check for corectness'''

    def __init__(self, minLength=1, maxLength=1, startPoint=0):
        self.minLength = minLength
        self.maxLength = maxLength
        self.startPoint = startPoint

    def rand_sequence(self, clip):	
        clipDuration = clip.duration
        start = round(self.startPoint + random.uniform(0, clipDuration - 1), 4)	
        minL = self.minLength
        maxL = self.maxLength
        if self.maxLength > clipDuration:
            maxL = clipDuration
        sequenceLength = round(random.uniform(minL, maxL - 1), 4)
        end = start + sequenceLength
        print("Sequence is {}-{} ".format(round(start, 4), round(end, 4)))
        sequence = clip.subclip(start, end)
        return sequence

if __name__ == "__main__":
    print("Use it in script!")