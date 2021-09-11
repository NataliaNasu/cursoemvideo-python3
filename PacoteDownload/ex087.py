#aprimore o ex86, mostrando a soma de todos os numeros pares.
#a soma da terceira coluna e, o maior da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = somaT = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

for l in range(0, 3):
    somaT += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if maior < matriz[1][c]:
            maior = matriz[1][c]
print('-'*38)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-'*38)
print(f'A soma dos valores pares: {par}.')
print(f'A soma dos valores da 3a coluna: {somaT}.')
print(f'E, o maior número da 2a coluna: {maior}.')
print('-'*38)
