x = int(input())
y = int(input())
soma = 0
quant = 0
nums = 0
while x != 0 and y != 0:
    soma = x+y
    nums += 2
    quant +=1
    print(soma)
    x = int(input())
    y = int(input())
print(f"quantidade de números digitados: {nums} \nquantidade de somas realizadas {quant}")