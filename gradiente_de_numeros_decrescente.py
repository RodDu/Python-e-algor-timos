n = int(input("Enter a positive integer: "))

while n <= 0:
    n = int(input("Enter a positive integer: "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    for k in range(n-i):
        print('0', end=' ')
    print()
