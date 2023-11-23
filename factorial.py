import time

def factorial(n: int) -> int:
    producto = 1
    for i in range(2, n + 1):
        producto *= i

    return producto

def factorial_r(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial_r(n - 1)

t1 = time.time()    
factorial(500000)
t2 = time.time()
#factorial_r(800)
t3 = time.time()

print(t2 - t1)
print(t3 - t2)