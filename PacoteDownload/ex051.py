#leia o 1o termo de uma PA. mostre os 10 primeiros termos.

t1 = int(input('Informe o primeiro termo de uma PA: '))
razao = int(input('Digite a razão: '))

print(t1, end=' > ')
soma = t1
for c in range(1, 10):
    soma += razao
    print(soma, end=' > ')
print('FIM!')

''' OU -> não consegui replicar'''
#p = int(input('Informe o primeiro termo: '))
#r = int(input('Digite a razão: '))
#decimo = p + (10 - 1) * r
#for c in range(p, 10 + r, r):
#    print(f'{c}', end=' -> ')
#print('FIM!')
