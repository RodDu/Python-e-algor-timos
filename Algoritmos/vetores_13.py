# Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontra o maior e o menor valor.

lista = []

for i in range(5):
    lista.append(int(input("Digite um valor: ")))

print(f"O maior valor é {max(lista)} e está na posição {lista.index(max(lista))}.")
print(f"O menor valor é {min(lista)} e está na posição {lista.index(min(lista))}.")
