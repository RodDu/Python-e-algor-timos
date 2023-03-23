n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1==0 or n2==0:
    print("Zero")
else:
    if n2>n1:
        n1,n2=n2,n1
    if n1%n2==0:
        print("Sim")
    else:
        print("Não")
