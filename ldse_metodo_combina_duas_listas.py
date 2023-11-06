def combinaListas(self, outra_lista):
    listaCombinada = LDSE()
    atual_self = self.cabeca
    atual_outra = outra_lista.cabeca

    while atual_self is not None and atual_outra is not None:
        if atual_self.pegaDado() < atual_outra.pegaDado():
            listaCombinada.insereFinal(atual_self.pegaDado())
            atual_self = atual_self.pegaProx()
        else:
            listaCombinada.insereFinal(atual_outra.pegaDado())
            atual_outra = atual_outra.pegaProx()

    # Adicione os elementos restantes de ambas as listas
    while atual_self is not None:
        listaCombinada.insereFinal(atual_self.pegaDado())
        atual_self = atual_self.pegaProx()

    while atual_outra is not None:
        listaCombinada.insereFinal(atual_outra.pegaDado())
        atual_outra = atual_outra.pegaProx()

    return listaCombinada
