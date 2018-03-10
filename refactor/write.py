# -*- coding: utf-8 -*-

def concat_and_write(clips=[], path="./", exec_numb, set_fps="25"):
	write_data = time.strftime("%I%M%S")
	try:
        if len(clips) == 0:
            print("no clips to write")
        else:
            clipOut = concatenate_videoclips(clips, method='compose')
            clipOut.write_videofile(path + write_data + "-cringe.mp4", fps=set_fps)
	except Exception as e:
		print(str(e))
		print("An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			cut_logic(exec_numb)
			exec_numb -= 1
		else:
			print("game over")

