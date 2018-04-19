import ffmpeg


#ffmpeg -i vidui.mkv -c:v libx264 -c:a ac3 -crf 20 -map 0:0 -map 0:4 vidui.mp4
in_file = ffmpeg.input(sys.argv[1])
overlay_file = ffmpeg.input('overlay.png')
(ffmpeg
    .concat(
        in_file.trim(start ='00:00:02', end='00:00:03'),
        in_file.trim(start_frame=30, end_frame=40),
    )
    .overlay(overlay_file.avgblur())
    .drawbox(50, 50, 120, 120, color='red', thickness=5)
    .output('out.mp4')
    .run()
)