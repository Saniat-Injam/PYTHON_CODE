# Inserting / Adding elements at the end
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end = " ")
                n = n.ref
            print()

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

LL1 = LinkedList()
LL1.printLL()

LL1.add_begin(10)
LL1.printLL()

LL1.add_begin(20)
LL1.printLL()

LL1.add_begin(30)
LL1.printLL()