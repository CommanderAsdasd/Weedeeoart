# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
# from moviepy.video.tools import segmenting
import random
import time

from generate_sequence import *
from files_scanner import *

class VideoEditor():
	pass

def test():
	pass


# =======================================================================OUT====================================
path = '../shaker/'
print(files_scanner(path))
write_data = time.strftime("%I%M%S")
print(write_data)

clips = []
clipsList = files_scanner(path)
# clips.append(generate_rand_sequence(clipsList[0], 5, 4))
print(clips)
dur = []

def randclip(maxclips):
	return random.randint(0, maxclips)

def clip_stacking(clipsList):
	pass


for i, objects in enumerate(clipsList):
	# clipsList[i].subclip(2, 4)
	clipsCounter = len(clipsList) - 1
	clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
	clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, i + random.uniform(1, 2)))
	clips.append(loop(generate_rand_sequence(clipsList[i], 1, 0.5), 5))
	clips.append(loop(generate_rand_sequence(clipsList[i], 1, 3), 5))
	# clips.extend(generate_sequence(clipsList[randclip(clipsCounter)], [6.7, 6.8]))



# Можно сделать штуку, которая раскладывает видеоряд на фрагменты, рендерит, применяет ко всем фильтры и снова их склеивает


for i, clip in enumerate(clips):
	# if i % 2 == 0:
	# 	if random.randint(0,2) == 2:
	# 		clips[i] = speedx(clips[i], 0.5)
	# 	else:
	# 		clips[i] = speedx(clips[i], 4)
	if i % 3 == 0:
		clips[i] = time_symmetrize(clips[i])





# Значит где-то внутри generate_freeze теряется инстанс и превращается в число.

# clip_in = generate_sequence(clip, 1.90)
# clip_in2 = generate_sequence(clip2, 5)
# print(clips)
# print(clips[0])
# clipOut.write_videofile("./" + write_data + "-out.avi",fps=25,codec='libx264',audio_codec='pcm_s16le')
print(clips)
clipOut = concatenate_videoclips(clips, method='compose')
clipOut.write_videofile("./" + write_data + "-out.mp4", fps=25)

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
