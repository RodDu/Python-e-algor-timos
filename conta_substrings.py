string = "Olá mundo, mundo maravilhoso"
substring = "mundo"
posicoes = []

indice = 0
while indice < len(string):
    indice = string.find(substring, indice)
    if indice == -1:
        break
    posicoes.append(indice)
    indice += len(substring)

if posicoes:
    print("A substring foi encontrada nas seguintes posições:", posicoes)
else:
    print("A substring não foi encontrada.")
