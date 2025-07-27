def binary(ls,target,left,right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if ls[mid] == target:
        return mid
    elif ls[mid] > target:
        return binary(ls, target,mid - 1,left )
    else:
        return binary(ls,target,mid+1,right)
ls=[1,2,3,4,5]
target =3

left = 0
right = len(ls)-1
res =binary(ls,target,left,right)

print(res)



# def binary(ls,target,left,right):
#     if left > right:
#         return -1
    
#     mid = (left+right)//2

#     if ls[mid] == target:
#         return mid
#     elif ls[mid] > target:
#         return binary(ls,target,left,mid-1)
#     else:
#         return binary(ls, target,mid+1,right)
# ls=[12, 3, 2, 57, 65, 7, 5]
# n=len(ls)

# left,right,target = 0,n-1,3

# res = binary(ls,target,left,right)

# print(res)