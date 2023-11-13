def saoIguais(self, outra_lista):
    if (
        self.estaVazia() and outra_lista.estaVazia()
    ):  # Verifica se ambas as listas estão vazias
        print("Ambas as listas estão vazias.")
        return True
    elif self.estaVazia():
        print("A primeira lista está vazia, mas a segunda não.")
        return False
    elif outra_lista.estaVazia():
        print("A segunda lista está vazia, mas a primeira não.")
        return False

    if (
        self.tam() != outra_lista.tam()
    ):  # Verifica se ambas as listas têm o mesmo comprimento
        print("As listas têm tamanhos diferentes.")
        return False

    atual_self = self.cabeca
    atual_outra = outra_lista.cabeca

    while (
        atual_self is not None and atual_outra is not None
    ):  # Percorre as duas listas ao mesmo tempo e compara os valores dos nós
        if atual_self.pegaDado() != atual_outra.pegaDado():
            print("As listas são diferentes.")
            return False
        atual_self = atual_self.pegaProx()
        atual_outra = atual_outra.pegaProx()

    print("As listas são iguais.")
    return True
