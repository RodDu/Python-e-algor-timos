# def converte_maiusculo(c):
#     return chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c

# def converte_minusculo(c):
#     return chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c

# def converte_palavra_minuscula(palavra):
#     return ''.join(converte_minusculo(c) for c in palavra)

# def anagrama(p1, p2):
#     p1_minuscula = converte_palavra_minuscula(p1)
#     p2_minuscula = converte_palavra_minuscula(p2)

#     if sorted(p1_minuscula) == sorted(p2_minuscula):
#         return True
#     else:
#         return False

# p1 = input("Digite a primeira palavra: ")
# p2 = input("Digite a segunda palavra: ")

# if anagrama(p1, p2):
#     print("ANAGRAMAS")
# else:
#     print("NAO")


def converte_maiusculo(c):
    return chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c


def converte_minusculo(c):
    return chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c


def converte_palavra_minuscula(palavra):
    return "".join(converte_minusculo(c) for c in palavra)


def anagrama(p1, p2):
    p1_minuscula = converte_palavra_minuscula(p1)
    p2_minuscula = converte_palavra_minuscula(p2)

    if sorted(p1_minuscula) == sorted(p2_minuscula):
        return True
    else:
        return False


p1 = input("Digite a primeira palavra: ").strip()
p2 = input("Digite a segunda palavra: ").strip()

if anagrama(p1, p2):
    print("ANAGRAMAS")
else:
    print("NAO")
