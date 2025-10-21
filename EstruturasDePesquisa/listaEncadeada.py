class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.head:
            self.last.next = new_node
            self.last = new_node
        else:
            self.head = self.last = new_node
        self.size += 1

    def delete(self, value):
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
            else:
                searcher = self.head
                found = False
                while searcher.next is not None:
                    if searcher.next.value == value:
                        found = True
                        break
                    searcher = searcher.next

                if not found:
                    return f"Valor {value} não encontrado."
                try:
                    searcher.next = searcher.next.next
                except TypeError:
                    searcher.next = None
            self.size -= 1
            return "Exclusão bem-sucedida."
        raise ValueError

    def search(self, value):
        if not self.head:
            return -1
        if self.head.value == value:
            return self.head
        searcher = self.head
        while searcher.next is not None:
            if searcher.next.value == value:
                searcher = searcher.next
                break
            searcher = searcher.next
        if searcher.value == value:
            return searcher
        raise Exception("Not found")

    def print(self):
        searcher = self.head
        while searcher is not None:
            print(searcher.value)
            searcher = searcher.next


lista = ListaEncadeada()
lista.add(1)
lista.add(2)
lista.add(4)
lista.add(5)
lista.delete(5)
valor = lista.search(1)
print(valor.value)

