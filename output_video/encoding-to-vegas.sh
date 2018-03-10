DIRNAME="./encoded/"
mkdir $DIRNAME
for i in $(ls ./ | egrep "mp4|avi");
do 
 ffmpeg -i $i -acodec aac -vcodec libx264 -strict experimental -tune fastdecode $DIRNAME+$i+"_vegas-enc.mp4"
done
