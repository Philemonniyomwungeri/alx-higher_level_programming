#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        """Defines a node of a singly linked list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Next node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Next node setter"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Defines a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        tmp = self.__head
        add_start = False

        if not self.__head:
            self.__head = new_node
            new_node.next_node = None
        else:
            if value < self.__head.data:
                add_start = True
            while tmp.next_node and value > tmp.next_node.data and not add_start:
                tmp = tmp.next_node
            if not add_start:
                new_node.next_node = tmp.next_node
                tmp.next_node = new_node
            else:
                new_node.next_node = tmp
                self.__head = new_node
            new_node.data = value

    def __str__(self):
        s = ""
        current = self.__head

        while current:
            s += str(current.data) + '\n'
            current = current.next_node
        return s[:-1]

# Test the SinglyLinkedList class with examples
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)