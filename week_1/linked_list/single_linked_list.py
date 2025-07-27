class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.length=0
    
    def append(self,value):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
        else:
            current_node = self.head

            while current_node.next is not None : 
                current_node = current_node.next

            current_node.next = newNode
        self.length +=1

    def prepend(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1
    def delete(self,index):
        if self.length <= index or index < 0:
            return "index error"
        else:
            current_node = self.head
            cnt=0
            prev=None
            value = None
            while True:
                if cnt == index:
                    if self.head == current_node:
                        value = current_node.value
                        self.head =current_node.next
                        self.length -=1
                        return value
                        
                    else:
                        value = current_node.value
                        prev.next = current_node.next
                        self.length -= 1
                        return value

                else:
                    prev = current_node
                    current_node= current_node.next
                    cnt+=1
    def reverse(self):
        prev = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev


    
    def __str__(self):
        if self.head is None:
            return "Linked List is null"
        else:
            nodes = []
            current_node = self.head
            while current_node is not None:
                nodes.append(str(current_node.value))
                current_node = current_node.next
            return '->'.join(nodes) +'-> None'
    

    def __len__(self):
        return self.length
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node=current_node.next


ll = Linked_list()
ll.append(90)
ll.append(80)
ll.append(70)
print("ooi",ll)
# delete =ll.delete(1)
# print(delete)
ll.reverse()
# hh =ll
# for i in range(10):
#         ll.append(i)
print("oooioi",ll)

# for value in ll:  
#     print(value)

print("length:",ll.length)