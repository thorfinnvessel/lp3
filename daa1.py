#non recursive
n = int(input("enter value of n:"))
a = 0
b = 1

print("Fibonacci series:")

for i in range(n):
    print(a,end=" ")
    c = a+b
    a = b
    b = c

#---------------------------------------------------
#recursive

def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))

print("Fibonacci series:")

for i in range(n):
    print(fib(i),end = " ")