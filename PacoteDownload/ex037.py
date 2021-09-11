numero = int(input('Digite um número: '))
base = int(input('Entre as opções: '
                 '\n[1] Binário'
                 '\n[2] Octal'
                 '\n[3] Hexadecimal'
                 '\nQual a base de conversão? '))
if base == 1:
    print(f'> {numero} convertido em BINÁRIO = {bin(numero)[2:]}.')
elif base == 2:
    print(f'> {numero} convertido para OCTAL = {oct(numero)[2:]}.')
elif base == 3:
    print(f'> {numero} convertido para HEXADECIMAL = {hex(numero)[2:]}.')
else:
    print('>>> Opção inválida!')

'''O resultado aparece 0b = binario, 0o = octal e 0x = hexa
por isso, se utiliza o conceito de fatiamento em strings, 
só que em números.
Exemplo = numero[2:] -> aparece a partir do 2 e vai até o final.'''