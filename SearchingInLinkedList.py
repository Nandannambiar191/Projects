class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target):
        current = self.head

        while current != None:
            if current.data == target:
                print("Found")
                return

            current = current.next

        print("Not Found")



ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)


ll.search(30)