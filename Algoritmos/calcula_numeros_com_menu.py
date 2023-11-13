#calculadora de numeros via input que apresenta um menu para impressão de resultados


numeros = []
while True:
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

while True:
    opcao = int(input("Escolha uma opção: (1) Soma dos números digitados; (2) Quantidade de números digitados; (3) Média dos números digitados; (4) Maior número digitado; (5) Menor número digitado; (6) Média dos números pares; (7) Sair"))
    if opcao == 1:
        soma = sum(numeros)
        print("Soma dos números digitados:", soma)
    elif opcao == 2:
        quantidade = len(numeros)
        print("Quantidade de números digitados:", quantidade)
    elif opcao == 3:
        media = sum(numeros) / len(numeros)
        print("Média dos números digitados:", media)
    elif opcao == 4:
        maior = max(numeros)
        print("Maior número digitado:", maior)
    elif opcao == 5:
        menor = min(numeros)
        print("Menor número digitado:", menor)
    elif opcao == 6:
        numeros_pares = [n for n in numeros if n % 2 == 0]
        if len(numeros_pares) > 0:
            media_pares = sum(numeros_pares) / len(numeros_pares)
            print("Média dos números pares:", media_pares)
        else:
            print("Não há números pares na sequência.")
    elif opcao == 7:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
