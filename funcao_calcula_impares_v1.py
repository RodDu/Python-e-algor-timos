def calcula(n):
    soma_geral = 0
    subsequencias = []

    for i in range(n):
        subsequencia = list(map(int, input().split()))
        soma_subsequencia = sum(x for x in subsequencia if x % 2 == 1)
        soma_geral += soma_subsequencia
        subsequencias.append(soma_subsequencia)

    for soma in subsequencias:
        print(soma)

    print(soma_geral)


n = int(input("Digite o número de subsequências: "))
calcula(n)
