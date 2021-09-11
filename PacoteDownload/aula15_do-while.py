#while infinito com break

c = 1
while c <= 10:
    print(f'{c} > ', end='')
    c += 1
print('FIM!')

n = soma = 0
while n != 999:
    n = int(input('Digite um número: [999]'))
    if n != 999:
        soma += n
print(f'Soma = {soma}')
'''whilw infinito'''
s = 0
print('\nCom while infinito + break\n')
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s += num
print((f'Soma = {s}'))