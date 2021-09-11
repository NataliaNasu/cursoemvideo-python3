#leia o 1o termo de uma PA e a sua razao
#mostre os 10 primeiros termos

t1 = int(input('Digite o 1o termo de uma PA: '))
razao = int(input('A sua razão: '))
termo = t1
print(f'PA = ', end='')
p = 1
while p <= 10:
    print(f'{termo}', end=' > ')
    termo += razao
    p += 1
print('FIM!')