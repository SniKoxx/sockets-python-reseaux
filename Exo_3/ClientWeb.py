from socket import *
import time
from struct import *
from zlib import *

# (Fonctions cours) Possibilité que lorsque le client fait le recv, il ne recoit pas tout les octets.
def recvall(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError(f'socket closed with {length} bytes left'' in this block')
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)

# (Fonctions cours) Permet d'envoyer un message avec sa taille a l'intérieur
def put_block(sock, message):
    block_length = len(message)
    sock.sendall(header_struct.pack(block_length))
    sock.sendall(message)

# (Fonctions cours) Permet de recupère le message 
def get_block(sock):
    data = recvall(sock, header_struct.size)
    (block_length,) = header_struct.unpack(data)
    return recvall(sock, block_length)


header_struct = Struct('!I')
serverName = gethostname() #Mettre l'adresse IP du serveur
serverPort = 1241
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

fichier = input(str('Quel fichier voulez vous recuperer ? : '))
host = gethostname()
message = 'GET ' + fichier + ' HTTP/1.1\nHost: ' + host + '\n Accept-Encoding: gzip\nContent-Type: text/xml\nContent-Length: 0'
message = compress(message.encode('utf-8'))
put_block(clientSocket, message)

decom1 = decompressobj()
resultatRequete = get_block(clientSocket)
resultatRequeteDecom = decom1.decompress(resultatRequete)
requete = resultatRequeteDecom.decode('utf-8')

decom2 = decompressobj()
resultatMessage = get_block(clientSocket)
resultatMessageDecom = decom2.decompress(resultatMessage)
message = resultatMessageDecom.decode('utf-8')

print(requete)
print(message)

clientSocket.close()