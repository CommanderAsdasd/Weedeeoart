# It works!
DATE=`date +%d-%M-%H`
# OUTFILE=$1+$DATE+"_ffef_vegas-enc.mp4"
OUTFILE=$DATE+"_ffef_vegas-enc.mp4"
echo $OUTFILE
# ffmpeg -i $1 -vf "split [main][tmp]; [tmp] crop=iw:ih/2:0:0, vflip [flip]; [main][flip] overlay=0:H/2" -af "aecho=0.8:0.88:60:0.4" -acodec aac -vcodec libx264 -strict experimental -ss $2  -to $3 -tune fastdecode $1+$DATE"_ffef_vegas-enc.mp4"
ffmpeg -i $1 -acodec aac -vcodec libx264 -strict experimental -ss 01:00:30 -to 01:00:32 -tune fastdecode $OUTFILE
