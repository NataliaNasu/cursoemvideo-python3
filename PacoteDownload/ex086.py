#crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
#mostre elana tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-'*30)

'''
matriz = [[], [], []]
for l in ranfe(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um número na posição [{l}, {c}]: '))
        if valor % 2 == 0:
            par += valor
        if l == 0:
            matriz[0].append(valor)
        elif l == 1:
            matriz[1].append(valor)
        elif l == 2:
            matriz[2].append(valor)'''

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
