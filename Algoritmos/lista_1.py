# lista = []
# for cont in range(5):
#     n = int(input("Digite um valor: "))
#     lista.append(n)

# for pos in range(4, -1, -1):
#     print(lista[pos])

####################################################################


# lista = []
# n = int(input("Digite um valor: "))
# while n != 0:
#     lista.append(n)
#     n = int(input("Digite um valor: "))

# for pos in range(4, -1, -1):

######################################################################


algI = []
nome = input("Digite o nome do aluno: ")
nome = nome.upper()
while nome != "FIM":
    algI.append(nome)
    algI.append(float(input("Digite a 1ª nota do aluno: ")))
    algI.append(float(input("Digite a 2ª nota do aluno: ")))
    algI.append(float(input("Digite a 3ª nota do aluno: ")))
    nome = input("Digite o nome do aluno: ")
    nome = nome.upper()

pos = 0
while pos < len(algI):
    print(algI[pos], end="\t")
    media = (algI[pos + 1] + algI[pos + 2] + algI[pos + 3]) / 3
    print(f"{media:.2f}", end="\t")
    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
    pos += 4

print(*algI)
