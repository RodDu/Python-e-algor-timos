def push(p, placa, manobras):
    p.append(placa)
    p.append(manobras)


def pop(p):
    if len(p) == 0:
        return -1, -1
    else:
        return p.pop(), p.pop()  # manobras e placa


pEst = []
pRua = []

opcao = "X"
while opcao != "F":
    print("-" * 50)

    print("Menu")
    print(" [ E ] Entrada de veículo ")
    print(" [ S ] Saída de veículo ")
    print(" [ M ] Mostrar estacionamento ")
    print(" [ F ] Finalizar ")
    opcao = input("Digite a opção desejada: ").upper()

    match opcao:
        case "E":
            print("Entrada de veículo")
            if len(pEst) == 20:
                print("Estacionamento cheio...")
            else:
                pl = input("Digite a placa do veículo: ").upper()
                push(pEst, pl, 0)
                print(pl, "carro estacionado com sucesso!")

        case "S":
            print("Saída de veículo")
            if len(pEst) == 0:
                print("Estacionamento vazio!")
            else:
                pl = input("Digite a placa do veículo para sair: ").upper()
                if not (pl in pEst):
                    print("Veículo não encontrado no estacionamento!")
                else:
                    manobras, placa = pop(pEst)
                    while placa != pl:
                        push(pRua, placa, manobras)
                        manobras, placa = pop(pEst)

                    manobras, placa = pop(pRua)
                    while placa != -1:
                        push(pEst, placa, manobras + 1)
                        manobras, placa = pop(pRua)
                    print(pl, "carro saiu do estacionamento com sucesso!")

        case "M":
            print("Mostrar estacionamento")
            pos = len(pEst) - 2
            if pos < 0:
                print("Estacionamento está vazio...")
            else:
                while pos >= 0:
                    print(pEst[pos] + "(" + str(pEst[pos + 1]) + ")")
                    pos -= 2
                print("Fundo do estacionamento")
