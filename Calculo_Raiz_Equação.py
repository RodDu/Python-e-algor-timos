import math

# Entrada dos coeficientes a, b e c
a = float(int("Digite o coeficiente a: "))
b = float(int("Digite o coeficiente b: "))
c = float(int("Digite o coeficiente c: "))

# Cálculo do discriminante
delta = b**2 - 4*a*c

# Verificação do valor do discriminante e cálculo das raízes
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = (-b)/(2*a)
    print("A equação possui uma raiz real: x =", x)
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("A equação possui duas raízes reais: x1 =", x1, "e x2 =", x2)
    