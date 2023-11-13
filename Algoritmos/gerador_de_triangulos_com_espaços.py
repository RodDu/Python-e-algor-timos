# Gerador de triangulos com espaços em branco

totalDeLinhas = int(input('Digite o total de linhas do triângulo: '))
while totalDeLinhas <= 0:
    totalDeLinhas = int(input('Digite o total de linhas do triângulo: '))


for linhas in range(1, totalDeLinhas+1):
    print('*' * linhas)