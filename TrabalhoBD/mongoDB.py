from pymongo import MongoClient
from tkinter import *
import tkinter.colorchooser
import datetime
import time

# Crie uma instância do cliente MongoDB
client = MongoClient()

# Conecte-se ao servidor MongoDB
db = client.local

#print(db.create_collection())
# Cria ou recebe a coleção 
alunos = db['Alunos']
text="""
-----------------------------------------------------

1 - Mostrar todos os alunos
2 - Pesquisar alunos pelo nome
3 - Ver alunos do semestre
4 - Editar dados do aluno 
5 - Adicionar aluno
0 - Parar

-----------------------------------------------------
"""

entrada = input(text)

while entrada != '0':
    match entrada:
        case '1':
            for alun in alunos.find({}, { "aluno": 1, 'nascimento': 1, "sexo": 1, "turma":1, 'cor_favorita':1}):
                ao = "o"
                sex = "Masculino"
                if alun['sexo']=="F":
                    ao, sex = "a", "Feminino"
                    
                print(f"Alun{ao}: {alun['aluno']}, nascid{ao}: {str(alun['nascimento'].day)+'/'+str(alun['nascimento'].month)+'/'+str(alun['nascimento'].year)}, sexo: {sex}, turma: {alun['turma']}, cor favorita: {alun['cor_favorita']}")
        case '2':

            for alun in alunos.find({'aluno':{'$regex':f"{input('Nome do aluno: ')}"}}, { "aluno": 1, 'nascimento': 1, "sexo": 1, "turma":1, 'cor_favorita':1}):
                ao = "o"
                sex = "Masculino"
                if alun['sexo']=="F":
                    ao, sex = "a", "Feminino"
                print(f"Alun{ao}: {alun['aluno']}, nascid{ao}: {str(alun['nascimento'].day)+'/'+str(alun['nascimento'].month)+'/'+str(alun['nascimento'].year)}, sexo: {sex}, turma: {alun['turma']}, cor favorita: {alun['cor_favorita']}")

        case '3':
            for alun in alunos.find({'turma':{'$regex':f"{input('Semestre do aluno: ')}"}}, { "aluno": 1, 'nascimento': 1, "sexo": 1, "turma":1, 'cor_favorita':1}):
                ao = "o"
                sex = "Masculino"
                if alun['sexo']=="F":
                    ao, sex = "a", "Feminino"

                print(f"Alun{ao}: {alun['aluno']}, nascid{ao}: {str(alun['nascimento'].day)+'/'+str(alun['nascimento'].month)+'/'+str(alun['nascimento'].year)}, sexo: {sex}, turma: {alun['turma']}, cor favorita: {alun['cor_favorita']}")
        case '4':
            selec = {'aluno':f"{input('Nome do aluno: ')}", 'turma':{'$regex':f"{input('Semestre do aluno: ').upper()}"}}
            veri = True
            data = datetime.datetime.now()
            while veri:
                try:
                    data = datetime.datetime(int(input("Ano de nascimento: ")), int(input("Mês de nascimento: ")), int(input("Dia de nascimento: ")))
                    veri = False
                except:
                    print("Data invalida!")
            alunos.update_one(selec, {"$set":{'aluno': input('Nome: '), 'nascimento': data, 'sexo':input("Sexo (M ou F): ").strip().upper(), 'turma': input("Semestre de entrada (sSaaa): ").upper(), 'cor_favorita': tkinter.colorchooser.askcolor()[1]}})

        case '5':

            veri = True
            while veri:
                try:
                    data = datetime.datetime(int(input("Ano de nascimento: ")), int(input("Mês de nascimento: ")), int(input("Dia de nascimento: ")))
                    veri = False
                except:
                    print("Data invalida!")
            alunos.insert_one({'aluno': input('Nome: '), 'nascimento': data, 'sexo':input("Sexo (M ou F): ").strip().upper(), 'turma': input("Semestre de entrada (sSaaa): ").upper(), 'cor_favorita': tkinter.colorchooser.askcolor()[1]})
        case _:
            1
    time.sleep(4)
    entrada = input(text)
