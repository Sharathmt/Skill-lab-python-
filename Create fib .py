def fib(n):
    if n<=1:
        return n
    else:
        c = fib(n-1)+fib(n-2)
        return c
n=int(input("Enter a number:"))
for i in range(n):
    print(fib(i),end=" ")
