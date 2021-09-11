#Leia vários números, e guarde em uma lista. crie 2 listas extras,
#onde uma irá conter os numeros apres, e a outra, os ímpares.
#mostre as 3 listas.

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    opcao = input('Deseja continuar? [S/N] ').upper()
    while opcao not in 'SN':
        opcao = input('Deseja continuar? [S/N] ').upper()
    if opcao == 'N':
        break

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('Lista: ', end='')
for v in lista:
    print(f'{v}', end=' ')
print()
print('Lista de nº PARES: ', end='')
for v in pares:
    print(f'{v}', end=' ')
print()
print('Lista de nº ÍMPARES: ', end='')
for v in impares:
    print(f'{v}', end=' ')