#leia vários números. mostre qntos foram digitados, mostre a lista em
#ordem decrescente, e se o valor 5 está ou não na lista.

lista = []
while True:
    n = lista.append(int(input('Digite um número: ')))
    opcao = input('Deseja continuar? [S/N] ').upper()
    while opcao not in 'NS':
        opcao = input('Deseja continuar? [S/N] ').upper()
    if opcao == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente: ', end='')
for v in lista:
    print(f'{v}', end=' ')
print()
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado...')
