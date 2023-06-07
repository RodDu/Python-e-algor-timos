# Faça um programa que possua um vetor denominado A que armazene 6 nu´meros intei- ros. O programa deve executar os seguintes passos: (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7. (b) Armazene em uma varia´vel inteira (simples) a soma entre os valores das posic¸o˜es A[0], A[1] e A[5] do vetor e mostre na tela esta soma. (c) Modifique o vetor na posic¸a˜o 4, atribuindo a esta posic¸a˜o o valor 100. (d) Mostre na tela cada valor do vetor A, um em cada linha.


# Passo (a): Atribuindo os valores ao vetor A
A = [1, 0, 5, -2, -5, 7]

# Passo (b): Calculando a soma dos valores nas posições A[0], A[1] e A[5]
soma = A[0] + A[1] + A[5]
print("A soma dos valores é:", soma)

# Passo (c): Modificando o valor na posição 4 do vetor
A[4] = 100

# Passo (d): Mostrando cada valor do vetor A em uma linha
print("Valores do vetor A:")
for valor in A:
    print(valor)
