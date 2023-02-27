fibo = []
import time
def fibonacci(n, count, max):
    fibo.append(n)
    if n >= max:
        print("Finished. \n Your number was close to count " + str(count + 1))
        time.sleep(5)
        exit()
    if n == 0:
        return n
    if n == 1:
        print(n)
        print(n)
        return fibonacci(n + n, count + 1, max)
    else:
        print(n)
        return fibonacci(n + fibo[count-1], count + 1, max)

max = int(input("Enter max: "))
print(fibonacci(1, 0, max))
