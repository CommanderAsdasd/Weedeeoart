# It works!
DATE=`date +%d-%M-%H-%s`
In="00:00:30"
Out="00:00:35"
Outfile=$1+$DATE"_ffef_vegas-enc.mp4"
echo $Outfile
ffmpeg \
    -i $1 \
    -i $2 \
        -ss $In  -to $Out \
        -acodec aac -vcodec libx264 \
        -af "aecho=0.8:0.88:60:0.4" \
        -strict -2 \
         -tune fastdecode \
        -filter_complex "\
            [0]trim=start_frame=10:end_frame=20[v0];\
            [0]trim=start_frame=30:end_frame=40[v1];\
            [v0][v1]concat=n=2[v2];\
            [1]hflip[v3];\
            [v2][v3]overlay=eof_action=repeat[v4];\
            [v4]drawbox=50:50:120:120:red:t=5[v5]"\
            -map [v5] \
            -map 0\
        $1+$DATE"_ffef_vegas-enc.mp4"





