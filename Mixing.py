# -*- coding: utf-8 -*-
import random

class Mixing():

    def __init__(self):
        pass

    def careful_mixing(self, chance=50):
        '''this method randmoly choose item from sequences_audio and append it to sequences_video due to chance variable.
        Audio/video sync'''
        if (hasattr(self, 'sequences_audio')) and (hasattr(self, 'sequences_video')):
            sequences_video = self.sequences_video
            sequences_audio = self.sequences_audio
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    pointerAudio = random.choice(sequences_audio)
                    print('DEBUG pointer is point on audio:', pointerAudio)
                    video_duration, audio_duration = sequences_video[i].duration, pointerAudio.duration
                    # How to rewrite it to .set_end
                    if video_duration > audio_duration:
                        pointerVideo = sequences_video[i].subclip(0, audio_duration)
                    elif video_duration < audio_duration:
                        pointerAudio = pointerAudio.subclip(0, video_duration)
                    # logging.debug('DEBUG AUDIO IS EXIST: {}'.format(pointerAudio))
                    sequences_video[i] = pointerVideo.set_audio(pointerAudio)
        else:
            logging.info("This method requires both audio and video providing")

    def uncareful_mixing(self, chance=50):
        '''Audio/video async'''
        if (hasattr(self, 'sequences_audio')) and (hasattr(self, 'sequences_video')):
            sequences_video = self.sequences_video
            sequences_audio = self.sequences_audio
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    pointerAudio = random.choice(sequences_audio)
                    video_duration, audio_duration = sequences_video[i].duration, pointerAudio.duration
                    # if video_duration > audio_duration:
                    #     pointerVideo = sequences_video[i].subclip(0, audio_duration)
                    # elif video_duration < audio_duration:
                    #     pointerAudio = pointerAudio.subclip(0, video_duration)
                    logging.debug('DEBUG AUDIO IS EXIST: {}'.format(pointerAudio))
                    sequences_video[i] = pointerVideo.set_audio(pointerAudio)
        else:
            logging.info("This method requires both audio and video providing")