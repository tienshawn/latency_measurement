#!/bin/bash
echo 'Delay Calculate and Rename Log file'

sleep 6
/bin/python3 /home/tienshawn1/Desktop/latency_measurement/process_log.py
sleep 6
time=$(date +"%d-%m-%Y..%H:%M:%S")
cd /home/tienshawn1/Desktop/Data
mkdir $time
cd ..
mv -t /home/tienshawn1/Desktop/Data/$time source.log transcoder.log
