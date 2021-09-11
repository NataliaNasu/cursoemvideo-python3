#jogo de par ou ímpar. interropme qndo o usuario perde.
#mostrar o total de vitórias consecutivas.
from random import randint

print('~'*30)
print('\t\t\033[2;31mPAR OU ÍMPAR:\033[m ')
print('~'*30)
total = 0
while True:
    pc = randint(0, 10)
    numero = int(input('Digite um valor: [0-10] '))
    jogador = input('A soma é par ou ímpar? [P/I] ').upper()
    print('-'*30)
    print(f'Pc: {pc} x Jogador: {numero}')
    soma = pc + numero
    if soma % 2 == 0:
        r = 'P'
        print(f'Soma = {soma} -> PAR')
    else:
        r = 'I'
        print(f'Soma = {soma} -> ÍMPAR')
    if jogador == r:
        print('Você VENCEU!')
        print('Vamos mais uma vez?!')
        total += 1
    else:
        print('GAME OVER!')
        break
    print('-'*30)

print(f'Você venceu {total} vezes!')