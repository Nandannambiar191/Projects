class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_after_position(self, data, position):
        new_node = Node(data)

        current = self.head

        
        for i in range(position - 1):
            current = current.next

        new_node.next = current.next

        
        new_node.prev = current

       
        if current.next is not None:
            current.next.prev = new_node

        
        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next



dll = DoublyLL()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

dll.head = node1

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2


dll.insert_after_position(25, 2)


dll.display()