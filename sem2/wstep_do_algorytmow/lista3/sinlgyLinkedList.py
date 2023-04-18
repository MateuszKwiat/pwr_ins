class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.length == 0
    
    def count(self):
        return self.length
    
    def insertHead(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node       
        self.length += 1

    def insertTail(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def removeHead(self):
        if self.length == 0:
            raise ValueError("Empty list")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node 