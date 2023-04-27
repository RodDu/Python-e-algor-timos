idade = 1
somaIdade = 1
qtPessoas = 0


#"Digite as idades para ser feita a média, digite 0 para terminar: "
while idade != 0:
    idade = int(input())
    if idade == 0:
        break
    
    
    
    else:
        if idade > 0:
            qtPessoas += 1
            somaIdade = somaIdade + idade
print("%.2f" % (somaIdade/qtPessoas))