def maior_elemento(lista):
    if not lista:
        return None

    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior


lista = []
n = 1
while n != 0:
    n = int(input("Digite um número inteiro: "))
    if n != 0:
        lista.append(n)

if not lista:
    print("Lista vazia")
else:
    maior = maior_elemento(lista)
    print(maior)
