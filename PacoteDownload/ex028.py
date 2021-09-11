from random import randint
from time import sleep

pc = randint(0, 5)
print('Pensei em um número, tente adivinhar... ')
jogador = int(input('Número de [0-5]: '))
print('Processando...')
sleep(2)
if jogador == pc:
    print('ACERTOU!')
else:
    print(f'ERROU! Eu tinha pensado no número {pc}.')