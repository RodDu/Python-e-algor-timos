termos = int(input(""))
num1, num2 = 0, 1
contador = 0
while contador < termos:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    contador += 1
    print(num1, end=', ')