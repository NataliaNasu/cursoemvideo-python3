#jogo de adivinhar oq o pc sorteou.
# mas as tentativas vão até acertar.
# e deve mostrar quantas tentativas foram utilizadas.
from random import randint

print("*** \033[31mADIVINHE O NÚMERO\033[m ***")
pc = randint(0, 11)
jogador = int(input('Digite um número: '))

tentativa = 1
while jogador != pc:
    jogador = int(input('Número: '))
    tentativa += 1

print(f'PC: {pc} x JOGADOR: {jogador}')
print(f'PARABÉNS!!!')
print(f'Acertou com {tentativa} tentativa(s).')