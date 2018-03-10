# CUTSIZE = 10
# clip = VideoFileClip("medved.mp4")
# clip = VideoFileClip("E:/Windows.old/Users/Cmmndr/Videos/Sources/Krutoe_pike.mp4")
# clip2 = VideoFileClip("AVGN 137 - The Crow.mp4")
# files = [f for f in os.listdir('./shaker/') if os.path.isfile(f)]
# .rotate(180)
# duration = int(clip.duration/2)
# duration2 = int(clip2.duration/4)
	'''
	if duration < length, length is duration
	При таком подходе он никогда не будет брать точки дальше чем length
	Надо сделать так, чтобы length ограничивал только разность между точками 
	Я уже заменил length на duration, только теперь надо ограничить точки.
	Если сделать duration - length не будет работать, если наоборот - то не будет кадров за пределами последовательности
	В любом случае надо duration, а как ограничить length - вопрос. Сначала выбираешь 2 точки, если разность между ними =< 4 - аппендишь в массив
	'''

# print(generate_sequence(clip, 10))
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

# clipRandom.write_videofile("./" + write_data + "-out.mp4",fps=25,codec='mpeg4')
# cut_frames = sorted([random.randint(0, duration), random.randint(0, duration // 2)])
# print(type(cut_frames))
# print(cut_frames)
# clip_in = clip.subclip(min(rand1_1,rand1_2), max(rand1_1,rand1_2))
# clip1Seq = generate_sequence(clip, 10)
# clip2Seq = generate_sequence(clip2, 5)
# Разнести всю эту тему по модулям