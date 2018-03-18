
#!/bin/bash
OUTDIRNAME="$1/encoded/"
# mkdir $DIRNAME
if [[ -d $1 ]]; then
    for i in $(ls $1 | egrep "mp4|avi");
    do 
        ffmpeg -i $1/$i -acodec aac -vcodec libx264 -s 1920x1080 -q:v 1 -strict experimental -tune fastdecode $OUTDIRNAME+$i+"_vegas-enc.mp4"
    done
else
    ffmpeg -i $1 -acodec aac -vcodec libx264 -s 1920x1080 -q:v 1 -r 60 -strict experimental -tune fastdecode "$1_vegas-enc.mp4"
fi    