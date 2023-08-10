import zxing
import sys
import cv2
import time

old_stdout = sys.stdout
log_file = open("Data_Processing/Frame_with_Time.log","w")
sys.stdout = log_file

cap = cv2.VideoCapture("rtmp://localhost/live/stream")
abc = [1,2,3]
while True:
    success, img = cap.read()
    if not success:
        break

    reader = zxing.readbarcode()
    barcode = reader.decode("rtmp://localhost/live/stream")
    print("frame: ", barcode.parsed, "time: ", time.monotonic())

cap.release()

sys.stdout = old_stdout

log_file.close()

#cannot read realtime image, only path
    
# reader = zxing.BarCodeReader()
# print(reader.zxing_version, reader.zxing_version_info)

# def barcode_reader(img):
#     barcode = reader.decode(img)
#     print(barcode.parsed)
# img = "/home/tienshawn1/Downloads/barcode (1).png"
# barcode_reader(img)
# for i in range (100):
#     img = "/home/tienshawn1/Desktop/Latency_Code/Code/new_code"+str(i)+".png"
#     barcode_reader(img)

#bug: cannot read number ending with 7
#bug solved: resize the barcode