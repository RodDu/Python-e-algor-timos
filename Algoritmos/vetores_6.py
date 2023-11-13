# Faça um programa que receba do usuário um vetor com 10 posições. Em seguida devera ser impresso o maior e o menor elemento do vetor.

vetor = []

for i in range(10):
    vetor.append(int(input("Digite um número: ")))


print(
    "O valor máximo é %d e o valor mínimo é %d" % (max(vetor), min(vetor))
)  # outra forma de fazer o print é: print(f"max(vetor), min(vetor))
