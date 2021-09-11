c1 = int(input('Digite um comprimento: '))
c2 = int(input('Segundo comprimento: '))
c3 = int(input('Terceiro comprimento: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Com essas medidas, é possível formar um triângulo!')
    if c1 == c2 == c3: #ou c1 == c2 and c2== c3
        print('E, ele é do tipo EQUILÁTERO!')
    elif c1 != c2 != c3:
        print('E, é do tipo ESCALENO!')
    elif c1 == c2 or c1 == c3 or c2 == c3:
        print('E, é do tipo ISÓSCELES!')
else:
    print('Não foi possível criar um triângulo...')