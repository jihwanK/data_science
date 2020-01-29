# Data Science
# Editor: Jihwan Kim
# Email: jhwan1228@gmail.com


FROM ubuntu:latest


# update apt
RUN apt update

# install softwares
RUN apt install -y git vim python3 python3-pip wget
RUN pip3 install numpy pandas matplotlib

# Add User
RUN useradd jihwan -md /home/jihwan -s /bin/bash -p jihwan
RUN usermod -aG sudo jihwan
USER jihwan

# WORKDIR (directory that CMD runs)
WORKDIR /home/jihwan

# git
RUN git clone https://github.com/jihwanK/data_science.git

# VOLUME: bind and mount directory
# VOLUME [ "/data" ]

# EXPOSE: open ports to connect host
EXPOSE 80

# ENTRYPOINT (file or shell script that runs when container starts)
ENTRYPOINT [ "/bin/bash" ]