FROM ubuntu:20.04
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    tzdata && \
    apt install -y python3 python3-pip && \
    apt install -y libgl1-mesa-glx && \
    apt install -y ffmpeg

RUN apt-get update && \
    apt install build-essential libpcre3 libpcre3-dev libssl-dev wget unzip zlibc zlib1g zlib1g-dev nano -y

RUN mkdir nginxDL && \
    cd nginxDL &&\
    wget http://nginx.org/download/nginx-1.16.1.tar.gz &&\
    tar -zxvf nginx-1.16.1.tar.gz

RUN cd nginxDL &&\
    wget https://github.com/sergey-dryabzhinsky/nginx-rtmp-module/archive/dev.zip && \
    unzip dev.zip

RUN cd ./nginxDL/nginx-1.16.1 &&\
    ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-dev &&\
    make &&\
    make install

COPY nginx.conf /usr/local/nginx/conf/nginx.conf

RUN /usr/local/nginx/sbin/nginx

RUN apt-get update && \
    pip install opencv-python 

RUN apt-get install -y libzbar0 && \
    pip install pyzbar && \
    pip install configargparse

RUN mkdir latency_measurement


COPY latency_cal1.py /latency_measurement
COPY input.mp4 /latency_measurement

COPY nginx.sh /latency_measurement
RUN cd latency_measurement && \
    chmod +x nginx.sh

WORKDIR /latency_measurement
EXPOSE 1935
CMD ["sh","./nginx.sh"]