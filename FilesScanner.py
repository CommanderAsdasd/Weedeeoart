# -*- coding: utf-8 -*-

from moviepy.editor import *
from moviepy.video.fx.all import *
import os
import time
import random
import sys
import re
import logging

class FilesScanner():

    # TODO loging
    def __init__(self, path):
        self.files_video = []
        self.files_audio = []
        self.files_images = []
        self.sourceFile = []
        self.path = path

    def randclip(self, maxclips=1):
        return random.randint(0, maxclips)

    def scan_video(self):
        formats = re.compile("mp4$|avi$|webm$|m2t$|gif$")
        try:
            if (os.path.isdir(self.path)):
                for i, filename in enumerate(os.listdir(self.path)):
                    if (formats.match(filename.split(".")[-1])):
                        logging.info("Videofile {}".format(filename))
                        self.files_video.append(VideoFileClip(os.path.join(self.path, filename)))
            else:
                    self.files_video.append(VideoFileClip(self.path))
        except Exception as Err:
                    logging.debug("error occured: {}".format(Err))
        return self.files_video

    def scan_audio(self):
        formats = re.compile("wav$|mp3$")
        if (os.path.isdir(self.path)):
            for i, filename in enumerate(os.listdir(self.path)):
                if (formats.match(filename.split(".")[-1])):
                    logging.info("Audiofile {}".format(filename))
                    self.files_audio.append(AudioFileClip(os.path.join(self.path, filename)))
        else:
            self.files_audio.append(AudioFileClip(self.path))
        return self.files_audio

    def scan_images(self, dur):
        formats = re.compile("png$|jpg$|jpeg$")    
        if (os.path.isdir(self.path)):
            for i, filename in enumerate(os.listdir(self.path)):
                if (formats.match(filename.split(".")[-1])):
                    self.files_images.append(ImageClip(os.path.join(self.path, filename), ismask=False, transparent=True, fromalpha=False, duration=dur))
                    logging.debug("Image object: {}".format(filename))
        else:
            self.files_images.append(ImageClip(self.path), ismask=False, transparent=True, fromalpha=False, duration=dur)
        return self.files_images

if __name__ == "__main__":
    print("Use it in script!")