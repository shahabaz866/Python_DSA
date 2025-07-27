# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def isempty(self):
#         return len(self.stack) == 0
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#             if self.isempty():
#                 return "its empty"
#             else:
#                 self.stack.pop()
#     def peek(self):
#         if self.isempty():
#             return "is empty"
#         else:
#             return self.stack[-1]
    
#     def display(self):
#         if self.isempty():
#             print("Stack is empty.")
#         else:
#             print(self.stack)




# stck = Stack()
# stck.push(10)
# for i in range(10):
#     stck.push(i)

# print(stck.peek())
# stck.pop()


# stck.display()

# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def isempty(self):
#         return len(self.stack) == 0
#     def push(self,data):
#         self.stack.append(data)

#     def pop(self):
#         if self.isempty():
#             return "is empty"
#         else:
#             self.stack.pop()
#     def peek(self):
#         if self.isempty():
#             return "is empty"
#         else:
#             self.stack[-1]

#     def display(self):
#          if self.isempty():
#              print("Stack is empty.")
#          else:
#              print(self.stack)


# sk = Stack()
# one=[1,243,34,35,33,2,5,5,6]
# for i in one:
#     sk.push(i)

# sk.display()
# print(sk.peek())


# def bubblesort():

#     pass


# ls= [1,21,1,4,15,6,8]

# for i in range(len(ls)):
#     for j in range(0,len(ls)-1-i):

#          if ls[j] > ls[j + 1]:
            
#             ls[j], ls[j + 1] = ls[j + 1], ls[j]

# print(ls)

# ls = [1, 21, 1, 4, 15, 6, 8]
# n= len(ls)
# for i in range(n):
#     for j in range(n-1-i):
#         if ls[j] > ls[j+1]:
#             ls[j],ls[j+1] = ls[j+1],ls[j]

    
# print(ls)

# def bubble_sort(ls,n):
#     for i in range(n):
#         for j in range(n-i-1):
#             if ls[j]>ls[j+1]:
#                 ls[j],ls[j+1]=ls[j+1],ls[j]
#     return ls
# ls = [1, 21, 1, 4, 15, 6, 8]
# n= len(ls)

# print(bubble_sort(ls,n))


