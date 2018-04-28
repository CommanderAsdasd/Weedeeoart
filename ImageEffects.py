import moviepy
import random
from moviepy.editor import *
from PIL import ImageFilter
from PIL import Image
import PIL.Image as PILImage
from scipy import ndimage
import numpy as np
import time
import logging
import wand as wnd
import wand.image as WndImage
# import StringIO
import io

class ImageEffects():

    
    def __init__(self):
        self.sequences_altered = []
        self.filters = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SMOOTH", "SMOOTH_MORE", "SHARPEN"]
        self.choosen_filter = None
        # self.lowerBound = int(min(self.insert_bound1.get(), self.insert_bound2.get()))
        # self.upperBound = int(max(self.insert_bound1.get(), self.insert_bound2.get()))
        self.lowerBound = 1
        self.upperBound = 5

    def make_dummy(self):
        blob = io.BytesIO()
        width = self.Clip.w
        height = self.Clip.h
        image = PILImage.new("RGB", (width, height), (0,0,0,0))
        draw = ImageDraw.Draw(image)
        draw.ellipse((10,10,300,300), fill="red", outline="red")
        del draw
        image.save(blob, format='JPEG')
        return image

    def rescaler(self, img):
        blob = io.BytesIO()
        with WndImage.Image(blob=img) as img:
            img.format = 'jpeg'
            size = img.size
            coefBounds = range(self.lowerBound, self.upperBound)
            coef_x = random.choice(coefBounds)
            coef_y = random.choice(coefBounds)
            if random.choice((0, 1)) == 0:
                ch = ('div', 'mul')
                x_size = size[0]//coef_x
                y_size = size[1]//coef_y
            else:
                ch = ('mul', 'div')
                x_size = size[0]//coef_x
                y_size = size[1]//coef_y
            img.liquid_rescale(x_size, y_size)
            img.sample(size[0], size[1])
            print(size[0], size[1])
            img_bin = img.make_blob('jpeg')
            blob = io.BytesIO(b'{}'.format(img_bin))
        return blob


    def _wand_image_adaptor(self, imarray):
        blob = io.BytesIO()
        inpImage = PILImage.fromarray(imarray, 'RGB')
        inpImage.save(blob, format='JPEG')
        blob2 = self.rescaler(blob.getvalue())
        blob2.seek(0)
        img = PILImage.open(blob2)
        imarray = np.fromstring(img.tobytes(), dtype=np.uint8)
        try:
            imarray = imarray.reshape((img.size[1], img.size[0], 3))
        except ValueError as err:
            print(str(err))
            img = self.make_dummy()
            imarray = np.fromstring(img.tobytes(), dtype=np.uint8)
            imarray = imarray.reshape((img.size[1], img.size[0], 3))
            # print(imarray)
            # imarray = 0
        return imarray

    def _filter(self, inpImage):
        logging.debug("Trying to apply filter: {}".format(self.choosen_filter))
        im_array = inpImage
        choosen_filter = getattr(ImageFilter, self.choosen_filter)
        inpImage = Image.fromarray(inpImage, 'RGB')
        inpImage = inpImage.filter(choosen_filter)
        imArr = np.fromstring(inpImage.tobytes(), dtype=np.uint8)
        imArr = imArr.reshape((inpImage.size[1], inpImage.size[0], 3))
        logging.debug("Filter applied: {}".format(self.choosen_filter))
        return imArr
        # else:
        #     logging.info("No correct filter choosed, current value is " + self.choosen_filter)

    def _filter_frame_rand(self, inpImage):
        '''randomly chooses filter every frame'''
        im_array = inpImage
        randFilter = getattr(ImageFilter, random.choice(self.filters))
        logging.info("Using random filter "+ str(randFilter))
        inpImage = Image.fromarray(inpImage, 'RGB')
        inpImage = inpImage.filter(randFilter)
        imArr = np.fromstring(inpImage.tobytes(), dtype=np.uint8)
        imArr = imArr.reshape((inpImage.size[1], inpImage.size[0], 3))
        return imArr

    def _set_duration_shortest(self, clips):
        clip_durations = []
        for clip in clips:
            clip_durations.append(clip.duration)
        min_duration = min(clip_durations)
        for clip in clips:
            if clip.duration > min_duration:
                logging.debug("set {} to {} duration".format(clip, clip.duration))
                clip.set_duration(min_duration)

    def set_filter(self, filter_name=""):
        change_flag = 0
        for filter_names in self.filters:
            if filter_name == filter_names:
                self.choosen_filter = filter_name
                logging.info("Filter changed, currently set " + self.choosen_filter)
                change_flag = 1
        if change_flag == 0:
            logging.info("Filter not changed, current filter is "+ self.choosen_filter)


    def apply_filter(self, chance=0):
        for i, clip in enumerate(self.sequences_video):
            if random.randint(0,100) <= chance and self.choosen_filter:
                logging.info("Use filter "+ self.choosen_filter)
                if self.choosen_filter == "CAS":
                    self.sequences_video[i] = clip.fl_image(self._wand_image_adaptor)
                else:
                    self.sequences_video[i] = clip.fl_image(self._filter)


    def apply_filter_framerand(self, chance=50):
        for i, clip in enumerate(self.sequences_video):
            if random.randint(0,100) <= chance:
                # logging.info("Use random filter on {}".format(, clip))
                self.sequences_video[i] = clip.fl_image(self._filter_frame_rand)


    def take_stills(self):
        pass

    def opacity_mixing(self, chance=50, separate=True, opacity=0.5):
        if hasattr(self, 'sequences_video'):
            for i, pointerVideo in enumerate(self.sequences_video):
                if random.randint(0,100) <= chance:
                    immediate_clip1 = self.sequences_video[i]
                    immediate_clip2 = random.choice(self.sequences_video)
                    self._set_duration_shortest(clips=[immediate_clip1, immediate_clip2])
                    if separate:
                        self.sequences_altered.append(CompositeVideoClip([immediate_clip1, immediate_clip2.resize(width=immediate_clip1.w, height=immediate_clip1.h).set_opacity(opacity)]))
                    else:
                        self.sequences_video[i] = CompositeVideoClip([immediate_clip1, immediate_clip2.set_opacity(opacity)])

    def random_compoziting(self):
        pass



    def compose_for_transitions_2(self, chance=50, separate=True):
        '''separate appends resulting video to another list, if set to False composed video may be taken for composing again, cool fractals resulting'''

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

if __name__ == "__main__":
    # logging.info("Seem")
    print("Seems working correctly")