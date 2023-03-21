#!/usr/bin/env python
import psutil
import time
import urllib.request
import os
import random

cpu_threshold = 10  # in percent
network_threshold = 10  # in percent
memory_threshold = 10  # in percent

# function to generate random data
def generate_random_data():
    data = []
    for i in range(2000000):
        data.append(random.randint(0, 100))
    return data

while True:
    # Check CPU utilization
    cpu_utilization = psutil.cpu_percent(interval=1, percpu=False)
    if cpu_utilization < cpu_threshold:
        # Generate random data to keep the CPU busy
        data = generate_random_data()
        print("CPU utilization ({0}%) is below threshold ({1}%)".format(cpu_utilization, cpu_threshold))

    # Check network utilization
    network_utilization = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    time.sleep(1)
    new_network_utilization = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    network_usage = new_network_utilization - network_utilization
    network_utilization_percentage = (network_usage / 1000000) * 100
    if network_utilization_percentage < network_threshold:
        # Download a large file to keep the network busy
        url = 'http://speedtest.tele2.net/1GB.zip'
        urllib.request.urlretrieve(url, os.devnull)
        print("Network utilization ({0}%) is below threshold ({1}%)".format(network_utilization_percentage, network_threshold))

    # Check memory utilization
    memory_utilization = psutil.virtual_memory().percent
    if memory_utilization < memory_threshold:
        # Allocate a large block of memory to keep the memory busy
        memory_block = [0] * (1000000)
        print("Memory utilization ({0}%) is below threshold ({1}%)".format(memory_utilization, memory_threshold))

    time.sleep(1)  # Wait for 1 second before running again
