# Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.

notas = []

for i in range(15):
    notas.append(float(input("Digite a nota do aluno: ")))

media = sum(notas) / len(notas)

print(f"A média da turma é: {media:.2f}")
