# -*- coding: utf-8 -*-

from moviepy.editor import *
from moviepy.video.fx.all import *
import os
import time
import random
import sys
import re
import logging
import glob

class FilesScanner():

    def __init__(self, path, sources_count):
        self.clips_video = []
        self.clips_audio = []
        self.clips_images = []
        self.sourceFile = []
        self.path = path
        self.sources_count = sources_count
        if os.path.isdir(path):
            self.path_data = os.listdir(path)
        self.video_formats = ["mp4", "avi", "webm", "m2t", "gif", "mov"]
        self.audio_formats = ["wav", "mp3"]
        # self.image_formats = re.compile("png$|jpg$|jpeg$") 

    def add_video(self, path):
        # if (formats.match(filename.split(".")[-1])):
        try:
            self.clips_video.append(VideoFileClip(path))
        except Exception as e:
            logging.debug("Can't add videofile, error: {}".format(e))
        #os.path.join(self.path, filename)
    
    def add_audio(self,path):
        try:
            self.clips_audio.append(AudioFileClip(path))
        except Exception as e:
            logging.debug("Can't add videofile, error: {}".format(e))

    def randclip(self, maxclips=1):
        return random.randint(0, maxclips)

    def scan_video(self, list_files):
        try:
            if (os.path.isdir(self.path)):
                for i, filename in enumerate(list_files):
                    add_video()
            else:
                    self.clip_video.append(VideoFileClip(self.path))
        except Exception as Err:
                    logging.debug("error occured: {}".format(Err))
        return self.clip_video

    def scan_audio(self, list_files):
        try:
            if (os.path.isdir(self.path)):
                for i, filename in enumerate(list_files):
                    add_audio()
            else:
                    self.clip_audio.append(AudioFileClip(self.path))
        except Exception as Err:
                    logging.debug("error occured: {}".format(Err))
        return self.clip_video

    def scan_audio_deprecated(self):
        # formats = 
        if (os.path.isdir(self.path)):
            for i, filename in enumerate(os.listdir(self.path)):
                if (formats.match(filename.split(".")[-1])):
                    logging.info("Audiofile {}".format(filename))
                    self.clip_audio.append(AudioFileClip(os.path.join(self.path, filename)))
        else:
            self.clip_audio.append(AudioFileClip(self.path))
        return self.clip_audio

    def scan_images(self, dur):         
        if (os.path.isdir(self.path)):
            for i, filename in enumerate():
                if (formats.match(filename.split(".")[-1])):
                    self.clip_images.append(ImageClip(os.path.join(self.path, filename), ismask=False, transparent=True, fromalpha=False, duration=dur))
                    logging.debug("Image object: {}".format(filename))
        else:
            self.clip_images.append(ImageClip(self.path), ismask=False, transparent=True, fromalpha=False, duration=dur)
        return self.clip_images

    def video_crawler(self):
        files = []
        for extension in self.video_formats:
            for filename in glob.iglob(self.path + '**/*.{}'.format(extension), recursive=True):
                files.append(filename)
        if len(files) > 0:
            for i in range(self.sources_count):
                file_to_add = random.choice(files)
                logging.debug('added file {}'.format(file_to_add))
                self.add_video(file_to_add)
                # return self.clips_video

    def audio_crawler(self):
        files = []
        for extension in self.audio_formats:
            for filename in glob.iglob(self.path + '**/*.{}'.format(extension), recursive=True):
                files.append(filename)
        if len(files) > 0:
            for i in range(self.sources_count):
                file_to_add = random.choice(files)
                logging.debug('added file {}'.format(file_to_add))
                self.add_audio(file_to_add)

    def random_crawler(self, video=True, audio=True, images=True):
        if video:
            self.video_crawler()
        if audio:
            self.audio_crawler()

        

if __name__ == "__main__":
    print("Use it in script!")