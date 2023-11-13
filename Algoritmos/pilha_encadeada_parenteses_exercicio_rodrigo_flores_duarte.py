class Nodo:
    def __init__(self, vlr=None):
        self.vlr = vlr
        self.proximo = None


class PilhaEncadeada:
    def __init__(self):
        self.topo = None

    def push(self, vlr):  # push eh empilha
        temp = Nodo(vlr)
        temp.proximo = self.topo
        self.topo = temp

    def pop(self):  # pop eh desempilha
        if self.vazia():
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        return removido.vlr

    def vazia(self):
        return self.topo is None


def esta_correta(expressao):
    pilha = PilhaEncadeada()

    for caractere in expressao:
        if caractere == "(":
            pilha.push(caractere)
        elif caractere == ")":
            if pilha.vazia():
                return False
            pilha.pop()

    return pilha.vazia()


expressao = input("Digite a expressão aritmética para verificar os parênteses: ")

if esta_correta(expressao):
    print("A expressão está correta!")
else:
    print("não está correta...")
