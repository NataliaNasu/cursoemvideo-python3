#melhorar o ex62, indicar qntos termos deseja mostrar na tela

t1 = int(input('Digite um número: '))
r = int(input('Razão: '))
termo = t1
pa = 1
total = 0
mais = 10
print(f'PA = ', end='')
while mais != 0:
    total += mais
    while pa <= total:
        print(f'{termo}', end=' > ')
        termo += r
        pa += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print(f'Progressão finalizada! '
      f'\nForam apresentados {total} termos de uma PA.')
print('FIM!')