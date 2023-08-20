**LATENCY MEASUREMENT TOOL FOR STREAMING FUNCTION SERVICE**

***Implementation of the tool***
1. The source_streaming container:
- The source streaming function is inside the container *tienshawn/latency:1.4* .The container itself will log the frame/ time with a rate of 48 frames per sample.
- Inside the container the frame-time will be log under the name *source.log*. It will look like this:
frame: 00000000 - time: 2018249.863058621   (frame 0)
frame: 00000482 - time: 2018251.762237232   (frame 48)
frame: 00000963 - time: 2018253.683992296   (frame 96)
frame: 00001441 - time: 2018255.608781408   (frame 144)
frame: 00001922 - time: 2018257.522894028   (frame 192)
frame: 00002400 - time: 2018259.442135818   (frame 240) (the last number in the frame is the checksum, omit it)

2. The transcoder container:
- Then we will run the transcoder container. Get inside the transcoder container using *docker exec -it <name_container> /bin/bash*, then execute the transcode command using ffmpeg (it's inside the *nginx.sh* file)
- REMEMBER to export the port of container to the host (like *-p 1937:1935*)
      *ffmpeg -re -analyzeduration 1 -probesize 32 -i rtmp://<source-container-ip>/live/stream -vf scale=1280:720 -f flv rtmp://localhost/live/stream*

3. The host:
- Simutaneously, run the python script *main_calculate.py* on the host. Get the port that the transcoder container uses to export to the host.
- Change the *rtmp_url* with the port respectively.
For example, if you use *-p 1937:1935* in running the container command, so the *rtmp_url* will be 
*rtmp://localhost:1937/live/stream*
- The frame - time value will be log in the *transcoder.log* file in the host.

- When it's done, go inside the source_streaming container to get the data (using *docker exec* command). The frame - time data will be stored inside the *source.log*. Cat the file, copy the data into a file in the host, name it *source.log*
- So we have 2 log file, *source.log* and *transcoder.log*
- Run the python script *process_log.py*.
- The delay data will the stored in the *Delay_history.log*. And the frame - time data will be saved in csv format in the *Lateny_Data_excel* folder

Finally!!!!!!
      