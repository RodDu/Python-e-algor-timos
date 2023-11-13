contador = 0
soma = 0
num = 1
media_pares = 0
quantidade_pares = 0
soma_pares = 0

while num != 0:
    num = int(input(""))
    soma = soma + num
    contador += 1
    if num % 2 == 0:
        soma_pares += num
        quantidade_pares += 1
 
else:
    print(soma, contador-1, "%.2f" % (soma/contador-1), soma_pares / quantidade_pares)
