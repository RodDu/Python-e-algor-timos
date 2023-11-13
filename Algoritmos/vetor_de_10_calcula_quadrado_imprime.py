# Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor.  Os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos.

# Criando vetores vazios para armazenar os conjuntos
conjunto_original = []
conjunto_quadrado = []

# Lendo o conjunto de números reais e armazenando no vetor conjunto_original
print("Digite os valores do conjunto:")
for i in range(10):
    valor = float(input("Digite um número real: "))
    conjunto_original.append(valor)

# Calculando o quadrado das componentes e armazenando no vetor conjunto_quadrado
for valor in conjunto_original:
    quadrado = valor**2
    conjunto_quadrado.append(quadrado)

# Imprimindo ambos os conjuntos
print("Conjunto Original:")
for valor in conjunto_original:
    print(valor)

print("Conjunto Quadrado:")
for valor in conjunto_quadrado:
    print(valor)


# valores = []

# for i in range(10):
#     valor = int(input("Digite um valor inteiro: "))
#     valores.append(valor)
#     valores[i] = valores[i] ** 2

# print("Valores lidos:")
# for valor in valores:
#     print(valor)
