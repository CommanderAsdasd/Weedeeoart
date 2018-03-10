# -*- coding: utf-8 -*-
# C:/Python27/python.exe
import random
from moviepy.editor import *
from moviepy.video.fx.all import *


def generate_rand_sequence_complicated(processClip, minLength=1, maxLength=1, startPoint=0):
	duration = processClip.duration
	if maxLength > duration:
		maxDuration = duration
	else:
		maxDuration = maxLength
	if minLength > maxDuration:
		minLength = maxDuration
		endPoint = minLength
	else:
		startPoint = random.uniform(startPoint, maxDuration - minLength)
		endPoint = startPoint + minLength
	# points.append(startPoint)
	# points.append(endPoint)
	if (endPoint - startPoint < minLength):
		endPoint = minLength
	if (endPoint - startPoint > maxDuration):
		endPoint = maxDuration
	print(startPoint, endPoint)
	# sequence = processClip.subclip(min(points), max(points))
	sequence = processClip.subclip(startPoint, endPoint)
	return sequence

def generate_rand_sequence_complicated(processClip, minLength=1, maxLength=1, startPoint=0):
	duration = processClip.duration
	print(duration)
	if (minLength > duration): # || maxLength < minLength || maxLength > duration) :
		minLength = duration
	if (maxLength < minLength):
		maxLength = minLength
	if (maxLength > duration):
		maxLength = duration
	points = []
	points.append(random.uniform(startPoint, duration))
	points.append(random.uniform(startPoint, duration))
	print(points)
	cuttedDuration = max(points) - min(points) 
	startPoint = min(points)
	endPoint = max(points)
	if (cuttedDuration < minLength):
		endPoint = cuttedDuration + (minLength - cuttedDuration)
	if (cuttedDuration > maxLength):
		endPoint = cuttedDuration - (maxLength - cuttedDuration)
	print(startPoint, endPoint)
	sequence = processClip.subclip(startPoint, endPoint)
	return sequence

def generate_rand_sequence2(processClip, minLength, startPoint=0):
	'''returns video objects instance'''
	# Да у меня в старом варианте все клипы были фиксированной длины, а это не прикольно. По сути можно взять старый вариант, и сделать так, что оно будет в пределах этой длины. minLength - Ограничитель длины, если сделать его вариативным, типа random, если > - то присваиваю его длине
	# Безобразный код на самом деле, эндпоинт ничем не ограничен
	# 
	points = []
	duration = processClip.duration
	if minLength > duration:
		minLength = duration
	startPoint = random.uniform(start, duration)
	endPoint = startPoint + minLength
	points.append(startPoint)
	points.append(endPoint)
	print(points)
	sequence = processClip.subclip(min(points), max(points))
	return sequence

def generate_rand_sequence(processClip, minLength, clipLength):
	'''returns video objects instance'''
	# В этом нет никакого смысла, потому что точки задаются в самом конце. Мой эндпоинт на самом деле не эндпоинт. Поэтому надо присвоить их, а уж потом обращаться как [0] и [1]
	# it's good
	duration = processClip.duration
	if minLength > duration:
		minLength = duration
	point1 = random.uniform(minLength, clipLength)
	# point2 = random.uniform(minLength, clipLength)
	point2 = point1 + clipLength
	if point2 > duration:
		point2 = duration
	if point1 == point2:
		point1 = 0
	pointsClip = [min(point1, point2), max(point1, point2)]
	# if duration < clipLength:
	# 	clipLength = duration
	# pointPlus = random.uniform(minLength, clipLength)
	if (pointsClip[1] > duration):
		pointsClip[1] = duration
	# else:
	# 	endPoint = startPoint + pointPlus
	# if (endPoint > duration):
	# 	endPoint = duration
	print(pointsClip)
	sequence = processClip.subclip(pointsClip[0], pointsClip[1])
	return sequence

if __name__ == "__main__":
	print("Use it in script!")