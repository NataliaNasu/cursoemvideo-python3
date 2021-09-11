import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O SENO de {angulo} graus, é {seno:.2f}.')
print(f'O COSSENO é {cos:.2f}')
print(f'E, a TANGENTE, é {tan:.2f}')