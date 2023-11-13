# Gerador de triangulos com espaços em branco

totalDeLinhas = int(input('Digite o total de linhas da pirâmide: '))
while totalDeLinhas <= 0:
    totalDeLinhas = int(input('Digite o total de linhas da pirâmide: '))


for linhas in range(1, totalDeLinhas+1):
    print(' ' * (totalDeLinhas - linhas), end='')
    print('*' * (linhas * 2 - 1))