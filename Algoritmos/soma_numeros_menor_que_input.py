total = int(input("Digite um número inteiro"))
soma = 0
i = 1
ms = 0
mn = 0
while soma + i <= total:
    soma += i
    if soma >= ms:
        ms = soma
        mn = i
    i += 1
    
    
    
print("A maior soma de números naturais com resultado inferior a ",total, "é: ",ms, "de 1 a ",mn)

