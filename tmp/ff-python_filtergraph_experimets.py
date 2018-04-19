import ffmpeg
import sys

#ffmpeg -i vidui.mkv -c:v libx264 -c:a ac3 -crf 20 -map 0:0 -map 0:4 vidui.mp4
in_file = ffmpeg.input(sys.argv[1])
# overlay_file = ffmpeg.input('overlay.png')
(ffmpeg
    .concat(
        in_file.trim(start='00:00:02', end='00:00:03'),
    #     in_file.trim(start='00:00:12', end='00:00:15'),
    )
    .filter_(filter_name='bbox')
    .filter_(filter_name='crystalizer')
    # .filter_('crystalizer')
    .output('out.mp4')
    .run()
)