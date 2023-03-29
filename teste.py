soma_idades = 0
quantidade_individuos = 0

while True:
    idade = int(input("Informe a idade do indivíduo (ou 0 para encerrar): "))
    if idade == 0:
        break
    soma_idades += idade
    quantidade_individuos += 1

if quantidade_individuos > 0:
    media_idades = soma_idades / quantidade_individuos
    print("A idade média do grupo de indivíduos é: {:.2f}".format(media_idades))
else:
    print("Não foi informada nenhuma idade.")