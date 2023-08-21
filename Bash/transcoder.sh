#!/bin/bash
echo 'Transcoder Bash'

#Run the transcoder container
sleep 5
#ip=$(docker inspect \
#  -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' source)
# export SOURCE_RTMP_URL="$(getent hosts $SOURCE_STREAM_SERVICE | awk '{ print $3 ;exit }')"
# echo "exported url of source streaming: $SOURCE_RTMP_URL"
docker run -itd --rm --name transcoder --ip 172.17.0.1 -p 1937:1935 hctung57/transcoder:1.1.1
docker exec transcoder /bin/bash -c 'ffmpeg -re -analyzeduration 1 -probesize 32 -i rtmp://172.17.0.2/live/stream -vf scale=1280:720 -f flv rtmp://localhost/live/stream' 
docker stop transcoder

