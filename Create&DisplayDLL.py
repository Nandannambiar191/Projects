class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next



dll = DoublyLinkedList()


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

dll.head = node1

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2


dll.display()