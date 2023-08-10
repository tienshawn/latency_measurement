import zxingcpp
from PIL import Image
import sys
import cv2
import time

old_stdout = sys.stdout
log_file = open("Data_Processing/zxingcpp_Frame_Time.log","w")
sys.stdout = log_file

cap = cv2.VideoCapture("rtmp://localhost/live/stream")

while True:
    success, img = cap.read()
    if not success:
        break

    results = zxingcpp.read_barcodes(img)
    for r in results:
        print("frame: ", r.text, "- time: ", time.monotonic())


cap.release()

sys.stdout = old_stdout

log_file.close()