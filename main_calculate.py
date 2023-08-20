import cv2
import subprocess
from pyzbar.pyzbar import decode
import time
from queue import Queue, Empty, Full
from threading import Thread
import logging

logging.basicConfig(filename='transcoder.log', filemode='a', level=logging.INFO,
                    format='frame: %(frame_value)s - time: %(time_value)s')


rtmp_url = 'rtmp://localhost:1937/live/stream'
cap = cv2.VideoCapture(rtmp_url)


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
        if current == 0:
            last = current
            put_data(queue, data)
            continue

        if (current - last == 1):
            put_data(queue, data)
            last = current
            continue
        else: continue    

def get_data(queue):
    while True:
        item = queue.get()
        try:
            decoded_data = decode(item['image'])[0].data.decode("utf-8")
            time = item['time']
            logging.info('', extra={'frame_value': f'{decoded_data}', 
                                    'time_value': f'{time}'})
        except:
          continue



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

    


    

