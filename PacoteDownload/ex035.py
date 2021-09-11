c1 = float(input('Digite um comprimento: '))
c2 = float(input('Segundo comprimento: '))
c3 = float(input('Terceiro comprimento: '))
soma = c1 + c2 + c3
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('É possível criar um triângulo!')
else:
    print('Não é possível criar um triângulo.')
