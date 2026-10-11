from socket import *
import time
from struct import *
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('0.0.0.0',serverPort))
serverSocket.listen(1)
print('server ready')

def recvall(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError('socket closed with %d bytes left'' in this block'.format(length))
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)

while True:
    connectionSocket, address = serverSocket.accept()

    message = recvall(connectionSocket,8)
    
    HeureClient = unpack('!d', message) 
    HeureAct = time.time()
    HeureDiff = HeureAct - HeureClient[0]
    resultat = pack('!d', HeureDiff)
    a = time.time()
    message = pack('!d', a)

    connectionSocket.send(resultat)
    connectionSocket.send(message)
    connectionSocket.close()
