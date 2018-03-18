
#!/bin/bash
OUTDIRNAME="$1/encoded/"
# mkdir $DIRNAME
for i in $(ls $1 | egrep "mp4|avi");
do 
 ffmpeg -i $1/$i -acodec aac -vcodec libx264 -strict experimental -tune fastdecode $OUTDIRNAME+$i+"_vegas-enc.mp4"
done

# Making an octopus merge