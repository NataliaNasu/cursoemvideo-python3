#Leia 5 valores e guarde-os em uma lista.
#mostre ql foi o maior e menor e as suas posições.

numeros = []

for c in range(0, 5):
    numeros.append(int(input('Digite um número: ')))

print('Lista de números: ', end='')
for num in numeros:
    print(num, end=' ')
print('\n')

maior = menor = 0
for posicao, v in enumerate(numeros):
    if posicao == 0:
        maior = numeros[posicao]
        menor = numeros[posicao]
    else:
        if maior < numeros[posicao]:
            maior = numeros[posicao]
        if menor > numeros[posicao]:
            menor = numeros[posicao]

print(f'O maior valor digitado foi {maior}'
      f'\ne, se encontra nas posições: ', end='')
for posicao, mm in enumerate(numeros):
    if numeros[posicao] == maior:
        print(f'{posicao+1}', end='... ')
print('\n')
print(f'O menor valor digitado foi {menor}'
      f'\ne, se encontra nas posições: ', end='')
for posicao, mm in enumerate(numeros):
    if numeros[posicao] == menor:
        print(f'{posicao+1}', end='... ')