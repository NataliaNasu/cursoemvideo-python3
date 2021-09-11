#20 primeiros colocados da tabela do brasileirao
#mostre os 5 primeiros colocados, os último 4.
#a lista em ordem alfabética, e a posição do time da chapecoense.
cbf = ('chapecoense', 'time1', 'time2', 'time3', 'time4', 'time5', 'time6',
       'time7', 'time8', 'time9', 'time10', 'time11', 'time12', 'time13',
       'time14', 'time15', 'time16', 'time17', 'time18', 'time19')

print('~'*32)
print('CAMPEONATO BRASILEIRO DE FUTEBOL: ')
print('~'*32)
print(f'Times: ')
for pos, times in enumerate(cbf):
    print(f'{pos+1}: {times}')
print('-'*32)
print(f'Os cinco primeiros colocados: ')
print('-'*32)
for i in range(0, len(cbf[:5])):
    print(f'{i+1}o colocado: {cbf[i]}')
print('-'*32)
print(f'Os últimos 4 colocados: ')
print('-'*32)
#print(cbf[-4:])
for c in range(len(cbf), len(cbf)-4, -1):
    print(f'{c}o colocado: {cbf[c-1]}')
print('-'*32)
print(f'Tabela em ordem alfabética: ')
print('-'*32)
ordem = sorted(cbf)
for i in range(0, len(ordem)):
    print(ordem[i])
#    print(ordem[i], end='')
#    print(', ' if i != len(ordem)-1 else ' ', end='')
print('-'*32)
print(f'A chapecoense está na {cbf.index("chapecoense")+1}a posição.')
print('-'*32)
