import ffmpeg
import time
import random

write_data = time.strftime("%I%M%S")
in_file = ffmpeg.input('020937-out.mp4')
in_file2 = ffmpeg.input('011932-out.mp4')
(ffmpeg
    .input('020937-out.mp4')
    .filter_('fps', fps=25, round='up')
    .concat(in_file, in_file2)
    .output('dummy233.mp4')
    .run()
)