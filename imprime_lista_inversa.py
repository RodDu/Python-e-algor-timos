listaNumeros = []

num = float(input("Digite um numero: "))

while num != 0:
    listaNumeros.append(num)
    num = float(input("Digite um numero: "))

tam = len(listaNumeros) - 1
while tam >= 0:
    print(listaNumeros[tam])
    tam = tam - 1
