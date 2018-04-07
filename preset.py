from Weedeeo import *

def video_preset(editor, times=1):
    for i in range(times):
    	# if editor.clips_video > 5:
    	# 	editor.shuffle_video(1,3,1)
    	# 	editor.shuffle_video(0.1,0.5,4)
    	# else:
	        # editor.shuffle_images(0.1,0.3,5)
	        # editor.chop_sequences('./chop.json')
	        # editor.chop_clips('./jsons/kaput.json')
        # editor.shuffle_video(0.5,0.9,5)
        editor.shuffle_video(1,2,1)
        # editor.compose_for_transitions_4(chance=100)
        # editor.compose_for_transitions_2(chance=100)
	        # editor.shuffle_video(1,3,2) # cool 1-second preset
	        # editor.time_warper(80)
	        # editor.clips_wall(chance=50)
	        # editor.shuffle_audio(1,3,1)
	        # editor.uncareful_mixing(chance=75)
	        # editor.careful_mixing(chance=25)
        # try:
        #     editor.speed_changer(minspeed=0.3, maxspeed=2, chance=80)
        #     editor.reverser_sas(chance=100, time=2)
        #     editor.symmetrizer(chance=75)
        # except Exception as e:
        #     logging.debug("can't time effects, error is \"{}\"".format(e))
        # editor.shuffle_video(0.1,2,10)
        # editor.shuffle_audio(1,3,10)
        # editor.write_audio()
        # editor.reshuffle()
        editor.write_video()
        # editor.wirte_video_separate()
        # editor.wirte_audio_separate()

def audio_preset(editor):
    # editor.chop_clips('./jsons/kaput.json')
    editor.shuffle_audio(1,5,20)
    editor.shuffle_audio(1,2,10)
    # editor.speed_changer(minspeed=0.1, maxspeed=10, chance=80)
    editor.reverser(chance=20)
    # editor.symmetrizer(chance=75)
    editor.write_audio()
    # editor.write_video()

if __name__ == '__main__':
    i = 3
    editor1 = Weedeeo(sys.argv[1], type='recur')
    try:
        # audio_preset(editor1)
        video_preset(editor1)

    except Exception as e:
        if i >= 0: 
            print("Error occured")
            print(str(e))
            i -= 1
            video_preset(editor1)
        else:
            print("Exit")