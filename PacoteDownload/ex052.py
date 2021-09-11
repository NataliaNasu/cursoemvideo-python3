#leia um numero e verifique se ele é um primo ou não.

n = int(input('Digite um número: '))
divisores = 0
for c in range(1, n + 1):
    if n % c == 0:
        divisores += 1
if divisores > 2:
    print(f'O número {n} NÃO É um número primo!')
else:
    print(f'O número {n} É um número primo!')

''' OU '''
print('\n')

total = 0
num = int(input('Dgite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2:
    print(f'E por isso, ele É primo')
else:
    print(f'E por isso, ele NÃO É primo.')