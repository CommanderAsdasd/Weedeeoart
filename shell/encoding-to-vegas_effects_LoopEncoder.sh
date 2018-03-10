# It works!
DATE=`date +%d-%M-%H-%s`
In=$2
Out=$3
Outfile=$1+$DATE"_ffef_vegas-enc.mp4"
echo $Outfile
ffmpeg \
    -i $1 \
        -ss $In  -to $Out \
        -acodec aac -vcodec libx264 \
        -strict -2 \
        -filter_complex "\
            [0]drawbox=50:50:120:120:red:t=5[v0]"\
        -map [v0] \
        -map 0 \
        $1+$DATE"_ffef_vegas-enc.mp4"






