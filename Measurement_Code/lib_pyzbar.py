from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
import sys
import cv2
import time

old_stdout = sys.stdout
log_file = open("Streaming_Barcode.log","w")
sys.stdout = log_file

cap = cv2.VideoCapture("rtmp://localhost/live/stream")

while True:
    success, img = cap.read()
    if not success:
        break

# def barcode_reader(img):
#     picture = Image.open(img)
    decoded_data = decode(img)[0].data.decode("utf-8")
    print("frame: ", decoded_data, "time: ", time.monotonic())



# for i in range (100):
#     img = "/home/tienshawn1/Desktop/Latency_Code/Code/new_code"+str(i)+".png"
#     barcode_reader(img)

cap.release()

sys.stdout = old_stdout

log_file.close()