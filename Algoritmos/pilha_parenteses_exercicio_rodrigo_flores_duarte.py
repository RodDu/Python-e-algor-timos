def esta_correta(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == "(":
            pilha.append(caractere)
        elif caractere == ")":
            if not pilha:
                return False
            pilha.pop()

    return len(pilha) == 0


expressao = input("Digite a expressão aritmética para verificar os parênteses: ")

if esta_correta(expressao):
    print("A expressão está correta!")
else:
    print("A expressão não está correta...")
