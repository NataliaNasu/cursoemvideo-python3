#while: serve quando SE SABE a quantidade, ou quando NÃO SE SABE.

for c in range(1, 11):
    print(c)

c = 1
while c < 11:
    print(c)
    c += 1
print('FIM\n')

r = 'S'
while r == 'S':
    n = int((input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('FIM')

print('\nInforme quantos valores desejar: [0 -> interrompe] ')
n = 1
par = impar = total = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        total += 1
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {total} números.'
      f'\nSendo, {par} par(es) e, {impar} ímpar(es).')
