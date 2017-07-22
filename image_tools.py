import random
from moviepy.video.fx.all import *
from moviepy.editor import *
from files_scanner import *

def add_rand_placed_image(clip, printText):
	imageFile = TextClip(printText, font='Amiri-regular',fontsize= 20, stroke_color='black', color='white')
	# clipSize = []
	# clipSize.append(clip.w)
	# clipSize.append(clip.h)
	xCoord = random.randint(0, clip.w)
	yCoord = random.randint(0, clip.h)
	clipOut = (CompositeVideoClip([clip,textString.set_pos((xCoord, yCoord))])
					.add_mask()
					.set_duration(clip.duration))
	return clipOut

# def add_still_placed_text(clip):
# 	textSub = TextClip('Lol',font='Amiri-regular',fontsize=120)
# 	clipOut = (CompositeVideoClip([clip,textSub.set_pos((100,180))])
# 	               .add_mask()
# 	               .set_duration(3)
# 	               .crossfadein( 0.5)
# 	               .crossfadeout( 0.5))
# 	return clipOut

# print(add_rand_placed_text("test"))