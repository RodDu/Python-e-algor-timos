n1 = int(input("Primeiro número"))
n2 = int(input("Segundo número"))

if n2<n1:
    temp=n1
    n1=n2
    n2=temp

n3 = int(input("Terceiro número"))
if n3<n1:
    n1,n3=n3,n1
if n3<n2:
    n2,n3=n3,n2

print(n1, n2, n3)