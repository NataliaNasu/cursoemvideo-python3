#tupla definida de 0 a 20, por extenso.
#leia um número, e mostre por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número: [0-20] '))
    if 0 <= numero <= 20:
        break
print(f'O nº {numero} por extenso: {extenso[numero]}')
