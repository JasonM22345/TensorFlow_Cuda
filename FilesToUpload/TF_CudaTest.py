"""
Title: Tensorflow + CUDA demonstration / testing
Jason Mensah-Homiah
https://github.com/JasonM22345
11/11/2023
"""

'''
This code tests if / demostrates how tensorflow works with CUDA
This code was written to be run within a docker container, which has all the prerequisites for
python 3 and CUDA installed already. You can find the dockerfile on my github.

NB: There is a one minute delay before all the vram is consumed. 
'''

import tensorflow as tf
import time
import numpy as np

# Function to print timestamp and notify the user
def print_timestamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'\n[{timestamp}] Delaying for 1 minute before starting TensorFlow GPU stress test.')

# Print timestamp and notify the user
print_timestamp()

# Delay for 1 minute
time.sleep(60)

# TensorFlow GPU information
try:
    gpu_devices = tf.config.experimental.list_physical_devices('GPU')
    if not gpu_devices:
        print('TensorFlow GPU not found.')
    else:
        print(f'TensorFlow GPUs found: {gpu_devices}')

        for device in gpu_devices:
            print(f'TensorFlow GPU device details: {device}')

            # Additional TensorFlow GPU information
            device_attributes = tf.config.experimental.get_device_attributes(device.name)
            print(f'TensorFlow GPU device attributes:')
            print(f'Name: {device_attributes["name"]}')
            print(f'Total Memory: {device_attributes["memory_limit"]}')
            print(f'Compute Capability: {device_attributes["compute_capability"]}')
            print(f'Multi-Processor Count: {device_attributes["multi_processor_count"]}')

except Exception as e:
    print(f'Error while retrieving TensorFlow GPU information: {e}')

# Print timestamp and notify the user before starting infinite computation
print_timestamp()

# Run something indefinitely on TensorFlow GPU
try:
    with tf.device('/GPU:0'):
        # Initialize a large shared array
        shared_array_size = (5000, 5000)
        shared_array = np.zeros(shared_array_size)

        while True:
            # Perform some TensorFlow computation on GPU
            result = tf.constant(42) * tf.constant(42)

            # Allocate and use shared VRAM
            shared_array += 1

            # Notify the user about VRAM usage
            print("Using all available VRAM for demonstration purposes. Press Ctrl+C to stop.")
            time.sleep(5)  # Adding a sleep to avoid excessive printing

except KeyboardInterrupt:
    print('\nTensorFlow GPU stress test completed.')

