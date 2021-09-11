#condicional
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')
'''>>>Outro jeito:'''
print('Carro novo!' if tempo <= 3 else 'Carro velho!')

nome = str(input('Digite o seu nome: '))
if nome == 'Gustavo: ':
    print('Que nome lindo!')
else:
    print('Que nome comum...')
'''ou...'''
print('Que nome lindo!' if nome == 'Gustavo' else 'Que nome comum...')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2
print(f'A sua média foi {media:.2f}')
if media >= 6.0:
    print('Sua média foi ótima! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
'''ou...'''
print('PARABÉNS' if media >= 6.0 else 'Estude mais...')
