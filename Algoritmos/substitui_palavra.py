def substitui_ultima_ocorrencia(frase, antiga, nova):
    indice = frase.rfind(antiga)
    if indice != -1:
        return frase[:indice] + nova + frase[indice + len(antiga) :]
    return frase


frase = input()
antiga = input()
nova = input()

resultado = substitui_ultima_ocorrencia(frase, antiga, nova)

print(resultado.upper())
