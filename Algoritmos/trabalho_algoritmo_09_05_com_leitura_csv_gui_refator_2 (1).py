# importa o módulo para leitura de arquivos CSV
import csv

# importa o método para abrir caixa de diálogo
import tkinter as tk
from tkinter import filedialog


def Media(div, exp):
    if exp == 0:
        exp = 1
    return div / exp


# declara variáveis
cont = rh = jur = atend = 0
salaCont = salaRh = salaJur = salaAtend = 0.0

# cria janela para usuário escolher arquivo
root = tk.Tk()

# esconde a janela principal
root.withdraw()

# abre caixa de diálogo para escolha de arquivo
file_path = filedialog.askopenfilename()

# abre o arquivo
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) < 2:  # ignora linhas vazias
            continue
        n = row[0]  # pega o setor do funcionário
        try:
            sal = float(row[1])  # tenta converter salário para float
            if sal < 0:  # ignora salários negativos
                print(f"Salário negativo ignorado: {sal}")
                continue
        except ValueError:  # se falhar, pula a linha atual e continua com a próxima
            print(f"Formato de salário inválido: {row[1]}")
            continue

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
        else:
            print(f"Número de setor inválido: {n}")

somaT = cont + jur + rh + atend

print(
    f"Média da Contabilidade: R$ {Media(salaCont, cont):.2f}\nMédia do RH: R$ {Media(salaRh, rh):.2f}\nMédia do jurídico: R$ {Media(salaJur, jur):.2f}\nMédia do atendimento: R$ {Media(salaAtend, atend):.2f}\nMédia da empresa: R$ {Media((salaCont+salaJur+salaRh+salaAtend),(somaT)):.2f}"
)
