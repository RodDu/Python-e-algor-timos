# Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

vetor = []
negativos = 0
positivos = 0

for i in range(10):
    vetor.append(int(input("Digite um número: ")))

for i in vetor:
    if i < 0:
        negativos += 1
    else:
        positivos += i

print(f"A quantidade de négativos é {negativos} e a soma dos positivos é {positivos}")
