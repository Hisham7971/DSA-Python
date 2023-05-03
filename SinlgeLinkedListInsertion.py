class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_begnining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
        
    def insert_ending(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        
    def insert_position(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np
        
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
                
n = SingleLinkedList()
n1 = Node(10)
n.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
n4.next = n5
n6 = Node(60)
n5.next = n6
n7 = Node(70)
n6.next = n7
n8 = Node(80)
n7.next=n8
n9 = Node(90)
n8.next = n9
# n.insert_begnining(5)
# n.insert_ending(95)
n.insert_position(6, 55)
print(n.display())