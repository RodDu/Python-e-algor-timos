#Vestibular e Notas

nome = input("Digite o nome do candidato:")
p1 = float(input("Digite a nota obtida em Português:"))
m1 = float(input("Digite a nota obtida em Matemática:"))
c1 = float(input("Digite a nota obtida em Conhecimentos Gerais:"))

#Nome e nota em cada prova
media = (p1 + m1 + c1 )/3

if p1>4 and m1>4 and c1>4 and media > 5:
    print(nome,", suas notas são: \n Português = ",p1, ", \n Matemática= ",m1, ", \n Conhecimentos Gerais = ", c1, "\n Sua média é = ", "%.2f" % (media), "Você foi aprovado!", sep='')
else:
    print(nome,", suas notas são: \n Português = ",p1, ", \n Matemática= ",m1, ", \n Conhecimentos Gerais = ", c1, "\n Sua média é = ", "%.2f" % (media), "\n Você não foi aprovado.", sep='')
