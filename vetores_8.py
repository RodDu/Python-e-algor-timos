# Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.


lista = []

for i in range(6):
    lista.append(int(input("Digite um valor: ")))
    lista.sort()
    # lista.reverse()

print(f"Os valores digitados em ordem foram {lista}")
print(f"Os valores digitados em ordem inversa foram {lista[::-1]}")
