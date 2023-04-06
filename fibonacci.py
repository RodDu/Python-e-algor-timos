n1 = 1
n2 = 1
proximo_numero = int(input())
print('{}, {}'.format(n1,n2), end='')
conta = proximo_numero -2
while conta !=0:

    n3 = n1 + n2
    print(', {}'.format(n3),end='')
    n1 = n2
    n2 = n3
    conta = conta-1