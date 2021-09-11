#mostre a tabuada de varios nº, de acordo com o usuário
#encerra somente qndo o valor for negativo

n = tabuada = 0
while True:
    n = int(input('Digite o nº da tabuada: '))
    if n <= 0:
        break
    else:
        print('-'*25)
        print(f'\t   TABUADA: {n}')
        print('-'*25)
        for i in range(1, 11):
            print(f'\t   {n} x {i} = {n*i}')
        print('-'*25)
print('FIM DO PROGRAMA!')