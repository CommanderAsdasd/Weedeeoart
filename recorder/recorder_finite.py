import recorder_finite
import multiprocessing
import time
import os
import subprocess
import argparse

def recorder_run(iterations=1, length=1, session_name="default"):
    try:
        for i in range(iterations):
            filename = time.strftime("%I%M%S%m%S") + session_name + ".wav"
            print("f:\\YandexDisk\\Muswork\\sounddevice_out\\{}".format(filename))      
            cmd = 'python3 f:/git/Weedeeo/recorder/recorder_infinite.py -d 1 "f:\\YandexDisk\\Muswork\\sounddevice_out\\{}"'.format(filename)
            Proc = subprocess.Popen(cmd) 
            time.sleep(length + 1)
            Proc.terminate()
            # Proc.sendcontrol('c')

    except KeyboardInterrupt:
        print('\nRecording finished')
        quit()
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-l', '--length', type=int, default=1,
        help='')
    parser.add_argument(
        '-i', '--iterations', type=int, default=1,
        help='how much iterate?')
    parser.add_argument(
        '-s', '--session_name', type=str, default="default",
        help='session filename')
    args = parser.parse_args()
    try:
        recorder_run(args.iterations, args.length)
    except Exception:
        recorder_run()