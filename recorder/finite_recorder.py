import infinite_recorder
import multiprocessing
import time
import os
import subprocess
import argparse



if __name__ == '__main__': 

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-l', '--length', type=int,
        help='')
    parser.add_argument(
        '-i', '--iterations', type=int,
        help='how much iterate?')
    args = parser.parse_args()

    try:
        for i in range(args.iterations):
            filename = time.strftime("%I%M%S%m%S") + ".wav"        
            cmd = 'python3 f:/git/Weedeeo/recorder/infinite_recorder.py -d 1 f:\\YandexDisk\\Muswork\\sounddevice_out\\{}'.format(filename)
            Proc = subprocess.Popen(cmd) 
            time.sleep(args.length + 1)
            Proc.terminate()
            # Proc.sendcontrol('c')

    except KeyboardInterrupt:
        print('\nRecording finished')
        quit()
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))