
# reverse string using stack

# def reversestring(strs):
#     stack=[]
#     for s in strs:
#         stack.append(s)

#     reversed_str = ''
#     while stack:
#         reversed_str += stack.pop()
#     return reversed_str

# strs = "hello"
# res = reversestring(strs)

# print(res)


# queue ,nq,dq,front operation

# class Queue:
#     def is_empty(self):
#         return len(self.queue) == 0

#     def __init__(self):
#         self.queue = []
    
#     def enque(self,data):
#         self.queue.append(data)
#     def deque(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         return "que is empty"
#     def peek(self):
#         if not self.is_empty():
#             return self.queue[0]
#         return "que is empty"
    
#     def size(self):
#         return len(self.queue)
    



# q= Queue()

# q.enque(10)
# q.enque(11)
# q.enque(13)
# q.enque(14)

# print("dq",q.deque())
# print("peeked",q.peek())
# print("size",q.size())

# merge sort



def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        l = arr[:mid]
        r= arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0


        while i < len(l) and j< len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1



arr=[64, 34, 25, 12, 22, 11, 90]

merge_sort(arr)

print(arr)