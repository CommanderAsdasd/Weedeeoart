# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
from moviepy.video.VideoClip import *
import random
import time
from PIL import ImageFilter
from PIL import Image
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import *

# from moviepy_effetcs import *
from refactor.generate_sequence import *
from files_scanner import *
from image_modules.testing_pillow import *
from scipy import ndimage
import numpy, math



class VideoEditor():
	pass

def test():
	pass


# =======================================================================OUT====================================
path = '../shaker/'
print(files_scanner_video(path))
exec_numb = 5

# clips.append(generate_rand_sequence(clipsList[0], 5, 4))
dur = []

def replace_pixels(inpImage):
	# print(type(image))
	# for i in image:
	# 	if image.any() % random.randint(2,6) == 0:
	# 		image.reshape()
	# numpy.set_printoptions(threshold=numpy.nan)
	# image = image[:,:,[0,2,1]]
	print(type(inpImage))
	xData = inpImage[[400],:,:][0]
	yData = inpImage[[400],:,:][0]
	print("x data is %d", xData)
	inpImage = np.array([xData, yData, [4, 5, 4]], np.uint8)

	# for i in inpImage:

	print(inpImage)
	return inpImage
	# break
	# return image

def PIL_framerand_filters(inpImage):
	print("Effecting")
	filters = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SMOOTH", "SMOOTH_MORE", "SHARPEN"]
	randFilter = getattr(ImageFilter, random.choice(filters))
	im_array = inpImage
	inpImage = Image.fromarray(inpImage, 'RGB')
	inpImage = inpImage.filter(randFilter)
	imArr = numpy.fromstring(inpImage.tobytes(), dtype=np.uint8)
	imArr = imArr.reshape((inpImage.size[1], inpImage.size[0], 3))
	return imArr



def scroll(get_frame, t):
    """
    This function returns a 'region' of the current frame.
    The position of this region depends on the time.
    """
    frame = get_frame(t)
    frame_region = frame[int(t):int(t)+360,:]
    return frame_region

def randclip(maxclips):
	return random.randint(0, maxclips)

def cut_logic(exec_numb):
	clips = []
	print(clips)
	clipsList = files_scanner_video(path)
	clipsCounter = len(clipsList) - 1
	for i, objects in enumerate(clipsList[::5]):
		# for j in range(0,3):
		# clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 5))
			# clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 4))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, random.uniform(1, 4)))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
		clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 5))
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, random.uniform(1, 3)))
			# clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
			# clips.append(generate_sequence(clipsList[randclip(clipsCounter)], [6.7, 6.8])
	for i, objects in enumerate(clips):

		if i % 3 == 0:
			clips[i] = mirror_x(clips[i])
			if i % random.randint(3, 4) == 0:
				clips[i] = speedx(clips[i], 0.5)
			if i % random.randint(1, 5) == 0:
			# textSub = TextClip('Lol')
				clips[i] = (clips[i].fl_image(PIL_framerand_filters))
			# pass
			# if i % random.randint(2, 3) == 0:
			# 	clips[i] = time_symmetrize(clips[i])

	concat_and_write(clips, exec_numb)

def resulst_store(clips, exec_numb):
	pass

def concat_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	for i, clip in enumerate(clips):
		clips[i] = clips[i].resize( (1920, 1080) )
	try:
		clipOut = concatenate_videoclips(clips, method='compose')
		clipOut.write_videofile("./output_video/" + write_data + "-out.mp4",fps=25)
	except Exception as e:
		print(str(e))
		print("An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			cut_logic(exec_numb)
		else:
			print("game over")


cut_logic(exec_numb)
"""
# Чета он вызывает не то, какую-то хуйню, пытается из "instance" отнять in
t# Потом надо потренироваться в композиции и
# Нужно сорганизовать всё это в структуру. Что будет неизменным, а что поменяется? Неизменным будет обращение к функции crop-a, а переменным - параметры, которые в неё передаются. Чтобы можно было вызывать рандомное количество склеек, точнее, склейки происходили в некое случайное время и склеивались в одну структуру. Должен объявляться некий список, в который подаётся случайное количество значений. Генерируется какое-то число случайных значений от нуля до конца клипа.
# Нужно сделать несколько секвенций, а ещё сделать
# как я в последний раз решил эту проблему с дюрейгенами, в какой-то либе метод отрабатывал не по видосу, а по интегеру, 
# Придумать прикольные числовые последовательон 
	Ещё надо намутить не, не то. Надо намутить эцсамое, балин, ща, надо сделать что-то для удобства, такую фичу, не то завернуть в классы, не то, а, даты прихуярить.
	Нужнна какая-то другая логика, типа "берёшь случайный кусочек видео и вставляешь его в случайное место(лол)" - для этого надо знать длительность клипа, потом выбрать нижнее значение, верхнее, вырезаешь, а потом надо 3 промежутка видео - от 0 до cut_low, cut_low-cut_top, cut_top-clip.Duration
- Лучше всего попробовать передавать туплами в функцию

# Можно потренироваться в паттернах добавив разные. Можно сделать 
Структуры данных
"""
