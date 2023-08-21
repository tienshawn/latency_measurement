#!/bin/bash
echo "Source_streaming Container Bash"

#Run the source_streaming container
docker run -itd --rm --ip 172.17.0.2 -p 1936:1935  --name source tienshawn/latency:1.4 
sleep 50
docker cp source:latency_measurement/source.log /home/tienshawn1/Desktop 
cat source.log
docker stop source

