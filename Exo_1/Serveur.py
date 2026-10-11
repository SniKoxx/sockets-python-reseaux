from socket import * 
import random
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('localhost',serverPort))
print('server ready')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('utf-8').upper()
    serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
