# Comment
# Data Science
# Editor: Jihwan Kim
# Email: super.jihwan@gmail.com


FROM mysql:latest AS jihwanK/


# update apt
RUN apt update

# install software
RUN apt install -y git vim python3 python3-pip wget

# make new directory
RUN mkdir -p /root/yelp

# git
RUN git clone https://github.com/jihwanK/data_science.git


# VOLUME: bind and mount directory
VOLUME [ "/data" ]


# EXPOSE: open ports to connect host
EXPOSE 80


# WORKDIR (directory that CMD runs)
# CMD (file or shell script that runs when container starts)