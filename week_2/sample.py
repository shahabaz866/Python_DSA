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


# index=0-7

# def Bubble_sort(arr):
#     n= len(arr) =8

#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] >arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1] ,arr[j]

#     return arr

# arr =[1,231,32,45,25,-1,53,5]

# result = Bubble_sort(arr)

# print(result)


# strg = "ones"
# my_string = "hello"
# print(''.join(reversed(my_string)))  

fruits = {'apple': 100, 'banana': 50, 'orange': 80}
