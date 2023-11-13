def insereAposRef(self, valor, vlrRef):
    temp = Node(valor)

    if self.cabeca == None:
        self.cabeca = temp
        temp.mudaProx = self.cabeca

    else:
        aux = self.cabeca

        while aux.pegaDado() != vlrRef and aux.pegaProx() != self.cabeca:
            aux = aux.pegaProx()

        if aux.pegaDado() == vlrRef or aux.pegaProx() == self.cabeca:
            temp.mudaProx = aux.pegaProx()
            aux.mudaProx = temp

            if aux.pegaProx() == self.cabeca:
                self.cabeca = temp
