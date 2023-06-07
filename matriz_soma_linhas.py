# m =  int(input())
# while m <= 0:
#     m = int(input())

# n =  int(input())
# while n <= 0:
#     n = int(input())

# M = []
# l = 0
# c = 0

# for T in range(m*n):
#     if c == 0:
#         M.append([])
#     M[l].append(float(input()))
#     c += 1
#     if c == n:
#         c = 0
#         l += 1

# print(M)


def ler_matriz(m, n):
    M = []
    for i in range(m):
        linha = []
        for j in range(n):
            valor = float(input())
            linha.append(valor)
        M.append(linha)
    return M


def imprimir_matriz(M):
    for i in range(len(M)):
        soma = 0
        for j in range(len(M[i])):
            print("{:.1f}".format(M[i][j]), end=" ")
            soma += M[i][j]
        print("= {:.1f}".format(soma))


m = int(input())
n = int(input())

M = ler_matriz(m, n)

imprimir_matriz(M)
