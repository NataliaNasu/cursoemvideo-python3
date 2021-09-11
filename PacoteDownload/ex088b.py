#profs
from random import  randint
from time import sleep
numero = []
jogos = []

print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)

total = int(input('Quantos jogos? '))
t = 1
while t <= total:
    c = 0
    while True:
        n = randint(1, 60)
        if n not in numero:
            numero.append(n)
            c += 1
        if c >= 6:
            break
    jogos.append(numero[:])
    numero.clear()
    t += 1
jogos.sort()
#print(f'Os números sorteados foram: {jogos}')

print(f'SORTEANDO {t} JOGOS:')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-'*30)
print(f'{"BOA SORTE!":^30}')
print('-'*30)