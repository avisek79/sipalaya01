#Fibonacci Series

def fibonacci_series(a,b):
    fib_list=[0,1]
    for i in range(13):
        c=a+b
        fib_list.append(c)
        a=b
        b=c
    print(fib_list)
    print(tuple(fib_list))

a=0
b=1
fibonacci_series(a,b)