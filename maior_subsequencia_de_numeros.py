n = int(input("Digite o número de elementos da sequência: "))
lista = []

def maior_ss_encontrada(n, lista):
    if n == 0:
        return 0
    size = [1] * n

    for i in range(1, n):
        for j in range(i):
            if lista[i] >= lista[j]:
                size[i] = max(size[i], size[j] + 1)

    return max(size)

for i in range(n):
    valor = int(input(f"Digite o {i+1}º valor da sequência: "))
    lista.append(valor)

print(f"O tamanho da maior subsequência crescente é {maior_ss_encontrada(n, lista)}")
