import random
import time


class Nodo:
    def __init__(self,valore):
        self.valore = valore
        self.next = None


class LinkedList:
    def __init__(self):
        self.__testa = None
        self.__size  = 0

    def insertFirst(self, valore):
        nuovo        = Nodo(valore)
        nuovo.next   = self.__testa
        self.__testa = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = Nodo(valore)
        if self.__testa is None:
            self.__testa = nuovo
        else:
            corrente = self.__testa
            while corrente.next is not None:
                corrente = corrente.next
            corrente.next = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente.next is not None:
            if corrente.next.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore       = self.__testa.valore
        self.__testa = self.__testa.next
        self.__size -= 1
        return valore
    
    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        if self.__testa.next is None:
            valore       = self.__testa.valore
            self.__testa = None
            self.__size -= 1
            return valore
        corrente = self.__testa
        while corrente.next.next is not None:
            corrente = corrente.next
        valore        = corrente.next.valore
        corrente.next = None
        self.__size -= 1
        return valore
    
    def find(self, valore):
        corrente = self.__testa

        while corrente is not None:
            if corrente.valore == valore:
                return True
            corrente = corrente.next

        return False

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        elementi = []
        corrente = self.__testa
        while corrente is not None:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
        return "LinkedList([" + " → ".join(elementi) + "])"

class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left   = None   # figlio sinistro — valori minori
        self.right  = None   # figlio destro — valori maggiori

class BST:
    def __init__(self):
        self.__radice = None

    def insert(self, valore):
        if self.__radice is None:
            self.__radice = NodoBST(valore)
        else:
            # partiamo dalla radice e scendiamo nell'albero
            # la funzione chiamerà se stessa finché non trova un posto libero
            self.__insertRicorsivo(self.__radice, valore)


    def __insertRicorsivo(self, nodo, valore):
        if valore < nodo.valore:
            # il valore è minore — dobbiamo andare a sinistra
            if nodo.left is None:
                # CASO BASE: posto libero a sinistra — inseriamo qui
                nodo.left = NodoBST(valore)
            else:
                # CASO RICORSIVO: c'è già un nodo a sinistra
                # richiamiamo la stessa funzione sul figlio sinistro
                # il problema si riduce: scendiamo di un livello
                self.__insertRicorsivo(nodo.left, valore)
        else:
            # il valore è maggiore — dobbiamo andare a destra
            if nodo.right is None:
                # CASO BASE: posto libero a destra — inseriamo qui
                nodo.right = NodoBST(valore)
            else:
                # CASO RICORSIVO: c'è già un nodo a destra
                # richiamiamo la stessa funzione sul figlio destro
                self.__insertRicorsivo(nodo.right, valore)

    def search(self, valore):
        # partiamo dalla radice
        return self.__searchRicorsivo(self.__radice, valore)

    def __searchRicorsivo(self, nodo, valore):
        # CASO BASE 1: nodo inesistente — il valore non è nell'albero
        if nodo is None:
            return False

        # CASO BASE 2: trovato — il valore corrisponde
        if nodo.valore == valore:
            return True

        if valore < nodo.valore:
            # il valore è minore — non può essere a destra
            # CASO RICORSIVO: cerchiamo solo nel sottoalbero sinistro
            return self.__searchRicorsivo(nodo.left, valore)
        else:
            # il valore è maggiore — non può essere a sinistra
            # CASO RICORSIVO: cerchiamo solo nel sottoalbero destro
            return self.__searchRicorsivo(nodo.right, valore)

    def inOrder(self):
        # inOrder restituisce i valori in ordine crescente
        # perché visita prima sinistra, poi radice, poi destra
        elementi = []
        self.__inOrderRicorsivo(self.__radice, elementi)
        return elementi

    def __inOrderRicorsivo(self, nodo, elementi):
        # CASO BASE: nodo inesistente — non c'è nulla da visitare
        if nodo is None:
            return

        # CASO RICORSIVO:
        # 1. visita prima tutto il sottoalbero sinistro (valori minori)
        self.__inOrderRicorsivo(nodo.left, elementi)

        # 2. poi aggiungi il valore del nodo corrente
        elementi.append(nodo.valore)

        # 3. poi visita tutto il sottoalbero destro (valori maggiori)
        self.__inOrderRicorsivo(nodo.right, elementi)

    def isEmpty(self):
        return self.__radice is None

    def __repr__(self):
        return f"BST(inOrder={self.inOrder()})"


albero = BST()
lista = LinkedList()

lista_search=[]

for _ in range(1000):
    lista_search.append(random.randint(1, 10000))

for n in lista_search:
    lista.insertLast(n)
    albero.insert(n)

valuesearch=lista_search[500]

print("\n=========== Search Lista ==============")
inizio = time.perf_counter()
trovato = lista.find(valuesearch) 
fine = time.perf_counter()
print("Trovato:", trovato)
tempo_lista = fine - inizio
print("Tempo impiegato:", tempo_lista, "secondi\n")

print("=========== Search Albero ==============")
inizio_albero = time.perf_counter()
trovato_albero = albero.search(valuesearch)
fine_albero = time.perf_counter()
print("Trovato:", trovato_albero)
tempo_albero = fine_albero - inizio_albero
print("Tempo impiegato:", tempo_albero, "secondi")


print("\n=========== Confronto ================")
volte = tempo_lista/tempo_albero
print(f"L'albero è {volte:.2f} volte più veloce della lista\n")
