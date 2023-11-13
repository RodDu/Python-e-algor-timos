# Pedro Henrique Botter Vasconcelos Fernandes
# Rodrigo Flores Duarte

# Enunciado
# Crie um programa em Python que peça ao usuário para selecionar o setor
# correspondente em que ele trabalha (1 - contabilidade, 2 - RH, 3 - jurídico e
# 4 - atendimento) e depois peça que ele digite o seu salário.
# ⚫ O programa deverá informar a média salarial dos setores e, ao final,
# informar a média salarial de toda a empresa.
# ⚫ O programa deverá funcionar até que o usuário digite 0 (zero) para o
# setor.
# ⚫ Deve ser criada uma função para calcular a média, devem ser usadas
# repetições (while ou for), bem como estruturas "if" ou "else" para o
# programa funcionar.


def Media(div, exp):
    if exp == 0:
        exp = 0
    return div / exp


text = "Qual área ele trabalha\n1 - Contabilidade\n2 - RH\n3 - Jurídico \n4 - Atendimento\n0 - Para finalizar: "
textSal = "Salario do funcionário: "

n = input(text)
cont = rh = jur = atend = 0
salaCont = salaRh = salaJur = salaAtend = 0.0
while n != "0":
    if n == "1":
        sal = float(input(textSal))
        cont += 1
        salaCont += sal

    elif n == "2":
        sal = float(input(textSal))
        rh += 1
        salaRh += sal

    elif n == "3":
        sal = float(input(textSal))
        jur += 1
        salaJur += sal

    elif n == "4":
        sal = float(input(textSal))
        atend += 1
        salaAtend += sal
    else:
        print("Coloque uma entrada válida")
    n = input(text)
somaT = cont + jur + rh + atend
# if somaT == 0:
#     somaT = 1
# if cont == 0:
#     cont = 1
# if rh == 0:
#     rh = 1
# if jur == 0:
#     jur = 1
# if atend == 0:
#     atend = 1
print(
    f"Média da Contabilidade: R$ {Media(salaCont, cont):.2f}\nMédia do RH: R$ {Media(salaRh, rh):.2f}\nMédia do jurídico: R$ {Media(salaJur, jur):.2f}\nMédia do atendimento: R$ {Media(salaAtend, atend):.2f}\nMédia da empresa: R$ {Media((salaCont+salaJur+salaRh+salaAtend),(somaT)):.2f}"
)
