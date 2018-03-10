# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

# from moviepy_effetcs import *
from generate_sequence import *
from files_scanner import *
from text_tools import *

class VideoEditor():
	pass

def test():
	pass


# =======================================================================OUT====================================
path = '../shaker/'
print(files_scanner_video(path))
exec_numb = 5
dur = []
# Такую хуйню можно слепить воедино сделав панно из идей и объединять их, можно даже делать им разноцветный бэкграунд
textEffects = ["Blur", "Mirror", "BlackCircle", "Fractal", "DoubleFace", "Glitchface", "crystallize", "маскирование фона", "pixelate", "face swap", "Заедание части", "Многократная картинка", "мультирендеринг", "телевизор", "Вылезание персонажа", "Datamosh", "Reflecting", "Текст программы", "EyeSize char"]
audioEffectsText = ["8bit", "EarRape", "Somatik", "Музпуп", "Звук удара", "Ретровейв"]
sourceParts = ["AVGN in TV", "Крутое пике", "Коммандор-зайчик", "Пакет с дерьмом", "Смешивание персонажей", "dyhanie.mp4", "Заедание джойстика", "Rebyata.mp4", "Ожидал внезапных ударов", "синтезаторы", "Закон не позволяет реверсить", "Либо - движение утки"]
memesText = ["Pepe", "БлэдНэвэльный", "У меня лапки"]
ideasAdder = ["Скопировать идеи в такие листы", "Смешивать программу со списком идей", "Список функций и частей программы перемешивать", "Сделать изображение меньше относительно видеоклипа"]

def randclip(maxclips):
	return random.randint(0, maxclips)

def add_text(textList):
	textIterate = random.randint(0, len(textEffects)-1)
	clips[i] = add_rand_placed_text(clips[i], textList[textIterate])

def cut_logic(exec_numb):
	clips = []
	print(clips)
	clipsList = files_scanner_video(path)
	clipsCounter = len(clipsList) - 1
	for i, objects in enumerate(clipsList[::1]):
		for j in range(0,3):
		# clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 5))
			# clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 4))
			clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, random.uniform(1, 4)))
			# clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
			# clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 5))
			clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, random.uniform(1, 3)))
			clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
			# clips.append(generate_sequence(clipsList[randclip(clipsCounter)], [6.7, 6.8])
	for i, objects in enumerate(clips):
		# pass
		# if i % 3 == 0:
			# clips[i] = supersample(clips[i], 1, 3)
	# 	clips[i] = mirror_x(clips[i])
		# if i % random.randint(3, 4) == 0:
		# 	clips[i] = speedx(clips[i], 0.5)
		# if i % 3 == 0:
		
		# textSub = TextClip('Lol')
		# clips[i] = add_still_placed_text(clips[i])


		textIterate = random.randint(0, len(sourceParts)-1)
		clips[i] = add_rand_placed_text(clips[i], sourceParts[textIterate])
		textIterate = random.randint(0, len(audioEffectsText)-1)
		clips[i] = add_rand_placed_text(clips[i], audioEffectsText[textIterate])
		textIterate = random.randint(0, len(memesText)-1)
		clips[i] = add_rand_placed_text(clips[i], memesText[textIterate])
		textIterate = random.randint(0, len(memesText)-1)
		clips[i] = add_rand_placed_text(clips[i], ideasAdder[textIterate])
		# if i % random.randint(2, 3) == 0:
		# 	clips[i] = time_symmetrize(clips[i])
		# try:
		# 	if i < len(clips)-5:
		# 		clips.append(clips_array([[clips[i], clips[i+1]],
	 #                          [clips[i+3], clips[i+4]]]))
		# except:
		# 	pass
	concat_and_write(clips, exec_numb)

def resulst_store(clips, exec_numb):
	pass

def concat_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	try:
		clipOut = concatenate_videoclips(clips, method='compose')
		clipOut.write_videofile("./" + write_data + "-out.mp4",fps=25)
	except Exception as e:
		print(str(e))
		print("An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			cut_logic(exec_numb)
		else:
			print("game over")


cut_logic(exec_numb)