from repositorioRestaurante import RestaurantRepository

class TrieNode:
    def __init__(self):
        self.children = {}
        self.data = set()


class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def inserir(self, word, data):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.data.add(data)

    def buscar(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return node.data
            node = node.children[char]
        return node.data

# nome = PrefixTrie()
# rest = RestaurantRepository()
# find = rest.find_all()
# nome.inserir('word',rest)