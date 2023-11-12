# TensorFlow CUDA Test Docker Container

## Overview

The Python code `TF_CudaTest.py` is designed to test and demonstrate how TensorFlow works with CUDA. 
In this Docker container serves as a working alternative for users when TensorFlow CUDA is no longer available.

## Docker Container Details

### Requisites
- The Docker container already contains the necessary prerequisites for using TensorFlow with CUDA.
- Within the folder containing the Dockerfile, there is a folder named 'FilesToUpload'. 

The contents of this folder are automatically uploaded to the Docker container when building and running it. 
Users can place any code they want to run in this folder.


####### DESIGNED BY Jason Mensah-Homiah, https://www.linkedin.com/in/jasonmh22345/, 11/11/2023



### Software Availability
- The Docker container includes a fully operational version of Python, TensorFlow, Keras, NumPy, Pandas, and SciPy.
- Additional packages can be installed via pip in the container's command line.

### SSH Access
- SSH is available in the container, and users can access it with the following command:
  ```
  > ssh -p <port> <user>@<container_ip>
  ```
  Replace `<port>`, `<user>`, and `<container_ip>` with the appropriate values.

### Default Terminal
- The default terminal for the container is `/bin/bash`.

## Usage

1. **Build Docker Image:**
   ```
   > docker build -t tf_cuda_test .
   ```

2. **Run Docker Container:**
   ```
   > docker run --gpus all -e TF_CPP_MIN_LOG_LEVEL=2 -it --rm tf_cuda_test
   ```
   Options breakdown:
   - `--gpus all`: Allocates all available GPUs to the container.
   - `-e TF_CPP_MIN_LOG_LEVEL=2`: Sets TensorFlow logging level to minimize informational messages.
   - `-it`: Enables an interactive terminal session.
   - `--rm`: Removes the container after it exits.

## Container Details

- OS: Ubuntu 22.04.2 LTS
- CUDA Version: 11.8.r111.8/compiler 31833905_0
- Python Version: 3.11.0rc1

## Security Considerations

- Use this Docker container in a secure environment to prevent potential vulnerabilities from being actively exploited.
