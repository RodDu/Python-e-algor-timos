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
contT = {}
TotaldeEmpregados = TotaldeSalario = 0


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
        n = (
            row[0].lower().strip()
        )  # pega o setor do funcionário, passados para letras minúsculas e sem espaços no inicio e final
        if (
            len(n) == 2
        ):  # Verifica se o setor tem 2 carácteres, considerando assim que ele é uma sigla
            n = n.upper()  # Passa o setor para letras maiúsculas

        try:
            sal = float(row[1])  # tenta converter salário para float
            if sal < 0:  # ignora salários negativos
                print(f"\033[31mSalário negativo ignorado: {sal}\033[0m")
                continue
        except ValueError:  # se falhar, pula a linha atual e continua com a próxima
            print(f"\033[33mFormato de salário inválido: {row[1]}\033[0m")
            continue

        if n:  # Verifica se algo está escrito no campo do setor
            if not contT.get(n):  # Confere se existe o setor no dicionário
                TotaldeEmpregados += 1  # Soma o total de salários que passaram
                TotaldeSalario += sal  # Soma o montante dos salários

                contT = {**contT, n: [0, 0]}  # Cria o campo caso não exista

            contT = {
                **contT,
                n: [contT[n][0] + 1, float(sal) + contT[n][1]],
            }  # Adiciona no dicionário com base no nome


for linha in contT:
    print(f"Média do setor {linha}: R$ {Media(contT[linha][1], contT[linha][0]):.2f}")

print(f"Média da empresa: R$ {Media(TotaldeSalario, TotaldeEmpregados):.2f}")
