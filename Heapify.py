class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.mark = False


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key):
        new_node = Node(key)

        if self.min_node is None:
            self.min_node = new_node
        else:
            new_node.left = self.min_node
            new_node.right = self.min_node.right
            self.min_node.right.left = new_node
            self.min_node.right = new_node

            if key < self.min_node.key:
                self.min_node = new_node

        self.total_nodes += 1
        return new_node

    def find_min(self):
        if self.min_node is None:
            return None
        return self.min_node.key

    def display(self):
        if self.min_node is None:
            print("Heap is empty")
            return

        print("Minimum:", self.min_node.key)
        print("Root nodes:", end=" ")

        current = self.min_node
        while True:
            print(current.key, end=" ")
            current = current.right
            if current == self.min_node:
                break

        print()
        print("Total nodes:", self.total_nodes)


heap = FibonacciHeap()

heap.insert(10)
heap.insert(3)
heap.insert(15)
heap.insert(7)
heap.insert(1)

heap.display()

print("Minimum element:", heap.find_min())