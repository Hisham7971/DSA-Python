class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
                
    def del_first(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        
    def del_last(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
    
    def del_pos(self, pos):
        prev = self.head
        temp = self.head.next
        for i in range(1, pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next

l = SingleLinkedList()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3

# l.del_first()
# l.del_last()
l.del_pos(2)
l.display()
        