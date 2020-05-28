FROM ubuntu:18.04


RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
RUN apt-get install  -y \
	build-essential \
	apt-utils \
	ca-certificates \
	wget \
	git \
	vim \
	libssl-dev \
	curl \
	unzip \
	unrar 

COPY baserequirements.txt baserequirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r baserequirements.txt
ADD code_controller /root/ 
WORKDIR  /root/
RUN ["chmod", "+x", "script.sh"]
ENTRYPOINT  /root/script.sh




