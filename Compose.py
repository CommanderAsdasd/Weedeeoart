# -*- coding: utf-8 -*-
from moviepy.video.fx.all import *
import moviepy.audio.fx.all as afx
from moviepy.editor import *
import moviepy
import random

class Compose():

    def __init__(self):
        pass

    def clips_wall(self, chance=50, wallSize=4, mode='wall'):

        wallModes = {
            'wall' : lambda clips: clips_array([clips, clips])
        }
        clipsArray = []

        if hasattr(self, 'sequences_video'):
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    for k in range(wallSize):
                        clipsArray.append(random.choice(self.sequences_video))
                    self.sequences_video[i] = wallModes[mode](clipsArray)

    