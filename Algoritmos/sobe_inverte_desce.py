# Faça um programa que leia diversos lista até ser digitado 0 (zero). Mostre os valores em ordem crescente até a metade da lista e em ordem decrescente da metade até o final. Use o comando "reversed()", este comando retorna a lista, ou parte dela, passada como parâmetro, ou seja, dentro dos parênteses, em ordem inversa a que se encontravam os elementos.


# lista = []
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     lista.append(num)

# metade = len(lista) // 2
# lista[:metade] = sorted(lista[:metade])
# lista[metade:] = list(reversed(sorted(lista[metade:])))
# print(*lista)

numeros = []
while True:
    num = int(input())
    if num == 0:
        break
    numeros.append(num)

numeros = sorted(numeros)
metade = len(numeros) // 2  # divisão inteira
numeros[metade:] = list(reversed(numeros[metade:]))
print(*numeros)
