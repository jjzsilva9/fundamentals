def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n-1)+fib(n-2)

i = 0
while True:
    i+=1
    print(fib(i))
