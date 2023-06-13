termos = int(input("Enter the number of terms in the Fibonacci sequence: "))
num1, num2 = 0, 1

for contador in range(termos):
    print(num1, end=', ' if contador < termos - 1 else '\n')
    num3 = num1 + num2
    num1 = num2
    num2 = num3