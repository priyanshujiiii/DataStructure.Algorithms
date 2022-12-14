import time

def fun1(n):
    return n*(n + 1)/2

def fun2(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def fun3(n):
    sum = 0 
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sum += 1
            
    return sum


fun1timestart = time.time()
print(fun1(100000))
fun1timeend = time.time()
print('fun1 time ', fun1timeend - fun1timestart)

fun2timestart = time.time()
print(fun2(100000))
fun2timeend = time.time()
print('fun2 time ', fun2timeend - fun2timestart)

fun3timestart = time.time()
print(fun3(100000))
fun3timeend = time.time()
print('fun3 time ', fun3timeend - fun3timestart)
