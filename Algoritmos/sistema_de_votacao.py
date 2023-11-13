#SISTEMA DE VOTAÇÃO
c1 = c2 = c3 = c4 = branco = nulo = 0

votos = int(input('Digite seu voto: '))
while votos < 0:
    votos = int(input('Digite seu voto: '))
while votos != 0:
    if votos == 1:
        c1 += 1
    elif votos == 2:
        c2 += 1
    elif votos == 3:
        c3 += 1
    elif votos == 4:
        c4 += 1
    elif votos == 5:
        branco += 1
    elif votos == 6:
        nulo += 1
    else:
        print('Voto invalido')
        
    votos = int(input('Digite seu voto: '))
    while votos < 0:
        votos = int(input('Digite seu voto: '))
    tVotos = c1 + c2 + c3 + c4 + branco + nulo
        
print(" VOTOS:",tVotos,"\n","CANDIDATO 1:",c1,"\n","CANDIDATO 2:",c2,"\n","CANDIDATO 3:",c3,"\n","CANDIDATO 4:",c4,"\n","BRANCO:",branco,"\n","NULO:",nulo,"\n","PERCENTUAL DE VOTOS BRANCOS:",branco/tVotos*100,"%\n","PERCENTUAL DE VOTOS NULOS:",nulo/tVotos*100,"%\n")


