from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('JA-KEN-PO:'
      '\n[0] Pedra'
      '\n[1] Papel'
      '\n[2] Tesoura')
jogador = int(input('Qual a sua jogada? '))

print('JA')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-'*20)
print(f'Computador: {itens[pc]} \n\tX')
print(f'Jogador: {itens[jogador]}')
print('-'*20)
sleep(1)
if pc == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Parabéns, você VENCEU!')
    elif jogador == 2:
        print('Você PERDEU...')
    else:
        print('Jogada inválida!')
elif pc == 1:
    if jogador == 0:
        print('Você PERDEU...')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Parabéns, você VENCEU!')
    else:
        print('Jogada inválida!')
elif pc == 2:
    if jogador == 0:
        print('Parabéns, você VENCEU!')
    elif jogador == 1:
        print('Você PERDEU...')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')
