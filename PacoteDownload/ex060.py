#leia um número e mostre seu fatorial.

num = int(input('Digite um número: '))
fatorial = num
print(f'{num}! = {num} x ', end='')
for c in range(num-1, 0, -1):
    if c != 1:
        print(f'{c}', end=' x ')
        fatorial *= c
    else:
        print(f'{c}', end=' = ')
        fatorial *= c
print(f'{fatorial}')

print('\nCom while: \n')
n = int(input('Digite um número: '))
fat = n
print(f'{n}! = {n} x ', end='')
c = n - 1
while c > 0:
    if c != 1:
        print(f'{c}', end=' x ')
        fat *= c
        c -= 1
    else:
        print(f'{c}', end=' = ')
        fat *= c
        c -= 1
print(f'{fat}')