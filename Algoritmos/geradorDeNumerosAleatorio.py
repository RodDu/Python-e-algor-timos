#gerar lista de 20 numeros aleatorios entre 1 e 100
import random

lista = []
for i in range(20):
    lista.append(random.randint(1,100))
    print(lista[i])
    