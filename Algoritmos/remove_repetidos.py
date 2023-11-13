# def remove_repetidos(numeros):
#     result = []
#     for num in numeros:
#         if num not in result:
#             result.append(num)
#     return result

# numeros = []
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     numeros.append(num)

# if not numeros:
#     print("Lista vazia")
# else:
#     print(remove_repetidos(numeros))


def remove_repetidos(numeros):
    result = []
    for num in numeros:
        if num not in result:
            result.append(num)
    return result


numeros = []
num = None
while num != 0:
    num = int(input())
    if num != 0:
        numeros.append(num)

if not numeros:
    print("Lista vazia")
else:
    print(remove_repetidos(numeros))
