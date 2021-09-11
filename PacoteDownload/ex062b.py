t1 = int(input('Digite um número: '))
r = int(input('Razão: '))
t2 = t1 + r
fim = 10
termo = t1

t2 = t1 + r
pa = 2
print(f'PA {t1} = {t1} {t2} ', end='')
while pa < 10:
    t2 += r
    print(f'{t2}', end=' ')
    pa += 1

mais = 0
termo = int(input('\nDeseja mostrar mais quantos termos? '))
termo += fim
while termo != 0:
    t2 = t1 + r
    pa = 2
    termo += mais
    print(f'PA {t1} = {t1} {t2} ', end='')
    while pa < termo:
        t2 += r
        print(f'{t2}', end=' ')
        pa += 1
    mais = int(input('\nQuantos mais? '))
    if mais == 0:
        break
