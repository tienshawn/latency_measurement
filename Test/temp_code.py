import cv2
import subprocess
from pyzbar.pyzbar import decode, ZBarSymbol
import sys
import cv2
import time
import threading

rtmp_url = "rtmp://localhost/live/stream"

path_video = "/home/tienshawn1/Downloads/output_bigger_barcode.mp4"
cap = cv2.VideoCapture(path_video)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

command = ['ffmpeg', '-re',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-i', '-',
           '-f', 'flv',
           rtmp_url]

p = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=True)
images = []
i = 0
while True:
    success, img = cap.read()
    if not success:
        break 
    data = {
        'image':img,
        'time':time.monotonic()
    }
    images.append(data) 
    p.stdin.write(img.tobytes())

old_stdout = sys.stdout
log_file = open("TestCode.log","w")
sys.stdout = log_file
path = '/home/tienshawn1/Desktop/Latency_Code/Image'

for i in data:
    decoded_data = decode(i['image'])[0].data.decode("utf-8")
    print("frame: ", decoded_data, "time: ", i['time'])

cap.release()
sys.stdout = old_stdout
log_file.close()