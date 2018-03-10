import ffmpeg
import time


def ffmpeg_parsefile(seq=[0, 10]):
	write_data = time.strftime("%I%M%S")
	in_file = ffmpeg.input('020937-out.mp4')
	overlay_file = ffmpeg.input('Nu_da_kek.mp4')
	for i in seq:
		(ffmpeg
		    .concat(
		        in_file.trim(start_frame=seq[i], end_frame=seq[i-1]).overlay(overlay_file.hflip()),
		        in_file.trim(start_frame=seq[i-2], end_frame=seq[i-3]).drawbox(50, 50, 120, 120, color='red', thickness=5),
		    )	    
		    .output("./" + write_data + "-ff-out.mp4")
		    .run()
		)

ffmpeg_parsefile([0,5,7,9,11,5,4])