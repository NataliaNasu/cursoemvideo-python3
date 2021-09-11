#profs

lista = ('Lápis', 1.5, 'Borracha', 2.5, 'Caderno', 10.8,
         'Estojo', 20, 'Mochila', 100.5)

print('\033[31m--'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--'*20, '\033[m')

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R${lista[posicao]:>5.2f}')
print('\033[31m--\033[m'*20)