#Recursion - definir algo en terminos de si mismo
#recursion - defining something in terms of itself

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#0,1,1,2,3,5,8,13,21,34
#0,1,2,3,4,5,6,7, 8, 9
print(fibonacci(8))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(9))

