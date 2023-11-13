num = int(input())
def fibonacci(n):
    t1 = 1
    t2 = 1
    t3 = 0
    for _ in range(0, n):
        print(t1)
        t3 = t1 + t2
        t1 = t2
        t2 = t3
fibonacci(num)