import cv2
import subprocess
from pyzbar.pyzbar import decode, ZBarSymbol
import sys
import cv2
import time

old_stdout = sys.stdout
log_file = open("Streaming_Barcode.log","w")
sys.stdout = log_file

rtmp_url = "rtmp://localhost/live/stream"

path = "/home/tienshawn1/Downloads/output(bigger_barcode).mp4"
cap = cv2.VideoCapture(path)


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

while True:
    success, img = cap.read()
    if not success:
        break 

    decoded_data = decode(img)[0].data.decode("utf-8")
    print("frame: ", decoded_data, "time: ", time.monotonic())     

    p.stdin.write(img.tobytes())
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
sys.stdout = old_stdout
log_file.close()