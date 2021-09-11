#leia nome e peso de varias pessoas. mostre qntas foram cadastradas.
# crie uma listagem das mais pesadas e, das mais leves.
pessoas = list()
temporario = list()
maior = menor = 0
print(' \033[31mCADASTRO:\033[m ')
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    pessoas.append(temporario[:])
    temporario.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).upper()
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
    if opcao == 'N':
        break

print(f'Ao todo, foram cadastradas {len(pessoas)}.')
print(f'O maior peso foi {maior:.1f}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'"{p[0]}', end='" ')
print()
print(f'O menor peso foi {menor:.1f}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'"{p[0]}', end='" ')
