from moviepy.editor import *
from moviepy.video.fx.all import *
import os

def files_scanner(path):
	files = os.listdir(path)
	filesList = []
	sourceFile = []
	for i, filenames in enumerate(os.listdir(path)):
	    filesList.append(VideoFileClip(os.path.join(path, filenames)))
	return filesList

def files_scanner_audio(path):
	files = os.listdir(path)
	filesList = []
	sourceFile = []
	for i, filenames in enumerate(os.listdir(path)):
	    filesList.append(AudioFileClip(os.path.join(path, filenames)))
	return filesList

def files_scanner_ffmpeg(path):
	files = os.listdir(path)
	filesList = []
	sourceFile = []
	for i, filenames in enumerate(os.listdir(path)):
		filesList.append(filenames)
	return filesList

def files_scanner_images(path, dur):
	files = os.listdir(path)
	filesList = []
	sourceFile = []
	for i, filenames in enumerate(os.listdir(path)):
		filesList.append(ImageClip(os.path.join(path, filenames), ismask=False, transparent=True, fromalpha=False, duration=dur))
	return filesList