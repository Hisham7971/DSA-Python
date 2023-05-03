class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Address of the next node.

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next

l = SingleLinkedList()
n1 = Node(10)
l.head = n1
n2 = Node(20)
l.head.next = n2
n3 = Node(30)
n2.next = n3
print(l.display())



