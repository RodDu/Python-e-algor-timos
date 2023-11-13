#Calculadora de números primos

n =  int(input("Digite um número inteiro positivo (zero para finalizar): "))
while n < 0:
    n =  int(input("Digite um número inteiro positivo (zero para finalizar): "))

while n != 0:
    primo = True
    divisor = n // 2
    if n != 2 and n % 2 == 0:
        primo = False
    else:
        while primo and divisor > 1:
            if n % divisor == 0:
                primo = False
            divisor -= 1
    print("É primo" if primo else "Não é primo")
    
    n =  int(input("Digite um número inteiro positivo (zero para finalizar): "))
    while n < 0:
        n =  int(input("Digite um número inteiro positivo (zero para finalizar): "))
