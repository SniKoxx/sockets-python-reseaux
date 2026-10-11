from socket import *
import time
from struct import *
from threading import *
from zlib import *
from pathlib import Path

# (Fonction cours) Récupère [length] octets : Tant qu'il ne reçoit pas length octets il ne s'arrête pas.
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

def get_txt(NomDuFichier):
    f = open(NomDuFichier, 'rb')
    txt = f.read().decode('utf-8')
    f.close()
    return txt

# (Fonctions cours) 
def handle_client(clientSocket):
    while True:
        received = get_block(clientSocket)
        if not received:
            clientSocket.close()
        else:
            decom = decompressobj()
            received_decomp = decom.decompress(received)
            resultat = received_decomp.decode('utf-8')
            verif = resultat[0:3]
            if verif == 'GET':
                file = ''
                indice = 4
                while resultat[indice] != ' ':
                    file += str(resultat[indice])
                    indice += 1
                
                Trouve = False
                for fichier in d.rglob(file):
                    if fichier.is_file():
                        Trouve = True
                        print(f'Fichier {file} trouvé')
                        break
                
                if Trouve:
                    texte = get_txt(file)
                    requete = 'HTTP/1.0 200 OK\nServer: BaseHTTP/0.6 Python/3.4.3\nDate: ' 
                    requete += str(time.ctime(time.time())) + '\nContent-type: text\nContent-length: '
                    requete += str(len(texte)) + '\n'
                    requete = compress(requete.encode('utf-8'))
                    put_block(clientSocket,requete)
                    message = texte.encode('utf-8')
                else:
                    texte = '404 Not Found'
                    requete = 'HTTP/1.0 404 Not Found\nServer: BaseHTTP/0.6 Python/3.4.3\nDate: ' 
                    requete += str(time.ctime(time.time())) + '\nContent-length: '
                    requete += str(len(texte)) + '\n'
                    requete = compress(requete.encode('utf-8'))
                    put_block(clientSocket,requete)
                    message = texte.encode('utf-8')
                message = compress(message)
                put_block(clientSocket,message)
                

d = Path('.')
header_struct = Struct('!I')
serverPort = 1241
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('0.0.0.0',serverPort))
serverSocket.listen(1)
print('server ready')

while True:
    connectionSocket, address = serverSocket.accept()
    Thread(target=handle_client,args=(connectionSocket,)).start()

