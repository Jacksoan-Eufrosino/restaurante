from ler_csv import *

class No:
    def __init__(self, carga=None, proximo=None):
        self.carga = carga
        self.proximo = proximo

    def __repr__(self):
        return '%s -> %s' % (self.carga, self.proximo)

class ListaEncadeada:
    def __init__(self, head:'No'=None, tail:'No'=None):
        self.head = head
        self.tail = tail

    def inserir(self, carga):
        novo = No(carga)
        if self.head is None:
            self.head = self.tail = novo
        else:
            self.tail.proximo = novo
            self.tail = novo

    def buscar(self, chave:'str'):
        atual = self.head
        results = []
        while atual.proximo is not None:
            if chave.title() == atual.carga['name'][:len(chave)]:
                results.append(atual.carga)
            atual = atual.proximo
        return results

    def __str__(self):
        return str(self.head)

if __name__ == '__main__':
    lista = ListaEncadeada()
    dados = read_csv('restaurants.csv')
    for item in dados:
        lista.inserir(item)

    for i in lista.buscar('Del'):
        if int(i['distance']) < 2:
            print(i)