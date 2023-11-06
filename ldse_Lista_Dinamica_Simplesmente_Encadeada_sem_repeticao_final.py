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
