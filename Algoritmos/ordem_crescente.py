n1 = int(input("Primeiro número"))
n2 = int(input("Segundo número"))
n3 = int(input("Terceiro número"))

if n1<=n2 and n1<=n3:
    if n2<=n3:
        print(n1, n2, n3) #a
    else:
        print(n1, n3, n2) #b
else:
    if n2<=n1 and n2<=n3:
        if n1<=n3:
            print(n2, n1, n3) #c
        else:
            print(n2, n3, n1) #d
    else:
        if n1<=n2:
            print(n3, n1, n2) #e
        else:
            print(n3, n2, n1) #d