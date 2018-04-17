import ffmpeg


#ffmpeg -i vidui.mkv -c:v libx264 -c:a ac3 -crf 20 -map 0:0 -map 0:4 vidui.mp4
#ffmpeg -i VIDEO.mkv
# ffmpeg -i vidui.mkv -c:v libx264 -c:a ac3 -crf 20 -map 0:0 -map 0:4 vidui.mp4
in_file = ffmpeg.input(sys.argv[1])
in_file.trim(start ='00:02:00', end='00:03:30'),
in_file.output('out.mp4')
