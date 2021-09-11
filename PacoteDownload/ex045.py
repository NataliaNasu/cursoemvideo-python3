from random import randint
#jokepo
itens = {'Pedra', 'Papel', 'Tesoura'}
pc = randint(0, 2)

print('Ja-ken-po:' 
    '\n[0] Pedra '
    '\n[1] Papel '
    '\n[2] Tesoura: ')
jogador = int(input('Qual a sua jogada: '))

print('O pc = ', itens[pc])
print('O jogador = ', itens[jogador])
