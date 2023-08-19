import re
import pandas as pd
from datetime import date

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
log1 = 'source_1.log'
frame1, time1, count1 = data_processing(log1)

log2 = 'transcoder_1.log'
frame2, time2, count2 = data_processing(log2)

time1_excel = []
time2_excel = []
delay_value = []
for i in range(count1):
    for j in range(count2):
        if (frame1[i] == frame2[j]):
            delay_value.append(time1[i] - time2[j])
            time1_excel.append(time1[i])
            time2_excel.append(time2[j])

fps_avg = []
for i in range(1,count1):
    fps_avg.append(time1(i) - time1(i-1))

fps_value = sum(fps)


def data_into_excel():
    output_file = 'Data_Check.xlsx'        
    df = pd.DataFrame()
    df['Time 1'] = time1_excel
    df['Time 2'] = time2_excel

    df.to_excel(output_file, index=False)

delay_final = sum(delay_value) / len(delay_value)
# with open("Delay_history.log", 'a') as d:
#     string = "Delay: " + str(delay_final) + " - Date: " + str(date.today().strftime("%d/%m/%Y")) + "\n"
#     d.write(string)

