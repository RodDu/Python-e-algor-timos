# Escreva um programa que leia 10 números inteiros e os armazene em um vetor.

vetor = []

for i in range(10):
    vetor.append(int(input("Digite um némero: ")))

# Imprima o vetor, o maior elemento e a posição que ele se encontra.
print(vetor, max(vetor), vetor.index(max(vetor)) + 1)

# Imprima o vetor, o menor elemento e a posição que ele se encontra.
print(vetor, min(vetor), vetor.index(min(vetor)) + 1)
