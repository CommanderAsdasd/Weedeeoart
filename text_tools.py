import random
from moviepy.video.fx.all import *
from moviepy.editor import *

# def add_rand_placed_text(clip):
	# textString = TextClip('Lol',font='Amiri-regular',fontsize=120, stroke_color='black', color='white')
	# # clipSize = []
	# # clipSize.append(clip.w)
	# # clipSize.append(clip.h)
	# # xCoord = random.randint(0, clipSize[0])
	# # yCoord = random.randint(0, clipSize[1])
	# clipOut = (CompositeVideoClip([clip, textString.set_pos((10, 120))])
					# .add_mask())
	# return clipOut

def add_rand_placed_text(clip):
	textSub = TextClip('Lol',font='Amiri-regular',fontsize=120)
	clipOut = (CompositeVideoClip([clip,textSub.set_pos((100,180))])
	               .add_mask()
	               .set_duration(3)
	               .crossfadein( 0.5)
	               .crossfadeout( 0.5))
	return clipOut

# print(add_rand_placed_text("test"))