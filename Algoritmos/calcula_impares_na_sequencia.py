#construa um algoritimo em python que receba um número natural positivo n (n>=1) e a seguir n listas de valores inteiros não-nulos, cada qual seguida por um 0 (finalizador da subsequencia), calcular a soma dos números ímpares de cada subsequencia e imprimi-los (assim que ler o finalizador 0). A função calcula(n) receberá o valor de n e impriomirá a saída.

def calcula(n):
somaP = 0
    for i in range(n):
        soma = 0
        while True:
            x = int(input())
            if x == 0:
                break
            if x % 2 != 0:
                soma += x
        print(soma)

    
n = int(input("Digite o número de sequências: "))

calcula(n)