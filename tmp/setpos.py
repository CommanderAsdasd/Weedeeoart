from moviepy.editor import *
H = 720
W = 1280
SIZE = (W, H)
HX = H + H * .10  # increase size 10%
WX = W + W * .10
bold_font = 'Liberation-Sans-Bold'
plain_font = 'Liberation-Sans'
img_1 = ImageClip("bbb.jpeg").set_duration(4).set_start(0).resize(height=H, width=W)   # 3-8
txt_1 = TextClip("title 1", font=bold_font, color='white', fontsize=64, interline=9).set_duration(2).set_start(1).set_pos(('right', 360)).crossfadein(.3)
stxt_1 = TextClip("sub title 1", font=plain_font, color='white', fontsize=80, interline=9).set_duration(1.5).set_start(1.5).set_pos(('right', 440)).crossfadein(.3)
img_2 = ImageClip("aaa.jpg").set_duration(8).set_start(4).resize(height=H, width=W)   # 3-8
# look the img_2's set_duration and set_start,the same as txt_2 and stxt_2
txt_2 = TextClip("title 2", font=bold_font, color='white', fontsize=64, interline=9).set_duration(7).set_start(4.5).set_pos(('right', 360)).crossfadein(.3)
stxt_2 = TextClip("sub title 2", font=plain_font, color='white', fontsize=80, interline=9).set_duration(6).set_start(5.5).set_pos(('right', 440)).crossfadein(.3)

slide_1 = CompositeVideoClip([img_1, txt_1, stxt_1]).set_duration(4)
slide_2 = CompositeVideoClip([img_2, txt_2, stxt_2]).set_duration(8)

clips = [slide_2, slide_1]
final_clip = CompositeVideoClip(clips, size=SIZE).set_duration(8)
final_clip.write_videofile("video.mp4", fps=12, audio_codec="aac")