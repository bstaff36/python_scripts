
def fibonacci(n): 
    a, b = 0, 1
    if n == 1: 
        return a
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b

def which_fibonacci(x):
    check_fib = False
    fib = 1
    while not check_fib:
        if fibonacci(fib) == x:
            check_fib = True
            return fib
        elif fibonacci(fib) > x:
            check_fib = True
            return 0
        else:
            fib+=1

def next_fibonacci(x):
    
    check_fib = False
    while not check_fib:
        if which_fibonacci(x) != 0:
            print(fibonacci(which_fibonacci(x)+1))
            check_fib = True
        else: 
            x+=1

a= which_fibonacci(2)
b= which_fibonacci(5)
c= which_fibonacci(12)
print(a)
print(b)
print(c)
next_fibonacci(2)
next_fibonacci(3)
next_fibonacci(4)
