# Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos. Os valores devem ser gravados em um vetor.

valores = []

# Lendo 6 valores inteiros e armazenando no vetor
for i in range(6):
    valor = int(input("Digite um valor inteiro: "))
    valores.append(valor)

# Mostrando os valores lidos na tela
print("Valores lidos:")
for valor in valores:
    print(valor)
