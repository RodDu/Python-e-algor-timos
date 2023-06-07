# Leia um vetor de 10 posições. Imprimir quantos valores pares ele possui.

vetor = []
pares = []
for i in range(10):
    vetor.append(int(input("Digite um valor: ")))

for i in range(10):
    if vetor[i] % 2 == 0:
        pares.append(i)

print(len(pares))
