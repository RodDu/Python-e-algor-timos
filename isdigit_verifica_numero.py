numero = input("Digite um número inteiro: ")

while not numero.isdigit():
    print("Valor inválido. Digite apenas números inteiros.")
    numero = input("Digite um número inteiro: ")

print("O número digitado foi:", int(numero))
