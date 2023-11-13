# soma os digitos de uma sequencia de numeros

n = int(input("Digite um numero inteiro: "))

soma = 0

while n > 0:
    soma = soma + n % 10
    n = n // 10
    
print(soma)
