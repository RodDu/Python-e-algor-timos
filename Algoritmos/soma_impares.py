n = int(input())
soma = 0
while n != 0:
    x = int(n)
    if x % 2 != 0:
        soma += x
    n = int(input())
print(soma)