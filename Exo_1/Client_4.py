from socket import *
import time
message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
serverName = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET, SOCK_DGRAM)
moyenneRTT = 0.0
nbRequete = 0
mess = "Client 4 : message "
#message = input('lower sentence :').encode('utf-8')
for i in range(10): 
    debut = time.time()
    clientSocket.sendto(mess.encode('utf-8')+message[i].encode('utf-8'), (serverName,serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    fin =  time.time()
    print(modifiedMessage.decode('utf-8'))
    moyenneRTT += fin-debut
    nbRequete += 1
moyenneRTT = moyenneRTT / nbRequete
print(f"Le client 4 a envoyer {nbRequete} requêtes et cela a pris en moyenne {round(moyenneRTT*1000,2)} ms")
    
clientSocket.close()