class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("Empty Circular Linked List")
        else:
            temp = self.head
            print(temp.data, end=" ")
            while temp.next != self.head:
                temp = temp.next
                print(temp.data, end=" ")
            print(temp.next.data)

l = CircularLinkedList()
print(l.display())