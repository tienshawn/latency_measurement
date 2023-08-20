from pyzbar.pyzbar import decode, ZBarSymbol
import sys
import cv2
import time
import configargparse
import logging
import threading

logging.basicConfig(filename='source.log', filemode='a', level=logging.INFO,
                    format='frame: %(frame_value)s - time: %(time_value)s')

ip_source = 'localhost:1936'
url_source = f'rtmp://{ip_source}/live/stream'
cap_source = cv2.VideoCapture(url_source)

ip_transcoder = 'localhost:1937'
url_transcoder = f'rtmp://{ip_transcoder}/live/stream'
cap_transcoder = cv2.VideoCapture(url_transcoder)

def catch_delay(cap):
  while True:
      success, img = cap.read()
      if not success:
          break
      try: 
        decoded_data = decode(img)[0].data.decode("utf-8")
        time1 = str(time.monotonic())
      
        logging.info('', extra={'frame_value': f'{decoded_data}', 
                                        'time_value': f'{time1}'})
      except:
        continue

if __name__ =="__main__":
  source_thread = threading.Thread(target=catch_delay, args=(cap_source,))
  transcoder_thread = threading.Thread(target=catch_delay, args=(cap_transcoder,))

  source_thread.start()
  transcoder_thread.start()

