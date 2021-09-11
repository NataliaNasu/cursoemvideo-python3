#MEGA SENA
#pergunte qntos jogos serão gerados e sorteie 6 números entre 1 a 60.
#cadastre td em uma lista composta.
from random import randint

print('--'*18)
print(f'{"JOGO DA MEGA SENA":^36}')
print('--'*18)
jogo = int(input('Quantos jogos você quer que eu sorteie? '))
matriz = [[], []]

for i in range(0, 6):
    n = randint(1, 60)
    matriz[1].append(n)
print(f'{matriz}')
