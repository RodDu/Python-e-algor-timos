# Faça um programa que leia 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.

lista = []

for i in range(6):
    numero = int(input("Digite um número inteiro par: "))
    while numero % 2 != 0:
        print("Valor inválido!")
        print("Digite um número inteiro par: ")
        numero = int(input("Digite um número inteiro par: "))
    lista.append(numero)

print(*lista[::-1])


# valores = []
# for i in range(6):
#     valor = int(input("Digite um valor inteiro par: "))
#     while valor % 2 != 0:
#         valor = int(input("Digite um valor inteiro par: "))
#     valores.append(valor)

# print("Valores lidos na ordem inversa:")
# for valor in reversed(valores):
#     print(valor)
