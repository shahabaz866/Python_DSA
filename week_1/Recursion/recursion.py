# #  factorials...

# def factorial(n):
#     if n == 0 or n == 1:  
#         return 1
#     return n * factorial(n - 1) 

# num = 5
# print(f"Factorial of {num} is {factorial(num)}")



# #  Fibonacci ...

# def fibonacci(n):
#     if n <= 0:
#         return "Invalid Input"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2) 

# n = 6
# print(f"The {n}th Fibonacci number is {fibonacci(n)}")




def sum(arr,i=0,s=0,ls=[]):

    if len(arr) is i:
        return ls
    if arr [i] % 2 != 0:

         ls.append(arr[i]) 

    return sum(arr,i+1,s,ls)

    
one =[1,2,3,4,5]
res =sum(one)
print(res)