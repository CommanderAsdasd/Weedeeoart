# -*- coding: utf-8 -*-
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
# from datetime import *
import time

class VideoEditor():
	pass

CUTSIZE = 10
# clip = VideoFileClip("medved.mp4")
clip = VideoFileClip("E:/Windows.old/Users/Cmmndr/Videos/Sources/Cutted/Matrix_pills.mp4")
clip2 = VideoFileClip("AVGN 137 - The Crow.mp4")
# .rotate(180)
# duration = int(clip.duration/2)
# duration2 = int(clip2.duration/4)

def generate_sequence(processClip, length):
	'''
	if duration < length, length is duration
	При таком подходе он никогда не будет брать точки дальше чем length
	Надо сделать так, чтобы length ограничивал только разность между точками 
	Я уже заменил length на duration, только теперь надо ограничить точки.
	Если сделать duration - length не будет работать, если наоборот - то не будет кадров за пределами последовательности
	В любом случае надо duration, а как ограничить length - вопрос. Сначала выбираешь 2 точки, если разность между ними =< 4 - аппендишь в массив
	'''
	points = []
	duration = processClip.duration
	if duration < length:
		length = duration
	passed = False
	while passed <> True:
		point1 = random.uniform(0, duration)
		point2 = random.uniform(0, duration)
		if abs(point1 - point2) < 4:
			points.append(point1)
			points.append(point2)
			passed = True
	sequence = processClip.subclip(min(points), max(points))

	return sequence

# print(generate_sequence(clip, 10))

def test():
	pass

'''
# эта херня примет клип и ожидаемую длительность, и вернёт какую-нить секвенцию в рамках клипа
- ща заколбашу туда выдачу готового куска клипа, зачем эти полумеры с флоатами
'''
# print(str(duration) + "\n")
# b = [random.randint(0, 5) for i in range(0, duration)]
# print(b)
# clipsList = range(0,CUTSIZE)
# clip = crop(clip, x1=50, y1=60, x2=460, y2=275)
# clip = freeze_region(clip, t=3, region=(30,30,200,300))
# clip = freeze_region(clip, t=3, region=(30,30,250,400))
# clip = even_size(clip)
# clip = speedx(clip, factor=0.7)
# print(clipsList)
# for i in range(0,CUTSIZE):
# 	# keyframes = sorted([random.randint(0, duration/(CUTSIZE/duration)), random.randint(0, duration/4)])
# 	# keyframes = sorted([random.randint(0, duration/2), random.randint(0, duration/4)])
# 	# clipsList[i] = clip.subclip(0, 0.6)
# 	# if i < CUTSIZE - 1:
# 		clipsList[i-1] = clip.subclip(random.randint(0, duration), random.randint(0, duration))
# # clip = painting(clip, 1.4, 0.006)
# # print(x)
write_data = time.strftime("%I%M%S")
print(write_data)
# clipRandom.write_videofile("./" + write_data + "-out.mp4",fps=25,codec='mpeg4')
# cut_frames = sorted([random.randint(0, duration), random.randint(0, duration // 2)])
# print(type(cut_frames))
# print(cut_frames)
# clip_in = clip.subclip(min(rand1_1,rand1_2), max(rand1_1,rand1_2))
# clip1Seq = generate_sequence(clip, 10)
# clip2Seq = generate_sequence(clip2, 5)
clips = []
for i in range(0,5):
	# clips.append(generate_sequence(clip, 1.90))
	clips.append(generate_sequence(clip, i + random.uniform(0, 4)))
	for x in xrange(0,6):
		clips.append(generate_sequence(clip2, random.uniform(0, 0.1)))
		clips.append(generate_sequence(clip, i + random.uniform(0, 3)))
		clips.append(generate_sequence(clip2, random.uniform(0, 3)))


# clip_in = generate_sequence(clip, 1.90)
# clip_in2 = generate_sequence(clip2, 5)
clipOut = concatenate_videoclips(clips)
clipOut.write_videofile("./" + write_data + "-out.avi",fps=25,codec='libx264',audio_codec='pcm_s16le')

"""
# Потом надо потренироваться в композиции и
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
