#outra maneira, com indicações de mais perto...
from random import randint

print("*** \033[31mADIVINHE O NÚMERO\033[m ***")
pc = randint(0, 10)
acertou = False
maior = menor = tentativas = 0
while not acertou:
    jogador = int(input('Número? '))
    tentativas += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print(f'Tente um número MAIOR...')
        elif jogador > pc:
            print('Tente um número MENOR...')
print(f'\033[31mPARABÉNS!\033[m')
print(f'Acertou com {tentativas} tentativas!')