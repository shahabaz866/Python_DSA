# # remove midle element
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.lenght = 0
    
    def remove_mid(head):
        if not head or not head.next:
            return None
        

        slow = head
        fast = head
        prev = None


        while fast and fast.next:
            fast = fast.next.next
            prev = slow 
            slow = slow.next 

        if prev : 
            prev.next = slow.next 
        
        return head 
    
        

def binary(ls,target,left,right):

    if left > right :
        return -1
    
    mid = (left+right)//2
    if ls[mid] == target :
        return mid
    elif ls[mid] < target:
        return binary(ls,target,mid+1,right)
    else:
        return binary(ls,target,left,mid-1)

ls= [1,2,3,4,5,6,7]
left = 0
right = len(ls) -1
target = 5

res = binary(ls,target,left,right)
print(res)