# adicionar idade de 20 pessoas e dizer quantos são menores de idade

# gerar uma lista aleatoria de 20 elementos entre 1 e 80

import random

idade = []
menor = 0
for i in range(20):
    idade.append(random.randint(1,100))
    if idade[i] < 18:
        menor = menor + 1
      
print(menor)