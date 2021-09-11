preco = float(input('Informe o preço dos produtos: R$'))
pagamento = int(input('Condições de pagamento: '
                      '\n[1] à vista no dinheiro/cheque'
                      '\n[2] à vista no cartão'
                      '\n[3] em até 2x no cartão'
                      '\n[4] 3x ou mais no cartão'
                      'Opção: '))

if pagamento == 1:
    desconto = preco * 10 / 100
    total = preco - desconto
    print(f'Com desconto de 10%, você economiza R${desconto:.2f} reais.')
elif pagamento == 2:
    desconto = preco * 5 / 100
    total = preco - desconto
    print(f'Com desconto de 5%, você economiza R${desconto:.2f} reais.')
elif pagamento == 3:
    total = preco
    parcela = preco / 2
    print(f'Em 2x, cada parcela vai custar R${parcela:.2f} SEM JUROS.')
elif pagamento == 4:
    total = preco + (preco * 20 / 100)
    tparcela = int(input('Quantas parcelas? '))
    parcela = total / tparcela
    print(f'Em {tparcela}x, cada parcela vai custar R${parcela:.2f} COM JUROS.')

print(f'A sua compra de R${preco}, sairá pelo preço de R${total:.2f} reais.')