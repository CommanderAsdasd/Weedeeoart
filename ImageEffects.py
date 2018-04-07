import moviepy
import random
from moviepy.editor import *
import time
import logging

class ImageEffects():

    def __init__(self):
        self.sequences_altered = []

    
    
    def take_stills(self):
        pass

    def compose_for_transitions_2(self, chance=50, separate=True):
        if hasattr(self, 'sequences_video'):
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    immediate_clip1 = self.sequences_video[i].resize(height=540, width=960)
                    immediate_clip2 = random.choice(self.sequences_video).resize(height=540, width=960)
                    clip1_duration = immediate_clip1.duration
                    clip2_duration = immediate_clip2.duration
                    if clip1_duration < clip2_duration:
                        immediate_clip2.set_duration(clip1_duration)
                    elif clip1_duration > clip2_duration:
                        immediate_clip1.set_duration(clip2_duration)
                    if separate:
                        self.sequences_altered.append(CompositeVideoClip([immediate_clip1.set_pos(("left", "bottom")), immediate_clip2.set_pos(("right", "top"))], size=(1920,1080)))
                    else:
                        self.sequences_video[i] = CompositeVideoClip([immediate_clip1.set_pos(("left", "bottom")), immediate_clip2.set_pos(("right", "top"))], size=(1920,1080))


    def compose_for_transitions_4(self, chance=50, separate=True):
        if hasattr(self, 'sequences_video'):
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    immediate_clips = []
                    clip_durations = []
                    positions = [("left", "bottom"), ("left", "top"), ("right", "top"), ("right", "bottom")]
                    immediate_clips.append(self.sequences_video[i])
                    for randclip_count in range(3):
                        immediate_clips.append(random.choice(self.sequences_video))
                    for clip in immediate_clips: 
                        clip_durations.append(clip.duration)
                    min_duration = min(clip_durations)
                    for clip in immediate_clips:
                        if clip.duration > min_duration:
                            clip.set_duration(min_duration)
                    for posclip_count, pos in enumerate(positions):
                        immediate_clips[posclip_count] = immediate_clips[posclip_count].resize(height=540, width=960).set_pos(pos)
                    # self.sequences_video[i] = CompositeVideoClip([immediate_clip1.set_pos(0, 540), immediate_clip2.set_pos(960, 0)], size=(1920,1080))
                    # logging.debug(pos)
                    # logging.debug(immediate_clips)
                    if separate:
                        self.sequences_altered.append(CompositeVideoClip(immediate_clips, size=(1920,1080)))
                    else:
                        self.sequences_video[i] = CompositeVideoClip(immediate_clips, size=(1920,1080))


    def broken_but_fun_compose(self, chance=50):
        if hasattr(self, 'sequences_video'):
             for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    immediate_clip1 = self.sequences_video[i].resize(height=1920/2, width=1080/2)
                    immediate_clip2 = random.choice(self.sequences_video).resize(height=1980/2, width=1080/2)
                    clip1_duration = immediate_clip1.duration
                    clip2_duration = immediate_clip2.duration
                    if clip1_duration < clip2_duration:
                        immediate_clip2.set_duration(clip1_duration)
                    elif clip1_duration > clip2_duration:
                        immediate_clip1.set_duration(clip2_duration)
                    self.sequences_video[i] = CompositeVideoClip([immediate_clip1.set_pos("left", "bottom"), immediate_clip2.set_pos("right", "top")], size=(1920,1080))

        else:
            logging.info("no video and audio sequences provided")
