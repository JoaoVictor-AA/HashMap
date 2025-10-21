from app.utils import hash_function
from app.EstruturasDePesquisa.listaEncadeada import ListaEncadeada

class HashMap:
    def __init__(self):
        self.list = [None, None, None, None, None, None, None, None, None, None]

    def add(self, value):
        index = hash_function(value)
        if self.list[index] is None:
            self.list[index] = ListaEncadeada()
        self.list[index].add(value)

    def remove(self, value):
        index = hash_function(value)
        if self.list[index] is None:
            return "Not found"
        self.list[index].delete(value)

    def search(self, value):
        index = hash_function(value)
        if self.list[index] is None:
            return "Not found"
        return self.list[index].search(value)


hashmap = HashMap()
hashmap.add("João")
hashmap.add("José")
hashmap.add("Pedro")
hashmap.add("Lucas")

print(hashmap.search("Lucas").value)

