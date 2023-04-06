n = int(float(input()))
x = float(input())

def potencia(x, n):
    resultado = 1
    for i in range(n):
        resultado *= x
    return resultado

print(potencia(x, n))