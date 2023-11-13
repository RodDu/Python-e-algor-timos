class Node:
    def __init__(self, placa, manobras, next=None):
        self.placa = placa
        self.manobras = manobras
        self.next = next


class Stack:
    def __init__(self, max_size=10):
        self.top = None
        self.max_size = max_size
        self.size = 0

    def push(self, placa, manobras):
        if self.size == self.max_size:
            print("Estacionamento está cheio.")
            return
        new_node = Node(placa, manobras, self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            return -1, -1
        else:
            placa = self.top.placa
            manobras = self.top.manobras
            self.top = self.top.next
            self.size -= 1
            return placa, manobras

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.size == self.max_size

    def __contains__(self, placa):
        current = self.top
        while current:
            if current.placa == placa:
                return True
            current = current.next
        return False


pEst = Stack(max_size=10)
pRua = Stack(max_size=10)

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
            pl = input("Digite a placa do veículo: ").upper()
            pEst.push(pl, 0)

        case "S":
            print("Saída de veículo")
            if pEst.is_empty():
                print("Estacionamento vazio!")
            else:
                pl = input("Digite a placa do veículo para sair: ").upper()
                if not (pl in pEst):
                    print("Veículo não encontrado no estacionamento!")
                else:
                    manobras, placa = pEst.pop()
                    while placa != pl:
                        pRua.push(placa, manobras)
                        manobras, placa = pEst.pop()

                    manobras, placa = pRua.pop()
                    while placa != -1:
                        pEst.push(placa, manobras + 1)
                        manobras, placa = pRua.pop()
                    print(pl, "carro saiu do estacionamento com sucesso!")

        case "M":
            print("Mostrar estacionamento")
            current = pEst.top
            if current is None:
                print("Estacionamento está vazio...")
            else:
                while current:
                    print(current.placa + "(" + str(current.manobras) + ")")
                    current = current.next
                print("Fundo do estacionamento")
