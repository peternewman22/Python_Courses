"""
What is a socket?
End point that receives data: sits at IP in a port
Use a header to tell the client how long the data will be
"""

import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 ??
#bind the socket
s.bind((socket.gethostname(), 1234))
#prepare for connection attempts
s.listen(5)

while True:
    #socket information will receive info
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    # need a fixed length header aligned left
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    #send info to the client socket in utf-8
    clientsocket.send(bytes(msg,"utf-8"))
