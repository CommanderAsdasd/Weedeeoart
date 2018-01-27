DIRNAME="./encoded/"
mkdir $DIRNAME
for i in ./;
do 
 ffmpeg -i $i -acodec aac -vcodec libx264 -strict experimental -tune fastdecode $DIRNAME+$i+"_vegas-enc.mp4"
done
