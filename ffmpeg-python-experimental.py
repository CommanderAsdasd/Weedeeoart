import ffmpeg
import time
import random


def ffmpeg_parsefile(colorVal, seq=[0, 10]):
	write_data = time.strftime("%I%M%S")
	in_file = ffmpeg.input('020937-out.mp4')
	# overlay_file = ffmpeg.input('Nu_da_kek.mp4')
	for i in seq:
		(ffmpeg
		    .concat(
		        # in_file.trim(start_frame=seq[i], end_frame=seq[i-1]).overlay(overlay_file.hflip()),
		        # in_file.trim(start_frame=seq[i-2], end_frame=seq[i-3]).filter_("colorchannelmixer", 0.1, 0.1),
		        in_file.filter_("colorchannelmixer", 0.1, 0.1),
		    )	    
		    .output("./" + write_data + "-ff-out.mp4")
		    .merge_outputs()
		    .run()
		)

colorVal = []
for i in range(1,12):
	colorVal.append(round(random.uniform(0, 0.5), 3))
ffmpeg_parsefile(colorVal, [0,5,7,9,11,5,4])