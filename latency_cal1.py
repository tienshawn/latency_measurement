import cv2
import subprocess
from pyzbar.pyzbar import decode
import cv2
import time
from queue import Queue, Empty, Full
from threading import Thread
import logging

logging.basicConfig(filename='Delay_Data.log', filemode='a', level=logging.INFO,
                    format='frame: %(frame_value)s - time: %(time_value)s')

rtmp_url = "rtmp://localhost/live/stream"

path_video = '/latency_measurement/input.mp4'
cap = cv2.VideoCapture(path_video)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# command = ['ffmpeg', '-re',
#            '-y',
#            '-f', 'rawvideo',
#            '-vcodec', 'rawvideo',
#            '-pix_fmt', 'bgr24',
#            '-s', "{}x{}".format(width, height),
#            '-i', '-',
#            '-f', 'flv',
#            rtmp_url]
# width = 480
# height = 360
command = ['ffmpeg', '-re', '-analyzeduration', '1', '-probesize', '32',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-i', '-',
           '-f', 'flv',
           rtmp_url]
#ffmpeg -re -analyzeduration 1 -probesize 32 -i "rtmp://$SOURCE_RTMP_URL/live/stream" -s "$resolution" -f flv rtmp://localhost/live/stream -loglevel quiet -stats 2> app.txt

p = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=True)
# p_transcoder = subprocess.Popen(command_transcoder, stdin=subprocess.PIPE, stderr=True)
def get_data(queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            decoded_data = decode(item['image'])[0].data.decode("utf-8")
            time = item['time']
            logging.info('', extra={'frame_value': f'{decoded_data}', 
                                    'time_value': f'{time}'})

def stream_data():
    while True:
        success, img = cap.read()
        if not success:
            break 
        p.stdin.write(img.tobytes())

stream_data()
# get_data_thread.start()

    


    

