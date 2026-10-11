HUANG Loïc 21203938

Le TME est composé de 3 repertoire :
- Exo_1 : 
    - Client_1.py
    - Client_2.py
    - Client_3.py
    - Client_4.py
    - Client_Exo1_Q4.py
    - Client.py
    - Serveur_proba.py
    - Serveur.py
- Exo_2 :
    - ClientTCP.py
    - ServeurTCP.py
- Exo_3 :
    - Aurevoir.txt
    - ClientWeb.py
    - MotDePasse.txt
    - Salut.txt
    - ServeurWeb.py
    - Test.txt

# Exo 1:
Implémentation du mécanisme de PING entre deux machines connectées à internet et calcule le temps en moyenne que prend le ping entre le client et le serveur
- `Client.py` : On envoie plusieurs requêtes au serveur et il regarde le temps écoulé entre l'envoie et la reception de chaque requête. A la fin calcule la moyenne des RTT puis il l'affiche.

- `Serveur.py` : Code du serveur avec le protocole UDP. Le serveur attends la requête du client et envoie une réponse au client.

Les fichiers `Client_1.py`, `Client_2.py`, `Client_3.py` et `Client_4.py` sont tous basés sur le fichier Client.py à quelque détails près.
Ils servent a tester le serveur (Serveur.py) où les clients effectuent des requêtes simultanées.

- `Client_Exo1_Q4.py` : Son code source est la même que celui de Client.py mais en rajoutant la fonctionnalité de renvoyer la requête au serveur, si celui-ci ne répond pas après x temps. A partir d'un certain temps, si le serveur ne répond toujours pas, on considère que le serveur est "off".

- `Serveur_proba.py` : Son code source est la même que celui de Serveur.py mais en rajoutant la possibilité que le serveur puisse oublié de répondre au client. La probabilité qu'il oublie est de 50%.

Réponse Exercice 1 Q4 : Avec une probabilité de 0.5 que le serveur oublie de répondre au client, le client est bloqué a l'infini parce qu'il attend la réponse du serveur.

# Exo 2 : 
Implémentation d'un serveur d’horloge simplifié qui répond aux requêtes formulées par les clients en revoyant l’heure courante sur la machine locale pour calculer la différence d’horloge entre le serveur et le client et l’afficher à l’écran.
- `ClientTCP.py` : On envoie au serveur l’heure courante de la machine client. En retour, le serveur lui envoie :(1) la différence que le serveur a eu avec l'horloge que le client a envoyer. (2) son heure courante. Le client calculera la différence avec l'heure courant que le serveur a envoyer. Il fera la moyenne des 2 différences obtenu puis l'affichera.

- `ServeurTCP.py` : Code du serveur avec le protocol TCP, reçoit de la part du client : son heure courant. Le serveur calcule la différence qu'il a entre lui et l'heure courant du client puis envoie au client 2 requête : (1) La différence entre lui et le client. (2) son heure courant.

# Exo 3 :
Implémentation d'un serveur Web simplifié qui répond aux requêtes formulées par les clients. Les requêtes formulées par le clients sont tous pour demander d'obtenir le contenu d'un fichier en particulier.

- `ClientWeb.py` : On envoie une requête qui suit le protocole HTTP pour demander a lire un fichier en particulier. Lorsque le client reçoit une réponse de la part du serveur, il affiche la reponse du serveur et de son contenu.

- `ServeurWeb.py` : Code du serveur Web avec le protocol TCP. Le serveur analyse le requête envoyer par le client. Il recupère le nom du fichier et cherche dans le système de fichiers si le fichier existe ou non. Si il existe, le serveur recupère le contenu du fichier et envoie d'une part une requête HTTP au client et d'une autre part une requête contenant le contenu du fichier. Sinon il envoie une erreur 404 avec le message 404 Not Found.

Pour pouvoir tester sur plusieurs PC différent, il faut pour chaque client, mettre l'adresse IP du serveur dans la variable ServerName.








