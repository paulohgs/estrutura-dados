from node import Node
from abc import ABC, abstractmethod

class List(ABC):
    @abstractmethod
    def append(self, element):
        """ Inserir elemento no fim da lista """
        pass
    
    def print_list(self):
        """ Imprimir no terminal os elementos da lista """
        pass

    def __setitem__(self, index, element):
        """ Insere um elemento no index passado """
        pass

    def __len__(self):
        pass

    def insert(self, index, element):
        """ Insere um elemento no index passado """
        pass

    def remove(self, element):
        """ Remover elemento da lista """
        pass

    def remove_at(self, index):
        """ Remove elemento no index passado """
        pass

class Linked_list(List):

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):
        if self.head is None:
            new_node = Node(element)
            self.head = new_node
        else:
            new_node = Node(element)
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
        self._size += 1
        return True    

    def __setitem__(self, index, element):
        if self.head is None:
            new_node = Node(element)
            self.head = new_node
            return new_node.data
        else:
            pointer = self.head
            for i in range(index):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError('List index out of range')
            if pointer:
                pointer.data = element
                return pointer.data
            else:
                raise IndexError('List index out of range')

    def remove(self, element):
        if self.head is None:
            raise ValueError('{} is not in list'.format(element))
        elif self.head.data == element:
            self.head = self.head.next
            self._size -= 1
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == element:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next

    def insert(self, index, element):
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head.next
            self.head = new_node
        else:
            pointer = self.head
            for i in range(index):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError('List index out of range')    
            new_node.next = pointer.next
            pointer = new_node
        return new_node.data


    def print_list(self):
        pointer = self.head
        teste = []
        print('Valores da lista:\n')
        while pointer:
            teste.append(pointer.data)
            print(pointer.data)
            pointer = pointer.next
        return teste

    def __len__(self):
        return self._size

    def __str__(self):
        return self.__repr__()
    
    

    