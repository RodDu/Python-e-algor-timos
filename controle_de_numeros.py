contador = 0
soma = 0
num = 1
maior = num
menor = num
media_pares = 0
quantidade_pares = 0
soma_pares = 0
quantidade = 0

while num != 0:
    num = int(input(""))
    soma = soma + num
    contador += 1
    if num > maior:
        maior = num 
    if num < menor or quantidade == 1:
        menor = num
    if num % 2 == 0 and num > 0:
        soma_pares += num
        quantidade_pares += 1
 
else:
    print(soma,"\n",contador-1,"\n","%.2f" % (soma / (contador - 1)),"\n", maior,"\n",menor,"\n", soma_pares / quantidade_pares)
