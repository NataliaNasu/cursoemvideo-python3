#mostre todos numeros pares -> 1-50

'''Faz 50 iterações'''
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')

''' OU '''
print('\n')

for c in range(2, 51, 2):
    print(c, end=' ')
print('FIM')
'''Fez somente 25x iterações'''