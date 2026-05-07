import random
import ipaddress
import time
from collections import deque

class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.__radice = None

    def insert(self, valore):
        if self.__radice is None:
            self.__radice = NodoBST(valore)
        else:
            self.__insertRicorsivo(self.__radice, valore)

    def __insertRicorsivo(self, nodo, valore):

        if valore < nodo.valore:
            if nodo.left is None:
                nodo.left = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.left, valore)
        else:
            if nodo.right is None:
                nodo.right = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.right, valore)

    def search(self, valore):
        return self.__searchRicorsivo(self.__radice, valore)

    def __searchRicorsivo(self, nodo, valore):

        if nodo is None:
            return False
        if nodo.valore == valore:
            return True
        if valore < nodo.valore:
            return self.__searchRicorsivo(nodo.left, valore)
        else:
            return self.__searchRicorsivo(nodo.right, valore)

#conversione Ip

def ipToInt(ip):
    return int(ipaddress.ip_address(ip))


def intToIp(n):
    return str(ipaddress.ip_address(n))


blacklist_bst = BST()

# 1000 IP casuali
blacklist_ip = [
    '.'.join(str(random.randint(0, 255)) for _ in range(4))
    for _ in range(1000)
]

# conversione in interi
blacklist_int = [ipToInt(ip) for ip in blacklist_ip]

# inserimento nel BST
for ip in blacklist_int:
    blacklist_bst.insert(ip)

pacchetti = []

# 10 IP presi dalla blacklist
ip_bloccati = random.sample(blacklist_ip, 10)

ip_nuovi = []

while len(ip_nuovi) < 10:

    nuovo_ip = '.'.join(
        str(random.randint(0, 255)) for _ in range(4)
    )

    if nuovo_ip not in blacklist_ip:
        ip_nuovi.append(nuovo_ip)

tutti_ip = ip_bloccati + ip_nuovi

# mescoliamo
random.shuffle(tutti_ip)

queue = deque()

for ip in tutti_ip:

    pacchetto = {
        "ip_sorgente": ip,
        "ip_destinazione": "10.0.0.1",
        "porta_sorgente": random.randint(1024, 65535),
        "porta_destinazione": 80,
        "protocollo": "TCP",
        "dimensione": random.randint(64, 1500)
    }

    queue.append(pacchetto)

bloccati = 0
permessi = 0

print("\n==== CONTROLLO PACCHETTI ====\n")

while queue:

    pacchetto = queue.popleft()
    ip = pacchetto["ip_sorgente"]
    ip_intero = ipToInt(ip)
    trovato = blacklist_bst.search(ip_intero)

    if trovato:
        print(f"{ip} --> BLOCCATO")
        bloccati += 1
    else:
        print(f"{ip} --> PERMESSO")
        permessi += 1

print("\n==== RIEPILOGO ====")
print("Pacchetti bloccati:", bloccati)
print("Pacchetti permessi:", permessi)

test_ip = random.choice(blacklist_ip)
test_ip_int = ipToInt(test_ip)

inizio = time.perf_counter()

for _ in range(10000):
    blacklist_bst.search(test_ip_int)

tempo_bst = time.perf_counter() - inizio

inizio = time.perf_counter()

for _ in range(10000):
    test_ip_int in blacklist_int

tempo_lista = time.perf_counter() - inizio

print("\n==== CONFRONTO ====")

print(f"Tempo BST:   {tempo_bst:.6f} secondi")
print(f"Tempo Lista: {tempo_lista:.6f} secondi")

if tempo_bst < tempo_lista:
    print(f"Il BST è circa {tempo_lista / tempo_bst:.2f} volte più veloce")
else:
    print(f"La lista è circa {tempo_bst / tempo_lista:.2f} volte più veloce\n")