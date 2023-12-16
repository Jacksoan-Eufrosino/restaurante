from main import *
from estrutura_triNode import *
from repositorioRestaurante import *

class NumberInvertedIndex:
    def __init__(self):
        self.indice = dict()

    def adicionar(self, chave, carga):
        if chave not in self.indice:
            self.indice[chave] = []
        self.indice[chave].append(carga)

    def menor_igual(self, max):
        from_index = [value for chave,
                      value in self.indice.items() if chave <= max]
        result = [item for sublist in from_index for item in sublist]
        return result

    def maior_igual(self, min):
        from_index = [value for chave,
                      value in self.indice.items() if chave >= min]
        result = [item for sublist in from_index for item in sublist]
        return result

    def get_item(self, chave):
        return self.indice[chave]


class PartialStringInvertedIndex:
    def __init__(self):
        self.indice = PrefixTrie()

    def adicionar(self, word, carga):
        word = word.strip().lower()
        self.indice.inserir(word, carga)

    def buscar(self, word):
        word = word.strip().lower()
        return self.indice.buscar(word)

valor = NumberInvertedIndex()
rating = NumberInvertedIndex()
distancia = NumberInvertedIndex()
restaurante = PartialStringInvertedIndex()
cuisine_indice = PartialStringInvertedIndex()

for restaurant in repositorio_restaurante.find_all():
    valor.adicionar(int(restaurant.price), restaurant)
    rating.adicionar(int(restaurant.customer_rating), restaurant)
    distancia.adicionar(int(restaurant.distance), restaurant)
    restaurante.adicionar(restaurant.name, restaurant)

for cuisine in repositorio_cozinha.find_all():
    cuisine_indice.adicionar(cuisine.name, cuisine)
