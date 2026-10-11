from socket import *
import time
message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
serverName = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET, SOCK_DGRAM)
moyenneRTT = 0.0
nbRequete = 0
delay = 0.1 # sec
#message = input('lower sentence :').encode('utf-8')
for i in range(10): 
    debut = time.time()
    while True:
        clientSocket.sendto(message[i].encode('utf-8'), (serverName,serverPort))
        clientSocket.settimeout(delay)
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        except timeout:
            delay *=2
            if delay > 2.0:
                raise RuntimeError('server seems down')
        else: 
            break
    fin =  time.time()
    print(modifiedMessage.decode('utf-8'))
    moyenneRTT += fin-debut
    nbRequete += 1
moyenneRTT = moyenneRTT / nbRequete
print(f"Le client a envoyer {nbRequete} requêtes et cela a pris en moyenne {round(moyenneRTT*1000,2)} ms")
    
clientSocket.close()