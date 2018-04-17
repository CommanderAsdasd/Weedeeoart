import ffmpeg
import sys

stream = ffmpeg.input(sys.argv[1])
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)