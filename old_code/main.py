import wordmix_main
import sys
# import audio_synth_mixes_resized as au
# import refactor.one_file_wordmix
import refactor
import Good_random_glitches_experiments


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        audioPath = sys.argv[2]
        exec_numb = 5
        dur = []
        # wordmix_main.cut_logic(exec_numb, path)
        # au.cut_logic(exec_numb, path, audioPath)
        cut_logic(exec_numb)
        refactor.write()

    except IndexError as e:
        # print(str(e))
        print("please enter all needed path")