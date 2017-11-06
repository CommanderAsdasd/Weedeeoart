# -*- coding: utf-8 -*-
import random
from moviepy.editor import *
from moviepy.video.fx.all import *

def generate_rand_sequence(processClip, minLength, clipLength):
	'''returns video objects instance'''
	points = []
	duration = processClip.duration
	if duration < clipLength:
		clipLength = duration
	startPoint = random.uniform(minLength, duration)
	endPoint = startPoint + clipLength
	points.append(startPoint)
	points.append(endPoint)
	print(points)
	sequence = processClip.subclip(min(points), max(points))
	return sequence

def generate_rand_sequence(processClip, minLength, clipLength):
	'''returns video objects instance'''
	points = []
	duration = processClip.duration
	if duration < clipLength:
		clipLength = duration
	startPoint = random.uniform(minLength, duration)
	endPoint = startPoint + clipLength
	points.append(startPoint)
	points.append(endPoint)
	print(points)
	sequence = processClip.subclip(min(points), max(points))
	return sequence

def generate_rand_inPlace_sequence(processClip, minLength, clipLength, times):
	points = []
	clips = []
	duration = clipLength
	if duration > processClip.duration:
		clipLength = duration
	for i in range(times):
		startPoint = random.uniform(minLength, duration)
		endPoint = startPoint + clipLength
		points.append(startPoint)
		points.append(endPoint)
		print(points)
		clips.append(processClip.subclip(min(points), max(points)))
	# sequence = concatenate_videoclips(clips, method='compose')
	# for i, objects in enumerate(clips):
		return clips





def generate_sequence(processClip, timecodes):
	'''retunrs list of video file objects'''
	points = []
	sequence = []
	if (type(timecodes) != list):
		raise Exception('sequence must be list of frames')

 	duration = processClip.duration
	for i, point in enumerate(timecodes[1::2]):
		if point > duration:
			point = duration
		points.append(timecodes[i])
		points.append(timecodes[i - 1])
		print(points)
		sequence.append(processClip.subclip(min(points), max(points)))
		points = []		
	return sequence

def generate_freeze(processClip, timecodes, times):
	points = []
	sequence = []
	if (type(timecodes) != list):
		raise Exception('"timecodes" must be list of frames')
 	duration = processClip.duration
	for i, point in enumerate(timecodes[1:]):
		if point > duration:
			point = duration
		points.append(timecodes[i])
		points.append(timecodes[i - 1])
		print(points)
		for i in range(0, times):
			print(points)
			sequence.append(processClip.subclip(min(points), max(points)))
			# sequence.append(processClip.subclip(, 2)) - короче тут идёт выбираиние самой большой точки и юзается только она. Это неправильно, надо использовать только лист из двух точек, не более
		points = []
	return sequence

def generate_ffmpeg_sequence(processClip, minLength, clipLength):
	duration = processClip.duration
	if duration < clipLength:
		length = duration
	point1 = random.uniform(minLength, duration)
	point2 = point1 + clipLength
	points.append(point1)
	points.append(point2)
	print(points)

def generate_ffmpeg_cutter_sequence(processClip, minLength, clipLength, duration):
	'''It returns to ffmpeg points'''
	points = []
	if duration < clipLength:
		clipLength = duration
	point1 = random.randint(minLength, duration)
	point2 = point1 + clipLength
	points.append(point1)
	points.append(point2)
	return points


	'''
	# Надо сделать так, чтобы секвенция принимала лист из точек и генерила с ним отрывки. Если количество нечётное, последняя точка обрезается. Если точка больше duration, её тоже не берём. 
	- 

	'''
if __name__ == "__main__":
	# generate_sequence(10, [20, 10])
	print("use it in script!")