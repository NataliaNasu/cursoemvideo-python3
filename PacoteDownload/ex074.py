#gerar uma tupla de 5 numeros aleatórios
#mostrar a listagem dos números, e o menor e maior valor.
from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))

print('Números sorteados: ', end='')
for i in range(0, len(tupla)):
    print(f'{tupla[i]}', end=' ')
'''mais simplificado: '''
print(f'\nO maior valor da tupla é {max(tupla)}.')
print(f'E, o menor é {min(tupla)}.')

''' OU ~~
maior = menor = 0
for i in range(0, len(tupla)):
    if i == 0:
        maior = tupla[i]
        menor = tupla[i]
    else:
        if maior < tupla[i]:
            maior = tupla[i]
        if menor > tupla[i]:
            menor= tupla[i]
print(f'\nO maior valor da tupla é {maior}.')
print(f'E, o menor é {menor}.')'''