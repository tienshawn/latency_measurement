Latency Measurement Tools for Streaming Function Services

* Step 1: Get the Frame - Time data
    - Use the video with barcode embedded as input
    - Specify the url of the video streaming, feed as input into the code in /Measurement Code/ folder
    Output of the code will be a file containing decoded barcode information and the time it receives the barcode.
    - For the time being, /lib_pyzbar/ can be used

* Step 2: Process the data
    - Move to the /Data_Processing/ folder. Now move the 2 log files into the folder. 
    - Specify the path of the log files in the /data_into_excel.py/
    - Delay will be calculated, printed in the console
    - If you want to get those values into Excel, call the function /data_into_excel/

Hope you like it! Enjoy!