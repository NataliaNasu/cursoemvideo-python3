dias = int(input('Quantos dias você alugou o carro? '))
km = int(input('Quantos Km foram rodados? '))
aluguel = (dias * 60) + (km * 0.15)

print(f'\nCom um aluguel de {dias} dias e, {km}km rodados,')
print(f'O total a ser pago é de R${aluguel} reais!')
