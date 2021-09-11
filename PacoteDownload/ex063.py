#fibonacci
print(' ***** FIBONACCI *****')
elementos = int(input('Digite um número: '))
t1 = 0
t2 = 1
print(f'Sequência fibonacci de {elementos} termos: '
      f'\n{t1} > {t2} > ', end='')
i = 2
while (i < elementos):
    t3 = t1 + t2
    print(f'{t3}', end=' > ')
    t1 = t2
    t2 = t3
    i += 1
print('FIM!')
