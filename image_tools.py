import random
from moviepy.video.fx.all import *
from moviepy.editor import *

def add_rand_placed_image(clip, imageClip):
	xCoord = random.randint(0, clip.w)
	yCoord = random.randint(0, clip.h)
	imageClip = imageClip.resize(width=clip.w/3)
	clipOut = (CompositeVideoClip([clip, imageClip.set_pos((xCoord, yCoord))])
					.add_mask()
					.set_duration(clip.duration))
	return clipOut