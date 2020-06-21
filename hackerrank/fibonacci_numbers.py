def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

for n in range(0,10):
    print(n, fibonacci(n))
