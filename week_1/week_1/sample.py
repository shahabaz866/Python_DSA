# class Node:
#     def __init__(self,data):
#         self.value = data
#         self.next = None

    
# class Linked_list:
#     def __init__(self):
#         self.head = None

#     def append(self,value):
#         newNode = Node(value)
        
#         if self.head == None:
#             self.head = newNode 
#         else:
#             current_Node =  self.head

#             while current_Node.next is not None:

#                 current_Node = current_Node.next
#             current_Node.next = newNode



# ll = Linked_list()

# ll.append(10)
# ll.append(20)

# print(ll.head.next.value)

# class Node:
#     def __init__(self,data):
#         self.value = data
#         self.next = None

# class Linked_list:
#     def __init__(self):
#         self.head = None
#         self.length = 0
    
#     def append(self,value):
#         New_node = Node(value)
#         if self.head == None:
#             self.head = New_node
#         else:
#             Current_node = self.head

#             while Current_node.next is not None:
#                 Current_node = Current_node.next

#             Current_node.next = New_node
#         self.length += 1
#     def prepend(self,value):
#         New_node = Node(value) 
#         if self.head == None:
#             self.head = New_node
#         else:
#             New_node.next = self.head
#             self.head = New_node
#         self.length += 1
    
#     def __str__(self):
#         if self.head is None:
#             return "Linked List is empty"
#         else:
#             nodes=[]
#             current_Node = self.head
#             while current_Node is not None:
#                 nodes.append(str(current_Node.value))
#                 current_Node = current_Node.next
#             return ' -> '.join(nodes) + ' -> None'
#     def __len__(self):
#         return self.length
    


            

# ll = Linked_list()

# ll.append(10)
# ll.append(190)
# ll.prepend(100)


# print(ll.head.value)
# print("hee:",ll)



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#     def append(self,data):
#         new_node = Node(data)

#         if self.head == None:
#             self.head = new_node
#         else:
#             current_node = self.head

#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = new_node
#         self.length += 1
    
#     def prepend(self,data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
        
#     def __iter__(self):
#         current_node = self.head
#         while current_node is not None:
#             yield current_node.data
#             current_node=current_node.next


# ll = Linkedlist()

# ll.append(100)
# ll.prepend(101)
# for i in ll:
#     # print(ll.head.data)
#     print(i)




# my_list = [10, 20, 30, 40, 50]
# removed_element = my_list.pop()

# print(my_list,"one: " , removed_element)

# def fibinoccie(n):
#     if n <=  0:
#         return "inavalid value"
#     elif n==1 :
#         return 0
#     elif n==2 :
#         return 1

#     return fibinoccie(n-1) + fibinoccie(n-2)

# res = fibinoccie(6)
# print(res)
  

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)


# # n=5

# rest= fact(5)
# print(rest)



# def bie(arr,trg,left,right):
#     if left>right:
#         return -1
#     mid = (left+right) // 2
#     if arr[mid]==trg:
#         return mid
#     elif arr[mid] < trg:
#         return bie(arr,trg,mid+1,right)
#     else:
#         return bie(arr,trg,left,mid-1)
    
# arr=[1,2,3,4,5]
# trg= 2
# left=0
# right=len(arr)-1

# res= bie(arr,trg,left,right)
# print(res)
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Liked_list:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head

#             while current_node.next is not None:
#                 current_node = current_node.next
            
#             current_node.next = new_node
        
#         self.length += 1
#     def prepend(self,data):
#         New_node = Node(data) 
#         if self.head is None:
#             self.head = New_node
#         else:
#             New_node.next = self.head
#             self.head = New_node
#         self.length += 1

    
#     def __getitem__(self,index):
#         if index < 0 or index >= self.length:
#             raise IndexError("Index out of range")
#         else:
#             current_node = self.head
#             for _ in range(index):
#                 current_node = current_node.next
#             return current_node.data
    
#     def __setitem__(self,index,data):
#         if index < 0 or index >= self.length:
#             raise IndexError("Index out of range")
#         else:
#             current_node = self.head

#             for _ in range(index):
#                 current_node = current_node.next
#             current_node.data = data




# ll = Liked_list()

# ll.append(100)
# ll.prepend(101)

# print(ll.head.next.data)
# ll[1]=900
# print(ll[1])


# class Node :
#     def __init__(self,data):
#         self.data =data
#         self.next = None

# class Linked_list:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#     def append(self,data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = new_node
#         self.length +=1

#     def __setitem__(self,index,data):
#         if index < 0 or index >=self.length:
#             raise IndexError("error out of range")
        
#         else:
#             current_node = self.head

#             for _ in range(index):
#                 current_node = current_node.next
#             current_node.data = data
#     def __getitem__(self,index):
#         if index < 0 or index >= self.length:
#             raise IndexError("error out of reach")
#         else:
#             current_node = self.head
#             for _ in range(index):
#                 current_node = current_node.next
            
#             return current_node.data
#     def __str__(self):
#         if self.head == None:
#             return "no value "
#         else:
#             nodes =[]
#             current_node = self.head
#             while current_node is not None:
#                 nodes.append(str(current_node.data))
#                 current_node = current_node.next
            
#             return ' -> '.join(nodes) + ' -> None'

#     def __len__(self):

#         return self.length
#     def __iter__(self):

#         current_node = self.head
#         while current_node  is not None:
#             yield current_node.data
#             current_node =current_node.next
   
        
#     def pop(self,index=0):
#         if index >= self.length:
#             raise IndexError("index out of reach")
#         elif index == 0:
#             temp = self.head
#             self.head = self.head.next
#             self.length -= 1
#             return temp.data
#         else:
#             current_node =self.head
#             for _ in range(index-1):
#                 current_node = current_node.next
#             temp = current_node.next.data
#             current_node.next = current_node.next

#             self.length -=1
#             return temp

#     def __delitem__(self, index):
#         self.pop(index)


# ll = Linked_list()

# ll.append(10)
# ll.append(12)
# ll.append(13)
# for i in range(10):
#     ll.append(i)
# ll[5]= 92
# ll[1] = 99
# ll[2] = 10
# # print(ll.head.next.next.data)
# # del ll[]
# print(ll)
# dell=ll.pop(5)
# print("del:",dell)
# print(len(ll))
# print(ll[1])
# print(ll)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None




# class Linkedlist:
#     def __init__(self):
#         self.head= None
#         self.legnth  = 0

#     def append(self,data):
#         new_node = Node(data)

#         if self.head == None:
#             self.head = new_node
#         else:
#             current_node = self.head

#             while current_node.next is not None:
#                 current_node = current_node.next 
#             current_node.next = new_node
#         self.legnth += 1
    

# ll = Linkedlist()

# ll.append(100)

# print(ll.head.data)

            

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.length = 0

#     def append(self,data):
#         new_node = Node(data)

#         if self.head == None:
#             self.head = new_node

#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = new_node
#         self.length +=1

#     def preppend(self,data):

#         new_node =  Node(data)
#         if self.head == None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length +=1

#     def search(self,data):
#         current_node = self.head
#         while current_node:
#             if current_node.data == data:
#                 return self.length
#             current_node = current_node.next
#         return False
#     def delete(self,index):
#         if self.length <= index or index < 0:
#             return "range out "
        
#         else:
#             current_node = self.head

#             cnt=0
#             data=None
#             prev = None
#             while True:
#                 if index == cnt :
#                     if self.head == current_node:
#                         data = current_node.data
#                         self.head = current_node.next
#                         self.length -= 1
#                         return data

#                     else:
#                         data = current_node.data
#                         prev.next = current_node.next
#                         self.length -= 1
#                         return data


#                 else:
#                     prev = current_node
#                     current_node = current_node.next
#                     cnt+=1
            
#     def lengths(self):
#         return self.length

    




# ll = Linkedlist()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.preppend(40)
# delete=ll.delete(2)
# print("del data",delete)
# print("length:",ll.lengths())

# print(ll.head.data)
# print(ll.search(20))

    


        

# lst = ["hina","annaan"]

# # lst_r = lst.split()
# join=' '.join(lst)
# print(type(join))
# print(join)
