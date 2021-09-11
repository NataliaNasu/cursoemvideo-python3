#leia vários números, até digitar 999.
# apresente qntos foram digitados e a soma.

n = total = soma = 0
while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n != 999:
        soma += n
        total += 1
print(f'Foram digitados {total} números.'
      f'\nE, a soma entre eles é igual a {soma}.')

''' OU '''
print('\n')

num = c = s = 0
num = int(input('Digite um nº: [999 encerra] '))
while num != 999:
    s += num
    c += 1
    num = int(input('Digite um nº: [999 encerra] '))
print(f'Você digitou {c} nº(s), e a soma entre eles é igual a {s}.')