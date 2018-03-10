from moviepy.editor import *
from moviepy.video.fx.all import *
import os
import time
import random
import sys

def randclip(maxclips):
    return random.randint(0, maxclips)

def files_scanner_video(path):
	for i in os.listdir(path):
		print(i)
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

def concat_and_write(clips, exec_numb):
    write_data = time.strftime("%I%M%S")
    print(write_data)
    for i, clip in enumerate(clips):
    	clips[i] = clips[i].resize( (1920, 1080) )
    try:
	    clipOut = concatenate_videoclips(clips, method='compose')
	    clipOut.write_videofile(sys.argv[1] + "/" + write_data + "-out.mp4", fps=25)
    except Exception as e:
        print(str(e))
        print("An error occured, try {} times".format(exec_numb))
        if exec_numb > 0:
            exec_numb -= 1
            # cut_logic(exec_numb)
        else:
            print("game over")

if __name__ == "__main__":
	print("Use it in script!")