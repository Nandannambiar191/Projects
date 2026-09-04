class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        previous = None
        current = self.head

        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def display(self):
        current = self.head

        while current != None:
            print(current.data, end=" ")
            current = current.next



ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)


print("Before reversing:")
ll.display()


ll.reverse()


print("\nAfter reversing:")
ll.display()