# Faça um programa que leia um vetor de 8 posiçães e, em seguida, leia também dois valores X e Y quaisquer correspondentes a duas posiçães no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posiçães X e Y.

# Lendo um vetor de 8 posições
vetor = []
for i in range(8):
    valor = int(input("Digite um valor inteiro para a posição {}: ".format(i)))
    vetor.append(valor)

# Lendo os valores X e Y
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

# Verificando se os valores de X e Y estão dentro do intervalo válido
if x < 0 or x >= len(vetor) or y < 0 or y >= len(vetor):
    print("Posições inválidas!")
else:
    # Calculando e exibindo a soma dos valores nas posições X e Y
    soma = vetor[x] + vetor[y]
    print("A soma dos valores nas posições {} e {} é: {}".format(x, y, soma))
