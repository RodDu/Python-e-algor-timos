# 1. Implementar uma função de nome determineSeOrdenado que recebe como parâmetros um inteiro n e lista de inteiros vet e que devolve 1 se os elementos em vet[] estão em ordem crescente e 0 em caso contrário (ou seja, se vet[0] < vet[1] < ... < vet[n-1],  devolve 1 e em qualquer outra configuração devolve 0).

# 2. Fazer um programa principal no qual o usuário digita um número inteiro n (0<n<=40), seguido de n valores inteiros que são armazenados em uma lista (que poderá ter até 40 elementos). Usando a função do item 1, seu programa deve imprimir 1 se a lista está em ordem crescente e 0 em caso contrário.

# Entrada esperada: um inteiro n maior que zero e menor ou igual a 40, seguido de n inteiros - nessa ordem.

# Saída esperada: o valor 1 se a sequência de n números estiver em ordem crescente e 0 em caso contrário.


def determineSeOrdenado(n, vet):
    for i in range(n - 1):
        if vet[i] >= vet[i + 1]:
            return 0
    return 1


n = int(input())
vet = []
for _ in range(n):
    vet.append(int(input()))

print(determineSeOrdenado(n, vet))
