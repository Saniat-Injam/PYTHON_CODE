# Inserting or adding  elements after the given node

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        n = self.head
        if n is None:
            print("Linked list is empty")
        else:
            while n is not None:
                print(n.data)
                n = n.ref

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

LL1 = LinkedList()









LL1 = LinkedList()
LL1.printLL()






