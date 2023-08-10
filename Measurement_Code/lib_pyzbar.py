from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
import sys
import cv2
import time
import configargparse

def parser_args():
    parser = configargparse.ArgParser(description="NFV FIL HUST",
                            formatter_class=configargparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-s", "--ip_add", 
                        help="source stream path")
    parser.add_argument("-name", "--name",
                        help="name_logfile")
    return parser.parse_args()

#parser init
args = parser_args()
ip = args.ip_add
name = args.name
file_name = f'{name}.log'


old_stdout = sys.stdout
log_file = open(file_name, "w")
sys.stdout = log_file

url = f'rtmp://{ip}/live/stream'
cap = cv2.VideoCapture(url)

while True:
    success, img = cap.read()
    if not success:
        break

    cv2.imwrite(str(time.monotonic())+'.jpg',img)


    # decoded_data = decode(img)[0].data.decode("utf-8")
    # print("frame: ", decoded_data, "time: ", time.monotonic())



# for i in range (100):
#     img = "/home/tienshawn1/Desktop/Latency_Code/Code/new_code"+str(i)+".png"
#     barcode_reader(img)

cap.release()

sys.stdout = old_stdout

log_file.close()