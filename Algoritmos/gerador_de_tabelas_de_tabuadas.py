# Gerador de tabelas de tabuadas

# Leitura dos valores de p e u
p = int(input("Digite o valor de p: "))
u = int(input("Digite o valor de u: "))

# Verificação de valores inválidos

while p < 1:
    p = int(input("Digite o valor de p: "))
    
while u < 1:
    u = int(input("Digite o valor de u: "))

    

# Troca os valores se p for maior que u
if p > u:
    p, u = u, p

# Desenho do cubo com as tabuadas
for i in range(p, u+1):
    for j in range(1, 11):
        linha = ""
        for k in range(p, i+1):
            linha = k*j
        print(linha,  "\t", end='')
    print("")


