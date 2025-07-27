def fibi(n):
    if n==0:
        return 0
    elif n== 1:
        return 1
    
    return fibi(n-1) + fibi(n-2)


print(fibi(10))