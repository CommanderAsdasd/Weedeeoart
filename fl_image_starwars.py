# -*- coding: utf-8 -*-
# C:/Python27/python.exe

"""
Description of the video:
Mimic of Star Wars' opening title. A text with a (false)
perspective effect goes towards the end of space, on a
background made of stars. Slight fading effect on the text.

"""

import numpy as np
# from skimage import transform as tf

from moviepy.editor import *
from moviepy.video.tools.drawing import color_gradient
import pip
import moviepy
import moviepy.config

from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.4-Q16\\magick.exe"})

# print(moviepy)

pip.main(["install", "scikit-image"])

# RESOLUTION

w = 720
h = w*9/16 # 16/9 screen
moviesize = w,h



# THE RAW TEXT
txt = "\n".join([
"A long time ago, in a faraway galaxy,",
"there lived a prince and a princess",
"who had never seen the stars, for they",
"lived deep underground.",
"",
"Many years before, the prince's",
"grandfather had ventured out to the",
"surface and had been burnt to ashes by",
"solar winds.",
"",
"One day, as the princess was coding",
"and the prince was shopping online, a",
"meteor landed just a few megameters",
"from the couple's flat."
])


# Add blanks
txt = 10*"\n" +txt + 10*"\n"


# CREATE THE TEXT IMAGE



# clip_txt = TextClip(txt,color='white', align='West',fontsize=25,
#                     font='Xolonium-Bold', method='label')
imageTransform = ImageClip("../imgShaker/kBln55mIDH8.jpg")

# SCROLL THE TEXT IMAGE BY CROPPING A MOVING AREA

txt_speed = 27
fl = lambda gf,t : gf(t)[int(txt_speed*t):int(txt_speed*t)+h,:]
moving_image = imageTransform.fl(fl, apply_to=['mask'])


# ADD A VANISHING EFFECT ON THE TEXT WITH A GRADIENT MASK

# grad = color_gradient(moving_txt.size,p1=(0,2*h/3),
#                 p2=(0,h/4),col1=0.0,col2=1.0)
# gradmask = ImageClip(grad,ismask=True)
# fl = lambda pic : np.minimum(pic,gradmask.img)
# moving_txt.mask = moving_txt.mask.fl_image(fl)


# WARP THE TEXT INTO A TRAPEZOID (PERSPECTIVE EFFECT)
# Так, что ещё надо захуячить, этосамое, как его, надо вместо текстварпа сделать какое-то изменение изображения, типа, типа, блеадь, надо взять картинку и попробовать её поварпить, функция trapzWarp в принципе пойдёт, нужно мне что-то изменить типа 
# Эцсамое, apply_to("mask ")


def trapzWarp(pic,cx,cy,ismask=False):
    """ Complicated function (will be latex packaged as a fx) """
    Y,X = pic.shape[:2]
    src = np.array([[0,0],[X,0],[X,Y],[0,Y]])
    dst = np.array([[cx*X,cy*Y],[(1-cx)*X,cy*Y],[X,Y],[0,Y]])
    tform = tf.ProjectiveTransform()
    tform.estimate(src,dst)
    im = tf.warp(pic, tform.inverse, output_shape=(Y,X))
    return im if ismask else (im*255).astype('uint8')


fl_im = lambda pic : trapzWarp(pic,0.2,0.3)
fl_mask = lambda pic : trapzWarp(pic,0.2,0.3, ismask=True)
warped_img= moving_image.fl_image(fl_im)
warped_img.mask = moving_image.mask.fl_image(fl_mask)


# BACKGROUND IMAGE, DARKENED AT 60%

# stars = ImageClip('../../videos/stars.jpg')
# stars_darkened = stars.fl_image(lambda pic: (0.6*pic).astype('int16'))


# COMPOSE THE MOVIE

# final = CompositeVideoClip([
#          stars_darkened,
#          warped_txt.set_pos(('center','bottom'))],
#          size = moviesize)


# WRITE TO A FILE

# final.set_duration(8).write_videofile("starworms.avi", fps=5)

# This script is heavy (30s of computations to render 8s of video)
