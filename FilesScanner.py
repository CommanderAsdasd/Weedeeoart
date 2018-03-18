# -*- coding: utf-8 -*-

from moviepy.editor import *
from moviepy.video.fx.all import *
import os
import time
import random
import sys
import re

class FilesScanner():

    # TODO loging
    def __init__(self, path):
        self.files_video = []
        self.files_audio = []
        self.sourceFile = []
        self.path = path

    def randclip(self, maxclips=1):
        return random.randint(0, maxclips)

    def scan_video(self):
        formats = re.compile("mp4$|avi$|webm$|m2t$|gif$")
        if (os.path.isdir(self.path)):
            for i, filename in enumerate(os.listdir(self.path)):
                if (formats.match(filename.split(".")[-1])):
                    print("Videofile", filename)
                    self.files_video.append(VideoFileClip(os.path.join(self.path, filename)))
        else:
            self.files_video.append(VideoFileClip(self.path))
        return self.files_video

    def scan_audio(self):
        formats = re.compile("wav$|mp3$")
        if (os.path.isdir(self.path)):
            for i, filename in enumerate(os.listdir(self.path)):
                if (formats.match(filename.split(".")[-1])):
                    print("Audiofile", filename)
                    self.files_audio.append(AudioFileClip(os.path.join(self.path, filename)))
        else:
            self.files_audio.append(AudioFileClip(self.path))
        return self.files_audio

    def files_scanner_images(path, dur):    
        if (os.path.isdir(self.path)):
                for i in os.listdir(self.path):
                    print(i)
                for i, filenames in enumerate(os.listdir(self.path)):
                    filesList.append(ImageClip(os.path.join(path, filenames), ismask=False, transparent=True, fromalpha=False, duration=dur))
        else:
            self.filesList.append(ImageClip(self.path), ismask=False, transparent=True, fromalpha=False, duration=dur)
        return self.filesList

if __name__ == "__main__":
    print("Use it in script!")