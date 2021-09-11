#correção profs = MUITO MELHOR

num = int(input('Digite um número: '))
c = num
fatorial = 1
print(f'{num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)

n = int(input('Digite um número: '))
i = n
f = 1
print(f'{n}! = ', end='')
for i in range(i, 0, -1):
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
print(f)