"""
port-scanner.py
> Scans all the open port for a given target
> Implements multi-threading to make script run faster, can change 'num_threads' variable

Parv Patel
"""

import threading
from queue import Queue
import socket

# target ip (uses authorized ip!)
target = "10.0.0.1"

queue = Queue()
open_ports = []


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f'Port {port} is open!')
            open_ports.append(port)


# fill queue
port_list = range(1, 1025)
fill_queue(port_list)

# TODO: name 'num_threads' command line variable
num_threads = 100
thread_list = []

for t in range(num_threads):
    thread = threading.Thread(target=worker)
    thread.start()
    thread_list.append(thread)

for thread in thread_list:
    thread.join()

print(f'Open ports are: {open_ports}')
