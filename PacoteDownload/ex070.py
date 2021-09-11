#Compras: leia o nome e o preco de varios produtos.
#questione se deseja continuar
#mostre o total gasto, qnts sao mais caros que 1000
#e o nome do produto mais barato.

print('\t *** COMPRAS ***')
total = c = caro = menor = 0
barato = opcao = ''
while True:
    print('-' * 25)
    print(f'\t{c+1}o produto: ')
    print('-'*25)
    nome = input('Produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        caro += 1
    if c == 0:
        menor = preco
        barato = nome
        '''SIMPLIFICAÇÃO:
        if c == 0 or preco < menor:
            menor = preco
            barato = nome
            *porque repetem'''
    else:
        if menor > preco:
            menor = preco
            barato = nome
    c += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar? [S/N] ').upper()
    if opcao == 'N':
        break

print(f'O total da compra foi R${total:.2f} reais.')
print(f'Dos {c} produtos, {caro} custaram mais de R$1000.00 reais.')
print(f'O produto mais barato foi o/a {barato}, que custou R${menor:.2f}.')