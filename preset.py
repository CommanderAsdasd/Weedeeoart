'''TODO: make json instead of code configs'''


from Weedeeo import *


def preset_manager(clipPath, count):
    for i in range(count):
        random_shortz(clipPath)

def random_shortz(clipPath):
<<<<<<< Updated upstream
    Editor = Weedeeo(clipPath, scantype='recur', sources_count=1)
    Editor.shuffle_video(0.5,1,4)
    # Editor.apply_filter_framerand()
    Editor.opacity_mixing(opacity=0.7, separate=False)
    # Editor.compose_for_transitions_2(chance=50, separate=False)
    # Editor.set_filter(filter_name="EMBOSS")
    Editor.apply_filter(chance=10)
    try:
        Editor.symmetrizer(chance=75)
    except Exception as e:
        logging.debug("can't symmetrize effects, error is \"{}\"".format(e))
    # try:
    #     Editor.speed_changer(minspeed=0.8, maxspeed=1.5, chance=50)
    # except Exception as e:
    #     logging.debug("can't speed change, error is \"{}\"".format(e))
    try:
        Editor.reverser_sas(chance=100, time=0.5)
    except Exception as e:
        logging.debug("can't reverser_sas, error is \"{}\"".format(e))
    try:
        Editor.reverser()
    except Exception as e:
        logging.debug("can't reverse, error is \"{}\"".format(e))
    Editor.reshuffle()
    Editor.write_video(size=(640, 320))
=======
    Editor = Weedeeo(clipPath, scantype='recur')
    Editor.shuffle_video(1,2,2)
    # Editor.apply_filter_framerand()
    Editor.opacity_mixing(opacity=0.5)
    Editor.reshuffle()
    # Editor.set_filter(filter_name="CONTOUR")
    Editor.apply_filter()
    Editor.write_video(size=(1280, 720))
    Editor.compose_for_transitions_2(chance=40)
>>>>>>> Stashed changes

def video_preset(clipPath):
    Editor = Weedeeo(clipPath, scantype='recur')
    # if editor.clips_video > 5:
    # 	editor.shuffle_video(1,3,1)
    # 	editor.shuffle_video(0.1,0.5,4)
    # else:
        # editor.shuffle_images(0.1,0.3,5)
        # editor.chop_sequences('./chop.json')
        # editor.chop_clips('./jsons/kaput.json')
    # editor.shuffle_video(0.5,0.9,5)
    Editor.shuffle_video(0.1,1,1)
    # editor.compose_for_transitions_4(chance=100)
    # Editor.compose_for_transitions_2(chance=5)
    # Editor.shuffle_video(1,2,1) # cool 1-second preset
        # editor.time_warper(80)
        # editor.clips_wall(chance=50)
        # editor.shuffle_audio(1,3,1)
        # editor.uncareful_mixing(chance=75)
        # editor.careful_mixing(chance=25)
    # try:
    #     Editor.symmetrizer(chance=75)
    # except Exception as e:
    #     logging.debug("can't time effects, error is \"{}\"".format(e))
    # try:
    #     Editor.speed_changer(minspeed=0.8, maxspeed=1.5, chance=50)
    # except Exception as e:
    #     logging.debug("can't time effects, error is \"{}\"".format(e))
    # try:
    #     Editor.reverser_sas(chance=100, time=0.5)
    # except Exception as e:
    #     logging.debug("can't time effects, error is \"{}\"".format(e))
    # try:
    #     Editor.reverser()
    # except Exception as e:
    #     logging.debug("can't time effects, error is \"{}\"".format(e))
    # Editor.set_filter(filter_name="CONTOUR")
    # Editor.apply_filter()
    # Editor.apply_filter()
    # Editor.apply_filter_framerand()
    # editor.shuffle_video(0.1,2,10)
    # editor.shuffle_audio(1,3,10)
    # editor.write_audio()
    Editor.reshuffle()
    Editor.write_video()
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
    # preset_manager(sys.argv[1])
    print('use main.py instead')