class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Circularlinkedlist:
    def __init__(self):
        self.head = None 
        self.length = 0
    
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head  = new_node
            self.head.next = self.head

        else:
            crnt_node = self.head
            while crnt_node.next != self.head :
                crnt_node = crnt_node.next
            crnt_node.next = new_node
            new_node.next = self.head
    
    def display(self):
        crnt_node = self.head
        if self.head:
            while True:
                print(crnt_node.data,end=" -> ")
                crnt_node = crnt_node.next 
                if crnt_node == self.head:
                    break
            print("(Back to Head)")
    

cll = Circularlinkedlist()
cll.append(10)
cll.append(20)
cll.append(30)

cll.display()