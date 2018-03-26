#!/bin/bash
PROCPID=$!
DATE=`date '+%Y-%m-%d-%H%M%S'`

python3 Recording_example.py -d 1 "/f/YandexDisk/Muswork/sounddevice_out/$DATE.wav" &
 ( sleep 2; kill $PROCPID ) & echo $! &
 echo "PROCPID: $PROCPID" &
fg $PROCPID
