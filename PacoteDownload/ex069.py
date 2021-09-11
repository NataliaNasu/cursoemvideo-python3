#cadastro. leia idade e sexo. Perguntar se desejar continuar.
#Mostrar qntas sao maiores de 18, qnts homens, e mulheres menores de 20.

print('-'*25)
print('\t  CADASTRO: ')
print('-'*25)
total = maior = menor = homem = 0
while True:
    print(f'\t  {total+1}a PESSOA: ')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper()
    print('-'*25)
    if idade >= 18:
        maior += 1
    if sexo in 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            menor += 1
    total += 1
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [S/N] ').upper()
    print('-' * 25)
    if opcao == 'N':
        break
print(f'Foram cadastradas {maior} pessoas maiores de 18 anos.')
print(f'Dos {total} cadastros, {homem} foram de homens.')
print(f'Existem {menor} mulheres com menos de 20 anos.')