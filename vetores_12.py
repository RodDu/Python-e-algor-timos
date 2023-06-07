# Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a média dos valores.

lista = []

for i in range(5):
    lista.append(int(input("Digite um valor: ")))

print(
    f"Você digitou os valores {lista}, o maior valor é {max(lista)}, o menor é {min(lista)} e a média é {sum(lista)/len(lista)}"
)


# {int(sum(lista)/len(lista))}
