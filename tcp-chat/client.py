"""
client.py
> Starts a client process for the tcp-chat
> After starting, enter a unique identifier name
"""

import socket
import threading

nickname = input('Choose a nickname: ')

# TODO: implement command line arguments for host-ip and host-port
#  (https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'handshake':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
