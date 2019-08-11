# Comment
# Data Science
# Editor: Jihwan Kim
# Email: super.jihwan@gmail.com


FROM mysql:latest AS jihwanK/


# apt update and install
RUN apt update
RUN apt install -y git
RUN apt install -y vim
RUN apt install -y python3
RUN apt install -y python3-pip

# make new directory
RUN mkdir /root/yelp

# git
RUN git clone https://github.com/jihwanK/data_science.git


# VOLUME: bind and mount directory
VOLUME [ "/data" ]


# EXPOSE: open ports to connect host
EXPOSE 80


# WORKDIR (directory that CMD runs)
# CMD (file or shell script that runs when container starts)