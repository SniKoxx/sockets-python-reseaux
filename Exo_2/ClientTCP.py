from socket import *
import time
from struct import *

#Possibilité que lorsque le client fait le recv, il ne recoit pas tout les octets.
def recvall(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError('socket closed with %d bytes left'' in this block'.format(length))
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)


serverName = gethostname() #Mettre l'adresse IP du serveur
serverPort = 1234
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Envoie l'horloge actuelle du client au serveur 
clientSocket.send(pack('!d',time.time()))  #!d et non !f parce que time.time() renvoie un nombre trop grand pour !f et il faut inclure les chiffre après la virgule.

ResultatMessage = recvall(clientSocket,16)

#Recupération des valeurs
DecalageClientServ = unpack('!d',ResultatMessage[0:8])[0] 
DecalageServClient = (time.time() - (unpack('!d', ResultatMessage[8:16])[0])) * 1000
Resultat = (DecalageClientServ + DecalageServClient)/2
print(f"La différence d’horloge entre le serveur et le client et l’afficher à l’écran est de {Resultat} ms")
clientSocket.close()