class Node:
    def __init__(self, vlr):
        self.dado = vlr
        self.prox = None

    def pegaDado(self):
        return self.dado

    def pegaProx(self):
        return self.prox

    def mudaDado(self, novoDado):
        self.dado = novoDado

    def mudaProx(self, novoProx):
        self.prox = novoProx


class LDSE:
    def __init__(self):
        self.cabeca = None

    def insereInicio(self, valor):
        temp = Node(valor)
        temp.mudaProx(self.cabeca)
        self.cabeca = temp

    def insereFinal(self, valor):
        temp = Node(valor)
        if self.cabeca is None:
            self.cabeca = temp
        else:
            aux = self.cabeca
            while aux.pegaProx() is not None:
                aux = aux.pegaProx()
            aux.mudaProx(temp)

    def insereAposValor(self, valor, vlrRef):
        temp = Node(valor)
        if self.cabeca is None:
            self.cabeca = temp
        else:
            aux = self.cabeca
            while aux.pegaDado() != vlrRef and aux.pegaProx() is not None:
                aux = aux.pegaProx()
            temp.mudaProx(aux.pegaProx())
            aux.mudaProx(temp)

    def mostraLista(self):
        aux = self.cabeca
        while aux is not None:
            print(aux.pegaDado(), end="-->")
            aux = aux.pegaProx()
        print(aux)

    def exclui(self, valor):
        ant = None
        temp = self.cabeca
        while temp is not None and temp.pegaDado() != valor:
            ant = temp
            temp = temp.pegaProx()
        if temp is None:
            return False
        else:
            if temp == self.cabeca:
                self.cabeca = temp.pegaProx()
            else:
                ant.mudaProx(temp.pegaProx())
            return True

    def estaVazia(self):
        return self.cabeca is None

    def tam(self):
        cont = 0
        pos = self.cabeca
        while pos is not None:
            cont += 1
            pos = pos.pegaProx()
        return cont

    def removeDuplicados(self):
        aux = self.cabeca
        while aux is not None:
            dado_atual = aux.dado
            segundo = aux
            while segundo.pegaProx() is not None:
                if segundo.pegaProx().dado == dado_atual:
                    segundo.mudaProx(segundo.pegaProx().pegaProx())
                else:
                    segundo = segundo.pegaProx()
            aux = aux.pegaProx()

    def insereOrdenado(self, valor):
        temp = Node(valor)
        if self.cabeca is None or valor < self.cabeca.pegaDado():
            temp.mudaProx(self.cabeca)
            self.cabeca = temp
        else:
            ant = None
            aux = self.cabeca
            while aux is not None and aux.pegaDado() <= valor:
                ant = aux
                aux = aux.pegaProx()
            ant.mudaProx(temp)
            temp.mudaProx(aux)

    def pertence(self, valor):
        aux = self.cabeca
        while aux is not None:
            if aux.pegaDado() == valor:
                print(f"{valor} existe na lista")
                return
            aux = aux.pegaProx()
        print(f"{valor} não existe na lista")

    def inverteLista(self):
        nova_lista = LDSE()
        aux = self.cabeca
        while aux is not None:
            nova_lista.insereInicio(aux.pegaDado())
            aux = aux.pegaProx()
        return nova_lista

    def mostraListaInvertida(self):
        print("Lista atual:")
        self.mostraLista()

        lista_invertida = self.inverteLista()

        print("Lista invertida:")
        lista_invertida.mostraLista()


def exibir_menu():
    print()
    print("*" * 50)
    print("[I] Inserir um novo elemento na lista")
    print("[R] Remover um elemento da lista")
    print("[V] Verificar se um número pertence à lista")
    print("[M] Mostrar os valores da lista")
    print("[E] Eliminar valores repetidos")
    print("[C] Criar uma segunda lista com os valores em ordem inversa")
    print("[S] Sair do programa")
    print("*" * 50)
    print()


lista = LDSE()  # Crie uma lista vazia

while True:
    exibir_menu()
    opcao = input("Digite sua opção: ").upper()

    if opcao == "I":
        while True:
            valor = input("Digite o valor a ser inserido (ou 'f' para finalizar): ")
            if valor.lower() == "f":
                print("Os valores da lista são:")
                lista.mostraLista()
                break  # Sai do loop quando 'f' é digitado
            try:
                valor = int(valor)
                lista.insereOrdenado(valor)
            except ValueError:
                print("Valor inválido. Digite um número inteiro ou 'f' para finalizar.")
    elif opcao == "R":
        print("Os valores da lista são:")
        lista.mostraLista()

        while True:
            valor = input("Digite o número a ser excluído (ou 'f' para finalizar): ")
            if valor.lower() == "f":
                break  # Sai do loop quando 'f' é digitado
            try:
                valor = int(valor)
                if lista.exclui(valor):
                    print(f"{valor} foi removido da lista.")
                else:
                    print(f"{valor} não foi encontrado na lista.")
            except ValueError:
                print("Valor inválido. Digite um número inteiro ou 'f' para finalizar.")
    elif opcao == "V":
        valor = int(input("Digite o valor a ser verificado: "))
        lista.pertence(valor)
    elif opcao == "M":
        print("Valores da lista:")
        lista.mostraLista()
    elif opcao == "E":
        lista.removeDuplicados()
        print("Valores duplicados removidos da lista.")
        print()
        print("Os valores da lista são:")
        lista.mostraLista()
    elif opcao == "C":
        print("Os valores da lista na ordem original são:")
        lista.mostraLista()
        print()
        lista_invertida = lista.inverteLista()
        print("Segunda lista com valores em ordem inversa:")
        lista_invertida.mostraLista()
    elif opcao == "S":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
