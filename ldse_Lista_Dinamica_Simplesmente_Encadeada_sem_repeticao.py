class Node:
    def __init__(self, vlr):  # Inicializa o nó
        self.dado = vlr
        self.prox = None

    def pegaDado(self):  # Retorna o dado do nó
        return self.dado

    def pegaProx(self):  # Retorna o valor de prox
        return self.prox

    def mudaDado(self, novoDado):  # Muda o valor do dado
        self.dado = novoDado

    def mudaProx(self, novoProx):  # Muda o valor de prox
        self.prox = novoProx


class LDSE:
    def __init__(self):  # Inicializa a LDSE
        self.cabeca = None

    def insereInicio(self, valor):  # Insere no início da LDSE
        temp = Node(valor)
        temp.mudaProx(self.cabeca)
        self.cabeca = temp

    def insereFinal(self, valor):  # Insere no final da LDSE
        temp = Node(valor)
        if self.cabeca is None:
            self.cabeca = temp
        else:
            aux = self.cabeca
            while aux.pegaProx() is not None:
                aux = aux.pegaProx()
            aux.mudaProx(temp)

    def insereAposValor(self, valor, vlrRef):  # Insere em posição determinada da LDSE
        temp = Node(valor)
        if self.cabeca is None:
            self.cabeca = temp
        else:
            aux = self.cabeca
            while aux.pegaDado() != vlrRef and aux.pegaProx() is not None:
                aux = aux.pegaProx()
            temp.mudaProx(aux.pegaProx())
            aux.mudaProx(temp)

    def mostraLista(self):  # Mostra a LDSE
        aux = self.cabeca
        while aux is not None:
            print(aux.pegaDado(), end="-->")
            aux = aux.pegaProx()
        print(aux)

    def exclui(self, valor):  # Exclui o valor da lista
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

    def estaVazia(self):  # Retorna o estado da LDSE
        return self.cabeca is None

    def tam(self):  # Retorna a quantidade de nós da LDSE
        cont = 0
        pos = self.cabeca
        while pos is not None:
            cont += 1
            pos = pos.pegaProx()
        return cont

    def remove_repeticoes(self):
        if self.estaVazia():
            return

        atual = self.cabeca

        while atual is not None:
            valor_atual = atual.pegaDado()
            ant = atual
            seguinte = atual.pegaProx()

            while seguinte is not None:
                if seguinte.pegaDado() == valor_atual:
                    ant.mudaProx(seguinte.pegaProx())
                else:
                    ant = seguinte
                seguinte = seguinte.pegaProx()

            atual = atual.pegaProx()
