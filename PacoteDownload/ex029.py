velocidade = int(input('Informe a velocidade do carro: '))

if velocidade > 80:
    print('Você foi MULTADO!')
    multa = (velocidade - 80) * 7
    print(f'E tem que pagar R${multa:.2f} reais de multa.')
else:
    print('Siga em frente!')

