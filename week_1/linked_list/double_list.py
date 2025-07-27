class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        
        self.length += 1
    
    def __str__(self):
        if self.head is None:
            return "Doubly Linked List is empty"
        else:
            nodes = []
            current_node = self.head
            while current_node is not None:
                nodes.append(str(current_node.value))
                current_node = current_node.next
            return " <-> ".join(nodes) + " <-> None"

    def __len__(self):
        return self.length
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next


dll = DoublyLinkedList()
dll.append(90)
dll.append(80)
dll.append(70)
print("Head next value:", dll.head.next.value)
print("Doubly Linked List:", dll)

for value in dll:
    print(value)

print("Length:", len(dll))
