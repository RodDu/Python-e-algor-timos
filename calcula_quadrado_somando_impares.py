#O quadrado de um número natural n é dado pela soma dos n primeiros números naturais (1 + 3 + 5 + ... + n).
#Por exemplo, o quadrado de 5 é dado pela soma dos 5 primeiros números naturais (1 + 3 + 5 + 7 + 9) = 25.
#Escreva um programa que receba um número natural n e imprima o quadrado de n somando a quantidade de números impares consecutivos que correspondem a n.


n = int(input("Digite um número natural: "))

soma = 0

for i in range(1, n * 2, 2):
        soma += i
        
print(soma)
