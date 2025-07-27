class Stack:
    def __init__(self):
        self.stack=[]
    def isempty(self):
        return len(self.stack)==0
    def push(self,data):
        self.stack.append(data)
    def pop(self):
       if self.isempty():
           return "stack underflow"
       else:
           return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def display(self):
        if self.isempty():
            print("Stack is empty.")
        else:
            print(self.stack)
s=Stack()
s.push(3)
s.push(6)
s.push(7)
s.push(10)
s.display()
print(s.pop())
s.display()
print(s.peek())
print(s.isempty())
print(s.size())
s.display()


        
    
            