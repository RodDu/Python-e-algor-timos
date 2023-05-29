import csv


def Media(div, exp):
    return div / exp


cont = rh = jur = atend = 0
salaCont = salaRh = salaJur = salaAtend = 0.0

with open("employee_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) < 2:  # skip rows that don't have enough fields
            continue
        n = row[0]
        sal = float(row[1])

        if n == "1":
            cont += 1
            salaCont += sal
        elif n == "2":
            rh += 1
            salaRh += sal
        elif n == "3":
            jur += 1
            salaJur += sal
        elif n == "4":
            atend += 1
            salaAtend += sal

somaT = cont + jur + rh + atend

if somaT == 0:
    somaT = 1
if cont == 0:
    cont = 1
if rh == 0:
    rh = 1
if jur == 0:
    jur = 1
if atend == 0:
    atend = 1

print(
    f"Média da Contabilidade: R$ {Media(salaCont, cont):.2f}\nMédia do RH: R$ {Media(salaRh, rh):.2f}\nMédia do jurídico: R$ {Media(salaJur, jur):.2f}\nMédia do atendimento: R$ {Media(salaAtend, atend):.2f}\nMédia da empresa: R$ {Media((salaCont+salaJur+salaRh+salaAtend),(somaT)):.2f}"
)
