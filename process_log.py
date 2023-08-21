import re
import pandas as pd
from datetime import datetime
import os

def data_processing(logfile):
    with open(logfile) as f:
        lines = f.readlines()

        frame = []
        time = []
        count_frame = 0
        count_time = 0
        for line in lines:
            #frame exact
            frame_match = re.search(r"frame:([\d.]+)", line)
            if "frame:" in line:
                frame_value = line.split('frame:')[1].split()[0]
                try:
                    frame.append(int(frame_value[:-1]))
                    count_frame += 1
                except:
                    continue
            
            #time exact
            time_match = re.search(r"time:([\d.]+)", line)
            if "time:" in line:
                time_value = line.split('time:')[1].split()[0]
                time.append(float(time_value))
                count_time += 1

        if (count_frame == count_time):
            return frame, time, count_frame
        else:
            print("Error")

#Get the filename here
log1 = '/home/tienshawn1/Desktop/source.log'
frame1, time1, count1 = data_processing(log1)

log2 = '/home/tienshawn1/Desktop/transcoder.log'
frame2, time2, count2 = data_processing(log2)

time1_excel = []
time2_excel = []
diff_value = []
delay_final = []
for i in range(count1):
    for j in range(count2):
        if (frame1[i] == frame2[j] and time2[j] - time1[i] < 1):
            diff_value.append(time2[j]-time1[i])
            time1_excel.append(time1[i])
            time2_excel.append(time2[j])
            print(frame1[i], frame2[j])
            print("source:", time1[i], "-", "transcoder:", time2[j], "=", time2[j] - time1[i])

delay_final = sum(diff_value) / len(diff_value)
print(delay_final)

with open("Delay_history.log", 'a') as d:
    string = "Delay: " + str(delay_final) + " - Date: " + str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + "\n"
    d.write(string)

def data_into_excel():
    output_name = 'Data_'+str(datetime.now().strftime("%d-%m-%Y, %H:%M:%S")) +'.xlsx'  
    output_dir = './Latency_Data_excel'  
    if not os.path.exists(output_dir):  
        os.mkdir(output_dir)  
    output_file = os.path.join(output_dir, output_name)   

    df = pd.DataFrame()
    df['Time 1'] = time1_excel
    df['Time 2'] = time2_excel
    df['Diff'] = diff_value
    df['Delay'] = delay_final

    df.to_excel(output_file, index=False)

data_into_excel()

