#leia 4 valores e guarde as em uma tupla.
#mostre, qntas vezes apareceu o numero 9,
#em que posição o valor 3 apareceu e quais foram os n pares.

numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print('Números digitados: ', end='')
for i in range(0, len(numeros)):
    print(numeros[i], end=' ')

print(f'\nO número 9 apareceu: {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O número três foi identificado na posição {numeros.index(3) + 1}.')
else:
    print('O número 3 não foi encontrado em nenhuma posição.')

''' OU ~~
encontrado = numeros.count(3)
if encontrado == 0:
    print('O número 3 não foi encontrado em nenhuma posição.')
else:
    print(f'O número três foi identificado na posição {numeros.index(3)+1}.')'''

print(f'Os números PARES foram encontrados: ')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(f'Na posição {c+1}: {numeros[c]}.')