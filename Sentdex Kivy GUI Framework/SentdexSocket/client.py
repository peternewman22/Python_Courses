"""
This one wants to connect
If you have a stream of data, you have to decide how big a chunk of data
at a time (in bytes)
"""

import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 ??
# pass it a tuple with the hostname/ip and the port
s.connect((socket.gethostname(), 1234))

full_msg = ''
new_msg = True
while True:
#buffer length = 1024
    msg = s.recv(16)
    if new_msg:
        print("new msg len:",msg[:HEADERSIZE])
        msglen = int(msg[:HEADERSIZE])
        new_msg = False
    print(f"full message length: {msglen}")
    full_msg += msg.decode('utf-8')
    print(len(full_msg))
    if len(full_msg) - HEADERSIZE == msglen:
        print("full msg recvd")
        print(full_msg[HEADERSIZE:])
        new_msg = True
        full_msg = '' #emptying it out
print(full_msg)
