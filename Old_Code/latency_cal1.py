import cv2
import subprocess
from pyzbar.pyzbar import decode
import time
from queue import Queue, Empty, Full
from threading import Thread
import logging

logging.basicConfig(filename='source.log', filemode='a', level=logging.INFO,
                    format='frame: %(frame_value)s - time: %(time_value)s')


rtmp_url = 'rtmp://localhost/live/stream'

path_video = '/latency_measurement/input.mp4'
cap = cv2.VideoCapture(path_video)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

command = ['ffmpeg', '-re',
           '-stream_loop', 
           '1',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-i', '-',
           '-f', 'flv',
           rtmp_url]


p = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=True)

def put_data(queue, data):
    try:
        queue.put(data)
    except:
        queue.clear()   

def stream_data():
    last = 0
    current = -1
    while True:
        current += 1
        success, img = cap.read()
        if not success:
            break 
        data = {
            'image':img,
            'time':time.monotonic()
        }
        p.stdin.write(img.tobytes())
        if current == 0:
            last = current
            put_data(queue, data)
            continue

        if (current - last == 48):
            put_data(queue, data)
            last = current
            continue
        else: continue    

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


queue = Queue()
stream_data_thread = Thread(
    target=stream_data, 
    args=()
)

get_data_thread = Thread(
    target=get_data,
    args=(queue,)
)

stream_data_thread.start()
get_data_thread.start()

    


    

