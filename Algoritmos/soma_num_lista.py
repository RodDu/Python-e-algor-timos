# Escreva um programa em Python que leia vários valores inteiros até ser digitado zero. Todos os valores, exceto o zero, deverão ser armazenados em uma lista. Escreva a função soma_elementos que recebe como parâmetro a lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida. Não use a função "sum"


def soma_elementos(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma


numeros = []
while True:
    num = int(input())
    if num == 0:
        break
    numeros.append(num)

print(soma_elementos(numeros))
