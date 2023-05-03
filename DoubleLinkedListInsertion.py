class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("empty double linked list")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def insert_beginning(self, data):
        n = Node(data)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n

    def insert_end(self, data):
        n = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        n.prev = temp

    def inset_position(self, pos, data):
        n = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        n.prev = temp
        n.next = temp.next
        temp.next.prev = n
        temp.next = n


l = DoubleLinkedList()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n2.prev = n1
n1.next = n2
n3 = Node(30)
n3.prev = n2
n2.next = n3
n4 = Node(40)
n4.prev = n3
n3.next = n4
n5 = Node(50)
n5.prev = n4
n4.next = n5
# l.insert_beginning(5)
# l.insert_end(55)
l.inset_position(4, 35)
print(l.display())