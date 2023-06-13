def nomeMaisCurto(nomes):
    pos_menor = 0
    for i in range(len(nomes)):
        nomes[i] = nomes[i].strip().capitalize()
        if len(nomes[i]) < len(nomes[pos_menor]):
            pos_menor = i
    return nomes[pos_menor]


nomes = []
for i in range(5):
    nomes.append(input("Digite 5 nomes:"))

print(nomeMaisCurto(nomes))
