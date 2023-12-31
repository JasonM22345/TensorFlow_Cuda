# Created by Jason Mensah-Homiah, https://www.linkedin.com/in/jasonmh22345/
# 11/11/2023     Docker container for TensorFlow with CUDA
# Python

# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the "FilesToUpload" folder into the container at /app
COPY FilesToUpload /app

# Install some Python libraries
RUN pip install torch \
    && pip install keras \
    && pip install numpy \
    && pip install pandas \
    && pip install scipy

RUN pip install transformers

# Enable SSH access to the container
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

# Install other utilities
RUN apt-get install -y nano vim iproute2 net-tools
RUN apt-get install -y grep traceroute


# Install netcat
RUN apt-get install -y netcat

# Start terminal by default
CMD ["/bin/bash", "-c", "/usr/sbin/sshd && /bin/bash"]

