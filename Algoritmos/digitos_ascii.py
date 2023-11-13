# def converte_digitos(frase):
#     varc = list(range(0, 30))
#     digitos = ""
#     for caractere in frase:
#         if caractere.isdigit():
#             digitos += caractere
#             varc[int(caractere)] = caractere
#     return digitos, varc


# frase = input()
# digitos, varc = converte_digitos(frase)

# print(int(digitos) if digitos != "" else 0)

# for i in range(len(varc)):
#     if isinstance(varc[i], str):
#         print(f"{varc[i]} :: {ord(varc[i])}")


def converte_digitos(frase):
    digitos = ""
    varc = []
    for caractere in frase:
        if caractere.isdigit():
            digitos += caractere
            varc.append((caractere, ord(caractere)))
    return digitos, varc


frase = input()
digitos, varc = converte_digitos(frase)

print(int(digitos) if digitos != "" else 0)

for digito, codigo in varc:
    print(f"{digito} :: {codigo}")
